-- Measure TDDS sequences
-- by Michael Waltl, IUE, TU Wien, 2014 -- now and more

-- configuration parameters for TDDS, to be settled by KeitleyMeasurements.py
-- VDSStress = 0.0
-- VGSStress = 0.0
-- tStress   = 1.0

-- VDSRead   = 0.0
-- VGSRead   = 0.0
-- tRead     = 2.0

-- traces = 1

-- samplesPerDecade  = 200 -- for log sampling
-- tSampleLin        = -1  -- positive value for linear sampling

-- current ranges configuration, hard coded
--IdStressRange = 1e-6
--IdReadRange   = 1e-8
--IgsRange      = 1e-7


-- common initialization stuff
reset()
errorqueue.clear()
format.asciiprecision = 11
Ilimit                = 10 * math.max(IdStressRange, IdReadRange)
logtinc               = math.pow(10, 1/samplesPerDecade)
defaultBufferSize     = 20000 -- sufficient for tRead <= 1ks

-- global functions
function init_smu(smu, rangev)
    display['smua'].measure.func = display.MEASURE_DCAMPS
    display['smub'].measure.func = display.MEASURE_DCAMPS

    smu.source.func     = smu.OUTPUT_DCVOLTS
    smu.source.rangev   = rangev
    smu.source.levelv   = 0
    smu.source.settling = smu.SETTLE_FAST_POLARITY
    smu.source.limiti   = Ilimit

    return smu
end

function make_buffer(s, r)
    b = s.makebuffer(2*defaultBufferSize)
    b.clear()
    b.appendmode = 1
    b.collecttimestamps = 1
    b.timestampresolution = r
    return b
end

compl_bit = 4*16 -- 0x40
function in_compliance(x)
	return math.mod(x, 2*compl_bit) >= compl_bit
end

function print_buffers(b1, b2) -- print fast/slow tandem buffers b1 and b2
	print('#n t tc Is')
	print('#u s s A')
	for i = 2, b1.n do -- skip time zero, bad for log-scale
		print(b1.timestamps[i], 0, in_compliance(b1.statuses[i]) and 'compliance' or b1[i])
	end
	dt = b2.basetimestamp - b1.basetimestamp
	for i = 2, b2.n do -- skip time zero, bad for log-scale
		print(b2.timestamps[i] + dt, 0, in_compliance(b2.statuses[i]) and 'compliance' or b2[i])
	end
	b1.clear()
	b2.clear()
	print()
	print('#buffer end')
end

-- init smu's and buffers
gate   = init_smu(smub, math.max(math.abs(VGSStress), math.abs(VGSRead)))
drain  = init_smu(smua, math.max(math.abs(VDSStress), math.abs(VDSRead)))

stressbuffast = make_buffer(drain, 1e-6)
stressbufslow = make_buffer(drain, 1e-3)
readbuffast   = make_buffer(drain, 1e-6)
readbufslow   = make_buffer(drain, 1e-3)

-- TDDS functions
function init_measure_fast(smu, rangei)
	smu.measure.delay = smu.DELAY_OFF
	if smu.measure.analogfilter then smu.measure.analogfilter = 0 end 
	smu.measure.rangei = rangei -- turns autorangei off automatically
	smu.measure.nplc = 0.001
	smu.measure.autozero = smu.AUTOZERO_ONCE
	smu.measure.nplc = 0.01
	smu.measure.autozero = smu.AUTOZERO_ONCE
	smu.measure.nplc = 1
	smu.measure.autozero = smu.AUTOZERO_ONCE
	smu.measure.nplc = 5
	smu.measure.autozero = smu.AUTOZERO_ONCE
	smu.measure.nplc = 25
	smu.measure.autozero = smu.AUTOZERO_ONCE
end

function stress_cycle_const(tmax)
	init_measure_fast(drain, IdStressRange)
	drain.trigger.measure.i(stressbuffast)
        
    -- linear sampling
	drain.measure.nplc  = tSampleLin -- 0.01/50 = 0.2ms integration time = 5kHz
	drain.source.levelv = VDSStress
	gate.source.levelv  = VGSStress
	drain.trigger.initiate() -- start measurement here
	mytimer.wait(tmax)
	drain.abort()
end

function relax_cycle_const(tmax)
	init_measure_fast(drain, IdReadRange)
	drain.trigger.measure.i(readbuffast)

    -- linear sampling
	drain.measure.nplc  = tSampleLin -- 0.01/50 = 0.2ms integration time = 5kHz
	drain.source.levelv = VDSRead
	gate.source.levelv  = VGSRead
	drain.trigger.initiate() -- start measurement here
	mytimer.wait(tmax)
	drain.abort()
end

function stress_relax_cycle(ts, tr)
    -- sampling with constant sampling rate
    if tSampleLin > 0 then
    	-- stress section
        stress_cycle_const(ts) 

        -- recovery section
	    relax_cycle_const(tr)
    end

	-- print buffers to be read from python script
	print('#m stress Vg=' .. VGSStress .. ' Vd=' .. VDSStress .. ' T=' .. temperature)
	print_buffers(stressbuffast, stressbufslow)
	print('#m relax Vg=' .. VGSRead .. ' Vd=' .. VDSRead .. ' T=' .. temperature)
        print_buffers(readbuffast, readbufslow)
end

-- start TDDS cycles 
temperature = 25 -- should be read from LakeShore temperature controller
tSampleLin  = tSampleLin*50 -- nplc value!!!

drain.trigger.measure.action = drain.ENABLE -- enable measuring drain current
drain.trigger.arm.stimulus   = 0
drain.trigger.count          = defaultBufferSize

-- init timer
mytimer = trigger.timer[1]
mytimer.count = 1
mytimer.passthrough = false

gate.source.output  = gate.OUTPUT_ON
drain.source.output = drain.OUTPUT_ON

for i = 1, traces do
    stress_relax_cycle(tStress, tRead)
end

gate.source.output  = gate.OUTPUT_OFF
drain.source.output = drain.OUTPUT_OFF

reset()

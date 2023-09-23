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


-- common initialization stuff
errorqueue.clear()
node[1].errorqueue.clear()
node[2].errorqueue.clear()
node[3].errorqueue.clear()

format.asciiprecision = 11
Ilimit                = 10 * math.max(IDStressRange, IDReadRange)
IlimitDiodeA          = 10 * math.max(IDiodeAStressRange, IDiodeAReadRange)
IlimitDiodeB          = 10 * math.max(IDiodeBStressRange, IDiodeBReadRange)
--logtinc               = math.pow(10, 1/samplesPerDecade)
defaultBufferSize     = 20000 -- sufficient for tRead <= 1ks

-- global functions
function init_smu(smu, rangev, ilim)
    node[1].display['smua'].measure.func = display.MEASURE_DCAMPS
    node[1].display['smub'].measure.func = display.MEASURE_DCAMPS
    node[2].display['smua'].measure.func = display.MEASURE_DCAMPS
    node[2].display['smub'].measure.func = display.MEASURE_DCAMPS
    node[3].display['smua'].measure.func = display.MEASURE_DCAMPS	
    node[3].display['smub'].measure.func = display.MEASURE_DCAMPS

    smu.source.func     = smu.OUTPUT_DCVOLTS
    smu.source.rangev   = rangev
    smu.source.levelv   = 0
    smu.source.settling = smu.SETTLE_FAST_POLARITY
    smu.source.limiti   = ilim

    return smu
end

function make_buffer(s, r)
    s.nvbuffer1.clear()
    s.nvbuffer2.clear()
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
	print('#n t tc Id Is')
	print('#u s s A A')
	for i = 2, b1.n do -- skip time zero, bad for log-scale
		print(b1.timestamps[i], 0, in_compliance(b1.statuses[i]) and 'compliance' or b1[i], in_compliance(b2.statuses[i]) and 'compliance' or b2[i])
	end
	--dt = b2.basetimestamp - b1.basetimestamp
	--for i = 2, b2.n do -- skip time zero, bad for log-scale
	--	print(b2.timestamps[i] + dt, 0, in_compliance(b2.statuses[i]) and 'compliance' or b2[i])
	--end
	b1.clear()
	b2.clear()
	print()
	print('#buffer end')
end

-- init smu's and buffers
gate   = init_smu(gateSMU,    math.max(math.abs(VGSStress),     math.abs(VGSRead)), Ilimit)
drain  = init_smu(drainSMU,   math.max(math.abs(VDStress),      math.abs(VDRead)),  Ilimit)
source = init_smu(sourceSMU,  math.max(math.abs(VSStress),      math.abs(VSRead)),  Ilimit)
bulk   = init_smu(bulkSMU,    math.max(math.abs(VBStress),      math.abs(VBRead)),  Ilimit)
diodeA = init_smu(diodeASMU,  math.max(math.abs(VDiodeAStress), math.abs(VDiodeARead)), IlimitDiodeA)
diodeB = init_smu(diodeBSMU,  math.max(math.abs(VDiodeBStress), math.abs(VDiodeBRead)), IlimitDiodeB)

stressbuffast_D = make_buffer(drain,  1e-6)
readbuffast_D   = make_buffer(drain,  1e-6)
stressbuffast_S = make_buffer(source, 1e-6)
readbuffast_S   = make_buffer(source, 1e-6)


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
    init_measure_fast(drain,  IDStressRange)
    init_measure_fast(source, IDStressRange)

    drain.trigger.measure.i(stressbuffast_D)
    source.trigger.measure.i(stressbuffast_S)
        
    -- linear sampling
    drain.measure.nplc   = tSampleLin -- 0.01/50 = 0.2ms integration time = 5kHz
    source.measure.nplc  = tSampleLin -- 0.01/50 = 0.2ms integration time = 5kHz
    drain.source.levelv  = VDStress
    diodeA.source.levelv = VDiodeAStress
    diodeB.source.levelv = VDiodeBStress
    gate.source.levelv   = VGSStress
    bulk.source.levelv   = VBStress
    source.source.levelv = VSStress
    drain.trigger.initiate()  -- start measurement here
    source.trigger.initiate() -- start measurement here
    mytimer.wait(tmax)
    drain.abort()
    source.abort()
end

function relax_cycle_const(tmax)
    init_measure_fast(drain,  IDReadRange)
    init_measure_fast(source, IDReadRange)

    drain.trigger.measure.i(readbuffast_D)
    source.trigger.measure.i(readbuffast_S)

    -- linear sampling
    drain.measure.nplc   = tSampleLin -- 0.01/50 = 0.2ms integration time = 5kHz
    source.measure.nplc  = tSampleLin -- 0.01/50 = 0.2ms integration time = 5kHz
    drain.source.levelv  = VDRead
    diodeA.source.levelv = VDiodeARead
    diodeB.source.levelv = VDiodeBRead	
    gate.source.levelv   = VGSRead
    bulk.source.levelv   = VBRead
    source.source.levelv = VSRead
    drain.trigger.initiate() -- start measurement here
    source.trigger.initiate() -- start measurement here
    mytimer.wait(tmax)
    drain.abort()
    source.abort()
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
    print('#m stress Vg=' .. VGSStress .. ' Vd=' .. VDStress)
    print_buffers(stressbuffast_D, stressbuffast_S)
    print('#m relax Vg=' .. VGSRead .. ' Vd=' .. VDRead)
    print_buffers(readbuffast_D, readbuffast_S)
end

-- start TDDS cycles 
tSampleLin  = tSampleLin*50 -- nplc value!!!

drain.trigger.measure.action = drain.ENABLE -- enable measuring drain current
drain.trigger.arm.stimulus   = 0
drain.trigger.count          = defaultBufferSize

source.trigger.measure.action = source.ENABLE -- enable measuring source current
source.trigger.arm.stimulus   = 0
source.trigger.count          = defaultBufferSize

-- init timer
mytimer = trigger.timer[1]
mytimer.count = 1
mytimer.passthrough = false

-- turn smu's on
gate.source.output   = gate.OUTPUT_ON
drain.source.output  = drain.OUTPUT_ON
source.source.output = source.OUTPUT_ON
bulk.source.output   = bulk.OUTPUT_ON
diodeA.source.output = diodeA.OUTPUT_ON
diodeB.source.output = diodeB.OUTPUT_ON

-- measure trace
for i = 1, traces do
    stress_relax_cycle(tStress, tRead)
end

-- delete dynamic allocated buffer
stressbuffast_D = nil
readbuffast_D   = nil
stressbuffast_S = nil
readbuffast_S   = nil

-- turn smu's off
gate.source.output   = gate.OUTPUT_OFF
drain.source.output  = drain.OUTPUT_OFF
source.source.output = source.OUTPUT_OFF
bulk.source.output   = bulk.OUTPUT_OFF
diodeA.source.output = diodeA.OUTPUT_OFF
diodeB.source.output = diodeB.OUTPUT_OFF

reset()

-- init Keithleys
errorqueue.clear()
-- clear error queues
if initNode1 == 1 then
    node[1].errorqueue.clear()
end

if initNode2 == 1 then
    node[2].errorqueue.clear()	 
end

if initNode3 == 1 then
    node[3].errorqueue.clear()
end

smulist = {}

format.asciiprecision = 11
--Ilimit                = 10 * math.max(IDStressRange, IDReadRange)
--IlimitDiodeA          = 10 * math.max(IDiodeAStressRange, IDiodeAReadRange)
--IlimitDiodeB          = 10 * math.max(IDiodeBStressRange, IDiodeBReadRange)
--logtinc               = math.pow(10, 1/samplesPerDecade)
defaultBufferSize     = 20000 -- sufficient for tRead <= 1ks

-- global functions
function init_smu(use, smus, rangev, ilim)
    if use == 0 then
       return nil
    end

    disp = nil
    if smus == 'node[1].smua' then
        smu  = node[1].smua
        disp = node[1].display['smua']
    end
    if smus == 'node[1].smub' then
        smu  = node[1].smub
        disp = node[1].display['smub']
    end
    if smus == 'node[2].smua' then
        smu  = node[2].smua
        disp = node[2].display['smua']
    end
    if smus == 'node[2].smub' then
        smu  = node[2].smub
        disp = node[2].display['smub']
    end
    if smus == 'node[3].smua' then
        smu  = node[3].smua
        disp = node[3].display['smua']
    end
    if smus == 'node[3].smub' then
        smu  = node[3].smub
        disp = node[3].display['smub']
    end
    
    if disp then
        disp.measure.func = display.MEASURE_DCAMPS
    end

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
	--print(b1.n)
	--print(b2.n)
	for i = 2, b1.n-2 do -- skip time zero, bad for log-scale
		--print(b1.timestamps[i], 0, in_compliance(b1.statuses[i]) and 'compliance' or b1[i], in_compliance(b2.statuses[i]) and 'compliance' or b2[i])
		print(b1.timestamps[i], 0, b1[i], b2[i])
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
gate   = init_smu(gateSMU_use,   gateSMU,   gateVMax,   gateIMax)
drain  = init_smu(drainSMU_use,  drainSMU,  drainVMax,  drainIMax)
source = init_smu(sourceSMU_use, sourceSMU, sourceVMax, sourceIMax)
bulk   = init_smu(bulkSMU_use,   bulkSMU,   bulkVMax,   bulkIMax)
addA   = init_smu(addASMU_use,   addASMU,   addAVMax,   addAIMax)
addB   = init_smu(addBSMU_use,   addBSMU,   addBVMax,   addBIMax)

stressbuffast_D = make_buffer(drain,  1e-6)
readbuffast_D   = make_buffer(drain,  1e-6)
stressbuffast_S = make_buffer(source, 1e-6)
readbuffast_S   = make_buffer(source, 1e-6)

-- TDDS functions
function setVoltage(smu, voltage)
    if smu ~= nil then
--        if type(voltage) == "number" then
   	    smu.source.levelv = voltage
--   	else
--   	    smu.source.levelv = voltage[i]
--   	end
    end
end

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

	--smu.trigger.count = 1000
end

function stress_cycle_const(tmax)
    init_measure_fast(drain,  1e-3) --drainIMaxStress)
    init_measure_fast(source, 1e-3) --sourceIMaxStress)

    drain.trigger.measure.i(stressbuffast_D)
    source.trigger.measure.i(stressbuffast_S)
        
    -- linear sampling
    drain.measure.nplc   = tSampleLin -- 0.01/50 = 0.2ms integration time = 5kHz
    source.measure.nplc  = tSampleLin -- 0.01/50 = 0.2ms integration time = 5kHz
    setVoltage(drain, VDStress)
    setVoltage(addA, VAStress)
    setVoltage(addB, VBStress)
    setVoltage(gate, VGStress)
    setVoltage(bulk, VBStress)
    setVoltage(source, VStress)
    timeStressStart = os.time()
    drain.trigger.initiate()  -- start measurement here
    source.trigger.initiate() -- start measurement here
    mytimer.wait(tmax)
    drain.abort()
    source.abort()
    timeStressEnd = os.time()
end

function relax_cycle_const(tmax)
    init_measure_fast(drain,  drainIMaxRead)
    init_measure_fast(source, sourceIMaxRead)

    drain.trigger.measure.i(readbuffast_D)
    source.trigger.measure.i(readbuffast_S)

    -- linear sampling
    drain.measure.nplc   = tSampleLin -- 0.01/50 = 0.2ms integration time = 5kHz
    source.measure.nplc  = tSampleLin -- 0.01/50 = 0.2ms integration time = 5kHz
    setVoltage(drain,  VDRead)
    setVoltage(addA,   VARead)
    setVoltage(addB,   VBRead)
    setVoltage(gate,   VGRead)
    setVoltage(bulk,   VBRead)
    setVoltage(source, VSRead)
    timeReadStart = os.time()
    drain.trigger.initiate()  -- start measurement here
    source.trigger.initiate() -- start measurement here
    mytimer.wait(tmax)
    drain.abort()
    source.abort()
    timeReadEnd = os.time()
end

function stress_relax_cycle(ts, tr)
    -- sampling with constant sampling rate
    if tSampleLin > 0 then
    	-- stress section
		if ts > 0 then
			stress_cycle_const(ts) 
        end

        -- recovery section
        if tr > 0 then
			relax_cycle_const(tr)
        end
    end

    -- print buffers to be read from python script
    if ts > 0 then
        print('#m stress Vg=' .. VGStress .. ' Vd=' .. VDStress .. ' timeStressStart=' .. timeStressStart .. ' timeStressEnd=' .. timeStressEnd)
        print_buffers(stressbuffast_D, stressbuffast_S)
    end
    if tr > 0 then
        print('#m relax Vg=' .. VGRead .. ' Vd=' .. VDRead .. ' timeReadStart=' .. timeReadStart .. ' timeReadEnd=' .. timeReadEnd)
        print_buffers(readbuffast_D, readbuffast_S)
    end
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
if addA ~= nil then
	addA.source.output   = addA.OUTPUT_ON
end
if addB ~= nil then
	addB.source.output   = addB.OUTPUT_ON
end

---- measure trace
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
if addA ~= nil then
	addA.source.output   = addA.OUTPUT_OFF
end
if addB ~= nil then
	addB.source.output   = addB.OUTPUT_OFF
end

reset()

-- CONFIGURATION SECTION

-- idvg for cp01dev01
--Vds = 0.001
--Vbs = 0.000  --sweep(5.0, -5.0, -0.25)
--Vgs = sweep(-20, 20, 5)

-- CONFIGURATION SECTION END

reset()
--tsplink.reset()
errorqueue.clear()
smulist = {}

function def_smu(s, d, i, irange)
--	s = 'smu' .. s
--	d = '# ' .. d .. ' was node[' .. n .. '].' .. s
	smu = s
	table.insert(smulist, smu)
	display['smua'].measure.func = display.MEASURE_DCAMPS
	display['smub'].measure.func = display.MEASURE_DCAMPS

    if irange == 0 then
        smu.measure.autorangei  = smu.AUTORANGE_ON
        smu.measure.autozero    = smu.AUTOZERO_AUTO
        smu.measure.delay       = smu.DELAY_AUTO
        smu.measure.delayfactor = 1.3
    else
        smu.measure.rangei   = irange
        smu.measure.autozero = smu.AUTOZERO_ONCE
        smu.measure.delay    = smu.DELAY_OFF
    end

	smu.measure.nplc        = nplcValue
	smu.source.func         = smu.OUTPUT_DCVOLTS
	smu.source.levelv       = 0
	smu.source.autorangev   = smu.AUTORANGE_ON
	smu.source.limiti       = i

	return smu
end

function smus_on(on)
	local o = (on and smulist[1].OUTPUT_ON) or smulist[1].OUTPUT_OFF
	for i, s in pairs(smulist) do
		s.source.output = o
	end
end

-- init timer
mytimer             = trigger.timer[1]
mytimer.count       = 1
mytimer.passthrough = false

-- init SMUs
gate   = def_smu(gateSMU,  'gate',   IgateMax,  IgateRange)
drain  = def_smu(drainSMU, 'drain',  IdrainMax, IdrainRange)


function measure()
	if measureIG > 0 then
		if gate.source.compliance   then Ig = 'compliance' Vg = Ig else Ig, Vg = gate.measure.iv() end
        else
	        Ig = 1e-100
		Vg = gate.source.levelv
        end

	if drain.source.compliance  then Id = 'compliance' Vd = Id else Id, Vd = drain.measure.iv() end
	print(Vg, Ig, Vd, Id)
end

function stressCycle()
	print('## startStress')

	smus_on(true)

	drain.source.levelv = VDSStress
        gate.source.levelv  = VGSStress
	mytimer.wait(tStress)
	drain.source.levelv = 0.
        gate.source.levelv  = 0.

	smus_on(false)	

	print('## endStress')
end

function measureIDVG(Vds)
	smus_on(true)

	print('## startIDVG')
	print('#n Vg Ig Vd Id')

	drain.source.levelv = Vds

	for _, Vgs_ in ipairs(Vgs) do
	    gate.source.levelv = Vgs_
	    measure()
	end

	print('## endIDVG')

	smus_on(false)
end

-- ordinary idvg
measureIDVG(Vds)

-- stress cycle
if tStress > 0 then
   stressCycle()

   if tIDVGDelay > 0 then   
      measureIDVG(Vds) 
   end
end

reset()


-- CONFIGURATION SECTION

-- idvg for cp01dev01
--Vds = 0.001
--Vbs = 0.000  --sweep(5.0, -5.0, -0.25)
--Vgs = sweep(-20, 20, 5)

-- CONFIGURATION SECTION END

reset()
tsplink.reset()
errorqueue.clear()
smulist = {}

-- Init TSP Link
--tspNodesFound = tsplink.initialize(0)
--print("Nodes found = " .. tspNodesFound)


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

--gate   = def_smu(smua, 'gate',   1e-5)
--drain  = def_smu(smub, 'drain',  1e-5)

gate   = def_smu(gateSMU,  'gate',   IgateMax,  IgateRange)
drain  = def_smu(drainSMU, 'drain',  IdrainMax, IdrainRange)
--dummy  = def_smu(node[2].smua, 'drain2',  IdrainMax, IdrainRange)

function measure()
	if measureIG > 0 then
		if gate.source.compliance   then Ig = 'compliance' Vg = Ig else Ig, Vg = gate.measure.iv() end
        else
	    Ig = 1e-100
            Vg = gate.source.levelv
        end

--	if measID > 0 then
		if drain.source.compliance  then Id = 'compliance' Vd = Id else Id, Vd = drain.measure.iv() end
--	else
--	    Id = 1e-100
--            Vd = drain.source.levelv
--        end
	print(Vg, Ig, Vd, Id)
end

function measureVds(Vds)
	drain.source.levelv = Vds

	for _, Vgs_ in ipairs(Vgs) do
	    gate.source.levelv = Vgs_
	    measure()
	end
end

print('## startIDVG')
print('#n Vg Ig Vd Id')
smus_on(true)

measureVds(Vds) 

smus_on(false)
print('## endIDVG')

reset()


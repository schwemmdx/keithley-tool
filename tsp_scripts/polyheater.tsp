reset()
errorqueue.clear()
smulist = {}

function def_smu(s, d, i, irange)
   smu = s
   table.insert(smulist, smu)
   display['smua'].measure.func = display.MEASURE_DCAMPS
   display['smub'].measure.func = display.MEASURE_DCAMPS

   smu.measure.autorangei  = smu.AUTORANGE_ON
   smu.measure.autozero    = smu.AUTOZERO_AUTO
   smu.measure.delay       = smu.DELAY_AUTO
   smu.measure.delayfactor = 1.3
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

--gate   = def_smu(gateSMU,  'gate',   IgateMax,  IgateRange)
--drain  = def_smu(drainSMU, 'drain',  IdrainMax, IdrainRange)

polyPlus   = def_smu(smua,  'polyPlus',   0.5,  0.5)
polyMinus  = def_smu(smub,  'polyMinus',  0.5,  0.5)

function controlPolyheater(t, P)
    ttotal = 0.
    polyMinus.source.levelv = 0.

    Vout = 1.  -- initial value
    Ip   = 0

    polyPlus.source.levelv = Vout
    Ip = polyPlus.measure.i()

    while ttotal < t do
        polyPlus.source.levelv = Vout
        Ip = polyPlus.measure.i()
        
        Pnew = P*(1.+0.3*math.exp(ttotal/(-5.)))

        R = Vout / Ip
        Vout = math.sqrt(Pnew*R)

        print('  ' .. ttotal .. '  ' .. Ip .. '  ' .. Vout .. ' ' .. Ip*Vout .. '  ' .. R)

        ttotal = ttotal + nplcValue/50.
    end

end

print('#n t Ih Vh Ph R')
smus_on(true)

controlPolyheater(tHeat, PHeat) 

smus_on(false)
reset()


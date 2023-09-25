-- CONFIGURATION SECTION

-- idvg for cp01dev01
--Vds = 0.001
--Vbs = 0.000  --sweep(5.0, -5.0, -0.25)
--Vgs = sweep(-20, 20, 5)

-- CONFIGURATION SECTION END

--node[1].reset()
--node[2].reset()
--node[3].reset()

errorqueue.clear()
node[1].errorqueue.clear()
node[2].errorqueue.clear()
node[3].errorqueue.clear()

smulist = {}

-- Init TSP Link
--tspNodesFound = tsplink.initialize(0)
--print("Nodes found = " .. tspNodesFound)


function def_smu(s, d, i, irange)
    if s == nil then
       return nil
    end

    smu = s
    table.insert(smulist, smu)
    node[1].display['smua'].measure.func = display.MEASURE_DCAMPS
    node[1].display['smub'].measure.func = display.MEASURE_DCAMPS
    node[2].display['smua'].measure.func = display.MEASURE_DCAMPS
    node[2].display['smub'].measure.func = display.MEASURE_DCAMPS
    node[3].display['smua'].measure.func = display.MEASURE_DCAMPS
    node[3].display['smub'].measure.func = display.MEASURE_DCAMPS

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

gate   = def_smu(gateSMU,   'gate',   IgateMax,   IgateRange)
drain  = def_smu(drainSMU,  'drain',  IdrainMax,  IdrainRange)
source = def_smu(sourceSMU, 'source', IsourceMax, IsourceRange)
bulk   = def_smu(bulkSMU,   'bulk',   IbulkMax,   IbulkRange)
diodeA = def_smu(diodeASMU, 'diodeA', IdiodeAMax, IdiodeARange)
diodeB = def_smu(diodeBSMU, 'diodeB', IdiodeBMax, IdiodeBRange)

function measure()
	IdiodeA = 0.
	IdiodeB = 0.
	Ig      = 0.
	Is      = 0.
	Ib      = 0.

	if measureIdiodeA > 0 then
	   if diodeA.source.compliance then 
	      IdiodeA = 'compliance' 
              VdA_    = IdiodeA 
	   else 
	      IdiodeA, VdA_ = diodeA.measure.iv() 
	   end
        else
	   VdA_ = diodeA.source.levelv
        end

	if measureIdiodeB > 0 then
	   if diodeB.source.compliance then 
	      IdiodeB = 'compliance' 
              VdB_    = IdiodeB
	   else 
	      IdiodeB, VdB_ = diodeB.measure.iv() 
	   end
        else
	   VdB_ = diodeB.source.levelv
        end

	if measureIG > 0 then
	   if gate.source.compliance then 
	       Ig  = 'compliance' 
	       Vg_ = Ig 
	   else 
	       Ig, Vg_ = gate.measure.iv() 
	   end
        else
	   Vg_ = gate.source.levelv
	end

	if measureIS > 0 then
	   if source.source.compliance then 
	       Is  = 'compliance' 
	       Vs_ = Is 
	   else 
	       Is, Vs_ = source.measure.iv() 
	   end
        else
	   Vs_ = source.source.levelv
	end

	if bulk ~= nil then
           if measureIB > 0 then
              if  bulk.source.compliance then 
      	          Ib = 'compliance' 
      	          Vb_ = Ib 
      	      else 
      	          Ib, Vb_ = bulk.measure.iv() 
      	      end
           else
      	      Vb_ = bulk.source.levelv
      	   end
        else
	   Vb_ = 1e100
	   Ib  = 1e100
	end

	-- measure IDrain
	if drain.source.compliance then 
	    Id = 'compliance' 
            Vd = Id 
        else 
            Id, Vd_ = drain.measure.iv() 
        end

	print(Vg_, Ig, Vd_, Id, Vs_, Is, Vb_, Ib, VdA_, IdiodeA, VdB_, IdiodeB)
end

function setOutputVoltage(smu, V)
   if smu ~= nil then
      smu.source.levelv = V
   end
end

function measureVds(Vds)
	if drain ~= nil then
   	   if type(Vds) == "number" then
   	      drain.source.levelv  = Vds
   	   else
   	      sweeplst = Vds
   	   end
	end

	if source ~= nil then
   	   if type(Vs) == "number" then
	      source.source.levelv = Vs
	   else
	     sweeplst = Vs
	   end
        end

        if bulk ~= nil then
	   if type(VB) == "number" then
	      bulk.source.levelv = VB
	   else
	     sweeplst = VB
	  end
	end

	if gate ~= nil then
   	   if type(Vgs) == "number" then
	      gate.source.levelv = Vgs
	   else
	      sweeplst = Vgs
	   end
	end

	if diodeA ~= nil then
	   if type(VdiodeA) == "number" then
	      diodeA.source.levelv = VdiodeA
           else
	      sweeplst = VdiodeA
	   end
	end

	if diodeB ~= nil then
	   if type(VdiodeB) == "number" then
	      diodeB.source.levelv = VdiodeB
	   else
	      sweeplst = VdiodeB
	   end
	end

	for i, _ in ipairs(sweeplst) do
	    if type(Vds) == "table" and drain ~= nil then
   	       drain.source.levelv  = Vds[i]
	    end
	    if type(Vs) == "table" and source ~= nil then
	       source.source.levelv = Vs[i]
	    end
	    if type(Vgs) == "table" and gate ~= nil then
	       gate.source.levelv = Vgs[i]
	    end
	    if type(VB) == "table" and bulk ~= nil then
	       bulk.source.levelv = VB[i]
	    end
 	    if type(VdiodeA) == "table" and diodeA ~= nil then
	       diodeA.source.levelv = VdiodeA[i]
	    end
	    if type(VdiodeB) == "table" and diodeB ~= nil then
	       diodeB.source.levelv = VdiodeB[i]
	    end

	    measure()
	end
end

print('## startIDVG')
print('#n Vg Ig Vd Id Vs Is VdiodeA IdiodeA VdiodeA IdiodeA')
smus_on(true)

measureVds(Vds) 

smus_on(false)
print('## endIDVG')

reset()


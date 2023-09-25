function sweep(b, e, d)
	local i, l, v = 1, {}, b
	while (v - e) / d <= 0.5 do
		l[i] = v
		i = i + 1
		v = v + d
	end
--	setmetatable(l, { __add=
--		function (s1, s2)
--			for _, x in ipairs(s2) do table.insert(s1, x) end
--			return s1
--		end
--	})
	return l
end

function table_length(t)
    if type(t) == "number" then 
        return 0 
    end

    for i, _ in t do
        if type(i) == "number" then 
            max = i 
        end
    end

    return max
end

function table_join(t1, t2)
  for _,v2 in ipairs(t2) do
    table.insert(t1, v2)
  end
end 

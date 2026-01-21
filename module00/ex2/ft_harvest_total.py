def ft_harvest_total():
	i = 1
	total = 0
	while i <= 3:
		harvest = int(input(f"Day {i} harvest: "))
		total += harvest
		i += 1
	print(f">> Total Harvest : {total}")
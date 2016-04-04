def search(tab):
	print("start: " + str(tab))
	if isinstance( tab[0], int ) is False:
		print("calc tab[0]: " + str(tab[0]))
		tab[0] = search(tab[0])
		return search(tab)
		
	if isinstance( tab[1], int ) is False:
		print("calc tab[1]: " + str(tab[1]))
		tab[1] = search(tab[1])
		return search(tab)
		
	print("max: " + str(max(tab[0], tab[1])))
	return max(tab[0], tab[1])
		
print(search(tab1))

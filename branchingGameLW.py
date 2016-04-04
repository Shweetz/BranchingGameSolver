tab1 = [[[2,3],[1,4]],[[4,5],[0,6]]]

def search(tab, tryToMax):
	for i in range(len(tab)):
		if isinstance( tab[i], int ) is False:
			tab[i] = search(tab[i], not tryToMax)
			return search(tab, tryToMax)
	
	if tryToMax:
		return max(tab)
	else:
		return min(tab)

print(search(tab1, True))

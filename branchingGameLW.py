tab1 = [[[2,3],[1,4]],[[4,5],[6,0]]]

def search(tab, tryToMax):
	for i in range(len(tab)):
		if isinstance( tab[i], int ) is False:
			tab[i] = search(tab[i], not tryToMax)
	
	if tryToMax:
		return max(tab)
	else:
		return min(tab)

print("Score: " + str(search(tab1, True)) + " (if the 1st player wants to maximize)")

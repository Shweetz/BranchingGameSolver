import copy

tab1 = [[[2,3],[1,4]],[[4,5],[0,6]]]
tryToMax1 = True;

tab2 = copy.deepcopy(tab1)
tryToMax2 = False;

def search(tab, tryToMax):
	print("start: " + str(tab) + ", tryToMax: " + str(tryToMax))
	
	for i in range(len(tab)):
		if isinstance( tab[i], int ) is False:
			print("calc tab[" + str(i) + "]: " + str(tab[i]))
			tab[i] = search(tab[i], not tryToMax)
			return search(tab, tryToMax)
	
	if tryToMax:
		print("max: " + str(max(tab)))
		return max(tab)
	else:
		print("min: " + str(min(tab)))
		return min(tab)

print("===== START WITH TRYTOMAX " + str(tryToMax1))
print(search(tab1, tryToMax1))
print("===== START WITH TRYTOMAX " + str(tryToMax2))
print(search(tab2, tryToMax2))

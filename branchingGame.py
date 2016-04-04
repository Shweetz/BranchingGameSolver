import copy

tab1 = [[[2,3],[1,4]],[[4,5],[6,0]]]
tryToMax1 = True;

tab2 = copy.deepcopy(tab1)
tryToMax2 = False;

turn = 1
path = "   "
 
def search(tab, tryToMax, turn, path):
	for i in range(len(tab)):
		if isinstance( tab[i], int ) is False:
			path = path[:turn-1] + str(i+1) + path[turn:]
			print("turn " + str(turn) + ", path: " + str(path) + ", computing " + str(tab[i]))
			tab[i] = search(tab[i], not tryToMax, turn + 1, path)
           
	if tryToMax:
		path = path[:turn-1] + str(tab.index(max(tab)) + 1) + path[turn:]
		print("turn " + str(turn) + ", path: " + path + ", max of " + str(tab) + " is " + str(max(tab)))
		return max(tab)
	else:
		path = path[:turn-1] + str(tab.index(min(tab)) + 1) + path[turn:]
		print("turn " + str(turn) + ", path: " + path + ", min of " + str(tab) + " is " + str(min(tab)))
		return min(tab)
 
print("Game table: " + str(tab1) + "\n")
print("1st player wants to maximize")
print("Score: " + str(search(tab1, tryToMax1, turn, path)) + " (if the 1st player wants to maximize), path: " + path + "\n")
print("1st player wants to minimize")
print("Score: " + str(search(tab2, tryToMax2, turn, path)) + " (if the 1st player wants to minimize), path: " + path)

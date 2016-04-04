# BranchingGameSolver
Recursive python function to do graph search and try all branches of a game.

Branching game: 2 players alternatively choose a branch to explore. At the end of branches, there is a number. One player wants to maximize this number, the other wants to minimize it.

Example:

             start
            /     \
           /       \
          /         \
         /           \
        /\           /\
       /  \         /  \
      /    \       /    \
     /\    /\     /\    /\
    /  \  /  \   /  \  /  \
    2  3  1  4   4  5  0  6

    Player 1 (maximize) goes right
    Player 2 (minimize) goes left
    Player 1 goes right: score is 5

# Files:
### findMax.py
Find maximum in nested tables

### branchingGame.py
Solves branching game assuming both players play optimally.

### branchingGameLW.py
LightWeight (LW) version of branchingGame.py

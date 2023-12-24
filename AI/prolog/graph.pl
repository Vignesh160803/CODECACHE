connected(one,two).

connected(two,three).
connected(two,six).
connected(two,eight).

connected(three,seven).
connected(three,six).
connected(three,four).

connected(four,six).

connected(six,five).


path(X,Y):- connected(X,Y).
path(X,Y):- connected(X,Z),path(Z,Y),X\=Y.
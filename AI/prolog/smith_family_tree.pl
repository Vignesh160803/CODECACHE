male(harry).
male(john).
male(james).
male(peter).
male(luke).
male(owen).
male(joel).

female(ann).
female(laura).
female(jane).
female(kate).
female(isabel).

parent(john,harry).
parent(john,ann).
parent(laura,harry).
parent(laura,ann).


parent(jane,laura).
parent(owen,laura).
parent(james,john).
parent(peter,john).

parent(kate,jane).
parent(joel,jane).
parent(isabel,jane).


parent(luke,peter).


father(X,Y):- parent(X,Y),male(Y).
mother(X,Y):- parent(X,Y),female(Y).
grandparent(X,Y):- parent(X,Z),parent(Z,Y).
grandmother(X,Y):- grandparent(X,Y),female(Y).
grandfather(X,Y):- grandparent(X,Y),male(Y).
% Define the predicate to return the first element of a list
first([], []).
first([H|_], H).

% Define the predicate to return the last element of a list
last([], []).
last([X], X).
last([_|T], R) :- last(T, R).

% Define the predicate to compute the sum of a list
sum([], 0).
sum([H|T], R) :- sum(T, R2), R is H + R2.

% Define the predicate to compute the sum of a list (Tail recursive)
sum2([], Acc, Acc).
sum2([H|T], Acc, L2) :- NewAcc is Acc + H, sum2(T, NewAcc, L2).

% Define the predicate to add 1 to each member of the list
add1([], []).
add1([H|T], [H2|T2]) :- H2 is H + 1, add1(T, T2).

% Define the predicate to add N to each member of the list
addN([], _, []).
addN([H|T], N, [H2|T2]) :- H2 is H + N, addN(T, N, T2).

% Define the predicate to check if an element is a member of a list
my_member(X, [X|_]).
my_member(X, [_|T]) :- my_member(X, T).

% Define the predicate to duplicate each element of a list (Tail recursive)
dup([], []).
dup([H|T], [H, H|T2]) :- dup(T, T2).

% Define the predicate to compute the length of a list (Tail recursive)
my_length([], 0).
my_length([_|T], R) :- my_length(T, R2), R is R2 + 1.

% Define the predicate to reverse a list (Tail recursive)
my_reverse(L, R) :- rev_helper(L, [], R).

rev_helper([], A, A).
rev_helper([H|T], A, R) :- rev_helper(T, [H|A], R).

% Define the predicate to merge two sorted lists into one sorted list
merge(Xs, [], Xs).
merge([], Ys, Ys).
merge([X|Xs], [Y|Ys], [X|Zs]) :- X < Y, merge(Xs, [Y|Ys], Zs).
merge([X|Xs], [Y|Ys], [X, Y|Zs]) :- X = Y, merge(Xs, Ys, Zs).
merge([X|Xs], [Y|Ys], [Y|Zs]) :- X > Y, merge([X|Xs], Ys, Zs).

% Define the predicate for merge sort
mergesort([], []).
mergesort([X], [X]).
mergesort(List, Sorted) :-
    List = [_, _|_],
    divide(List, L1, L2),
    mergesort(L1, Sorted1),
    mergesort(L2, Sorted2),
    merge(Sorted1, Sorted2, Sorted).

% Helper predicate to divide a list into two halves
divide([], [], []).
divide([X], [X], []).
divide([X1, X2|Xs], [X1|L1], [X2|L2]) :-
    divide(Xs, L1, L2).

% Bogosort Algorithm
is_sorted([]).
is_sorted([_]).
is_sorted([X, Y | T]) :-
    X =< Y,
    is_sorted([Y | T]).

remove(X, [X | T], T).
remove(X, [H | T], [H | R]) :-
    remove(X, T, R).

permutation([], []).
permutation(L, [H | T]) :-
    remove(H, L, R),
    permutation(R, T).

bogosort(X, Y) :-
    permutation(X, Y),
    is_sorted(Y).
	
% Palindrome Checker
palindrome(X) :-
    reverse(X, X).

% Sublist Finder
suffix(S, L) :- append(_, S, L).
prefix(P, L) :- append(P, _, L).
sublist(SubL, L) :-
    suffix(Suffix, L),
    prefix(SubL, Suffix).

% Queries with examples for each predicate:

% ?- first([1,2,3], FirstElement).
% ?- last([1,2,3], LastElement).
% ?- sum([1,2,3], Sum).
% ?- sum2([1,2,3], 0, Sum).
% ?- add1([1,2,3], NewList).
% ?- addN([1,2,3], 5, NewList).
% ?- my_member(2, [1,2,3]).
% ?- dup([1,2,3], DupList).
% ?- my_length([1,2,3], Length).
% ?- my_reverse([1,2,3], ReversedList).
% ?- merge([1,3,5], [2,4,6], MergedList).
% ?- mergesort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], SortedList).
% ?- bogosort([4, 3, 2, 1], Sorted).
% ?- palindrome([r, a, c, e, c, a, r]).
% ?- sublist([2, 3], [1, 2, 3, 4]).
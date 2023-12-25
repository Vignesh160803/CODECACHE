% Check if a list is empty
is_empty([]).

% Check if an element is a member of a list
is_member(X, [X|_]).
is_member(X, [_|T]) :- is_member(X, T).

% Concatenate two lists
concatenate([], L, L).
concatenate([H|T], L, [H|Result]) :- concatenate(T, L, Result).

% Reverse a list
reverse_list([], []).
reverse_list([H|T], Result) :- reverse_list(T, Reversed), concatenate(Reversed, [H], Result).

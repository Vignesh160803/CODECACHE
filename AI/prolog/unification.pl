% Unification example
unify(X, X).

% Check if variable occurs in term
occurs_in(X, X) :- var(X).
occurs_in(X, T) :- compound(T), functor(T, _, N), occurs_in_args(X, T, N).

occurs_in_args(X, T, N) :- N > 0, arg(N, T, Arg), occurs_in(X, Arg).
occurs_in_args(X, T, N) :- N > 0, N1 is N - 1, occurs_in_args(X, T, N1).

% unify(a, a).
% occurs_in(X, f(X, g(Y))).
% occurs_in_args(X, f(X, g(Y)), 2).

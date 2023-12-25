:- use_module(library(clpfd)).

solve_cryptarithmetic_problem([N,I,N,E] + [F,I,N,E] = [W,I,V,E,S]) :-
    Vars = [N,I,E,F,W,V,S],
    Vars ins 0..9,
    all_different(Vars),
    N #\= 0,
    E #\= 0,
    W #\= 0,
    
    1000*N + 100*I + 10*N + E +
    1000*F + 100*I + 10*N + E #=
    
    10000*W + 1000*I + 100*V + 10*E + S,
    
    label(Vars).

% Example query
% solve_cryptarithmetic_problem([N,I,N,E] + [F,I,N,E] = [W,I,V,E,S]).
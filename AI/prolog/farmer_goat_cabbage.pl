% Define the valid states
valid_state(state(Farmer, Wolf, Goat, Cabbage)) :-
    Farmer = left, (Goat = left ; Cabbage = left), (Goat = left ; Wolf = left);
    Farmer = right, (Goat = right ; Cabbage = right), (Goat = right ; Wolf = right).

% Define the move actions
move(state(left, left, Goat, Cabbage), state(right, right, Goat, Cabbage)).
move(state(left, Wolf, left, Cabbage), state(right, Wolf, right, Cabbage)).
move(state(left, Wolf, Goat, left), state(right, Wolf, Goat, right)).
move(state(left, Wolf, Goat, Cabbage), state(right, Wolf, Goat, Cabbage)).

move(state(right, right, Goat, Cabbage), state(left, left, Goat, Cabbage)).
move(state(right, Wolf, right, Cabbage), state(left, Wolf, left, Cabbage)).
move(state(right, Wolf, Goat, right), state(left, Wolf, Goat, left)).
move(state(right, Wolf, Goat, Cabbage), state(left, Wolf, Goat, Cabbage)).

% Define the goal state
goal_state(state(right, right, right, right)).

% Define the path predicate
path(State, State, _, []).
path(State1, State3, Visited, [Move|Path]) :-
    move(State1, State2),
    valid_state(State2),
    \+ member(State2, Visited), % Check if State2 has already been visited
    path(State2, State3, [State2|Visited], Path),
    Move = State1-State2.

% Find a solution
solve(Path) :-
    path(state(left, left, left, left), state(right, right, right, right), [state(left, left, left, left)], Path).

%   ?- solve(Path).
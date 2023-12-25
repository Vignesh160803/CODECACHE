% Define the possible colors
color(red).
color(blue).
color(green).
color(yellow). % Added another color for more options

% Define the adjacency relationships between regions in the graph
adjacent(a, b). adjacent(a, d). adjacent(a, e).
adjacent(b, c). adjacent(b, d). adjacent(b, e).
adjacent(c, d). adjacent(c, e). adjacent(c, f).
adjacent(d, e).
adjacent(e, f). adjacent(e, g). adjacent(e, h).
adjacent(f, g). adjacent(f, h).
adjacent(g, h).

% Rule to color the map with 8 regions
color_map(A, B, C, D, E, F, G, H) :-
    color(A), color(B), color(C), color(D), color(E), color(F), color(G), color(H),
    different(A, B), different(A, D), different(A, E),
    different(B, C), different(B, D), different(B, E),
    different(C, D), different(C, E), different(C, F),
    different(D, E),
    different(E, F), different(E, G), different(E, H),
    different(F, G), different(F, H),
    different(G, H).

% Ensure that two regions do not have the same color
different(X, Y) :- \+ X = Y.

% Query to find a valid coloring
?- color_map(A, B, C, D, E, F, G, H).

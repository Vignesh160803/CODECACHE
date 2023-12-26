edge(a, c).
edge(a, b).
edge(c, d).
edge(b, e).
edge(e, g).

% DFS traversal
dfs(Node) :-
    dfs(Node, []).

dfs(Node, Visited) :-
    \+ member(Node, Visited),
    write(Node), write(' '),
    findall(Neighbor, (edge(Node, Neighbor), \+ member(Neighbor, Visited)), Neighbors),
    member(NextNode, Neighbors),
    dfs(NextNode, [Node | Visited]).

% Start the DFS traversal from a specific node
start_dfs :- dfs(a).
% PACE 2019
% 1a. Vertex Cover Exact (Compute a vertex cover of smallest size)

% Vertices in graph
array[int] of int: vertex;

% Edges between vertices
array[int, int] of int: edges;

int: num_edges = (length(edges) div 2);

% Array of chosen vertices
array[1..length(vertex)] of var 0..1: span;

% An edge is connected if one of its' endpoints is in our chosen vertices          
constraint forall(i in 1..num_edges)
            (true == ((span[edges[i,1]] == 1) \/ (span[edges[i,2]] == 1)));
                         
% Minimize the number of vertices in span (SINGLE SOlUTION)
solve minimize sum(span);

% Multiple solutions, set <OPT_CARD_SIZE> to the minimal
% card size found by the solver above.
%constraint card(span) = <OPT_CARD_SIZE>;
%solve satisfy;

output[show(span),show(sum(span))];
# ezContactGraphRouting
A contact graph routing algorithm using minimum priority queue and Dijkstra.

## Project Description
In a network with mobile nodes, the vertices of a graph keep moving. Links are established or
abolished over time. A full path from a source node S to a destination node D may never exist,
but it may still be possible to go from S to D in multiple “hops” with possible delay after each
hop (i.e. go to an intermediate node, wait until a new link is established, go to another
intermediate node,... and so on). Classical graph representation of such a network cannot be
used to find best paths, since such a graph keeps changing continuously.

Such a time-varying graph can be represented by a “contact graph” 𝐺 = (𝐶, 𝐸).

The goal of this project is to implement the Dijkstra algorithm on contact graphs.
Dijkstra tries to find a valid path in the contact graph minimizing the “arrival time” as
its metric (which corresponds to the “path cost” in regular Dijkstra).

The input for the project is a contact graph represented in file “ContactList.txt”. The graph in
the file contains 190 contacts (with IDs 1 through 190) among 12 network nodes (numbered 1
through 12). Each line in the text file specifies the id, start time, end time, sender, receiver, and
owlt attributes of a contact.

The program is capable of performing the following tasks:
 - Read the contact graph info from the file.
 - Implement a minimum priority queue using a heap, which will be used in Dijkstra.
 - Implement Dijkstra using the minimum priority queue instead of the linear search in the CSP function.
 - Use the algorithm to find an optimal path from node #8 to node #5.
 - Print the contact ids corresponding to the optimal path and the resulting best arrival
   time.
## MVAY - Final project - A stochastic route planner for the Zürich area.

### Introduction
In this final project we will build our own robust public transport route planner to improve on the problematic of route planning with travel time uncertainty.

We are supposed to reuse the SBB dataset. The route planner can build on a set of simplifying assumptions and has to meet the constraints of shortest travel time, user-defined certainty level and latest initial route departure time.

Our approach for this  is well documented in `main_final`.
### Project Structure
We chose to split our project (`notebooks`) into 3 parts:

-`main_final`: this file represents the report-like implementation of the project, with all its parts: timetable creation, graph construction and routing algorithm with predictive modeling. All comments and descriptions are included.

-`modules`: this file folder includes important modules of our project, like the graph construction or data filtering. 

-`helper functions`: for the sake of reproducible data science, we have saved some useful functions, for example the modified Djikstra, into this .py file folder. Feel free to use them in other projects too! 

### Video Link of our pitch

Youtube: https://www.youtube.com/watch?v=od6SdbsdZ6Y


### References
[1] Peng Ni ; Hoang Tam Vo ; Daniel Dahlmeier ; Wentong Cai ; Jordan Ivanchev ; Heiko Aydt,
DEPART: Dynamic Route Planning in Stochastic Time-Dependent Public Transit Networks, https://ieeexplore.ieee.org/document/7313363

[2]Jin Y. Yen: Finding the K Shortest Loopless Paths in a Network,
https://www.semanticscholar.org/paper/Finding-the-K-Shortest-Loopless-Paths-in-a-Network-Yen-YENt/aa6a64afc25f48ad44e510d0055405836c8cc325    

[3] Yen algorithm in Python: https://github.com/handloomweaver/YenKSP/blob/master/algorithms.py

[4]Adi Botea, Evdokia Nikolova, Michele Berlingerio, "Multi-Modal Journey Planning in the Presence of Uncertainty". 
ICAPS 2013.

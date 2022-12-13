# Introduction
In computational complexity theory, the maximum satisfiability problem (MAX-SAT) is the problem of determining the maximum number of clauses, of a given Boolean formula in conjunctive normal form, that can be made true by an assignment of truth values to the variables of the formula. It is a generalization of the Boolean satisfiability problem, which asks whether there exists a truth assignment that makes all clauses true.
[More about MAX-SAT](https://en.wikipedia.org/wiki/Maximum_satisfiability_problem)
<br>
# Features
I solve this problem in <b>three methods</b>:
### 1- Stochastic hill-climbing search
Stochastic hill climbing is a variant of the basic hill climbing method. While basic hill climbing always chooses the steepest uphill move, "stochastic hill climbing chooses at random from among the uphill moves; the probability of selection can vary with the steepness of the uphill move.".
[More about Stochastic hill-climbing](https://en.wikipedia.org/wiki/Stochastic_hill_climbing)
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Max-SAT-solver$ python3 stochastic_hill_climbing_search.py                                       
Final solution found with fitness = 80
values: 
X0=True X1=True X2=True X3=True X4=True X5=True X6=False X7=False X8=True X9=True X10=False X11=False X12=False X13=True X14=False X15=True X16=False X17=False X18=True X19=False
```
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Max-SAT-solver$ python3 stochastic_hill_climbing_search.py                                        
Final solution found with fitness = 78
values: 
X0=False X1=True X2=False X3=False X4=True X5=True X6=True X7=False X8=True X9=True X10=False X11=False X12=True X13=True X14=False X15=True X16=True X17=True X18=False X19=True 
```
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Max-SAT-solver$ python3 stochastic_hill_climbing_search.py                                        
Final solution found with fitness = 79
values: 
X0=True X1=False X2=True X3=True X4=False X5=True X6=True X7=True X8=True X9=False X10=True X11=True X12=True X13=False X14=False X15=False X16=False X17=True X18=True X19=False 
```


### 2- Tabu search
Tabu search is a metaheuristic search method employing local search methods used for mathematical optimization. 
The implementation of tabu search uses memory structures that describe the visited solutions or user-provided sets of rules. If a potential solution has been previously visited within a certain short-term period or if it has violated a rule, it is marked as "tabu" (forbidden) so that the algorithm does not consider that possibility repeatedly. 
[More about Tabu search](https://en.wikipedia.org/wiki/Tabu_search)
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Max-SAT-solver$ python3 tabu_search.py                                                              
final solution found with fitness = 79
values: 
X0=False X1=True X2=True X3=True X4=True X5=True X6=True X7=False X8=True X9=True X10=False X11=False X12=True X13=True X14=False X15=False X16=True X17=True X18=False X19=False 
```
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Max-SAT-solver$ python3 tabu_search.py                                                            
final solution found with fitness = 79
values: 
X0=False X1=True X2=True X3=True X4=True X5=False X6=False X7=False X8=True X9=True X10=False X11=False X12=False X13=True X14=True X15=True X16=True X17=False X18=False X19=False 
```
```
yasin@Hunter ~/Documents/Code/iut/ai/github/MAX-SAT-solver$ python3 tabu_search.py                                                               
final solution found with fitness = 80
values: 
X0=False X1=True X2=False X3=True X4=True X5=True X6=False X7=False X8=True X9=True X10=False X11=False X12=False X13=True X14=True X15=True X16=False X17=False X18=True X19=False 

```
### 3- Simulated annealing
Simulated annealing (SA) is a probabilistic technique for approximating the global optimum of a given function. Specifically, it is a metaheuristic to approximate global optimization in a large search space for an optimization problem. It is often used when the search space is discrete (for example the traveling salesman problem, the boolean satisfiability problem, protein structure prediction, and job-shop scheduling). For problems where finding an approximate global optimum is more important than finding a precise local optimum in a fixed amount of time, simulated annealing may be preferable to exact algorithms such as gradient descent or branch and bound. 
The name of the algorithm comes from annealing in metallurgy, a technique involving the heating and controlled cooling of a material to alter its physical properties. 
This notion of slow cooling implemented in the simulated annealing algorithm is interpreted as a slow decrease in the probability of accepting worse solutions as the solution space is explored. Accepting worse solutions allows for a more extensive search for the global optimal solution. In general, simulated annealing algorithms work as follows. The temperature progressively decreases from an initial positive value to zero. At each time step, the algorithm randomly selects a solution close to the current one, measures its quality, and moves to it according to the temperature-dependent probabilities of selecting better or worse solutions, which during the search respectively remain at 1 (or positive) and decrease toward zero.
[More about Simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Max-SAT-solver$ python3 simulated_annealing.py                                                    
final solution found with fitness = 80
values: 
X0=True X1=True X2=False X3=True X4=True X5=True X6=False X7=False X8=True X9=True X10=False X11=False X12=False X13=True X14=False X15=True X16=False X17=False X18=True X19=False 
```
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Max-SAT-solver$ python3 simulated_annealing.py                                                     
final solution found with fitness = 80
values: 
X0=True X1=True X2=True X3=True X4=True X5=True X6=False X7=False X8=True X9=True X10=False X11=False X12=False X13=True X14=False X15=True X16=False X17=False X18=True X19=False 
```
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Max-SAT-solver$ python3 simulated_annealing.py                                                     
final solution found with fitness = 80
values: 
X0=True X1=True X2=True X3=True X4=True X5=True X6=False X7=False X8=True X9=True X10=False X11=False X12=False X13=True X14=False X15=True X16=False X17=False X18=True X19=False 

```
<br>
I also have an input.txt that is an example of MAX-SAT with 80 clauses and 20 variables and run my algorithms on this sample.

import random
import copy

def fitness(candida,variables):
    fit = 0
    for var in variables:
        for index in var:
            if (index<0 and candida[-index-1]==0)or(index>0 and candida[index-1]==1):
                fit += 1
                break
    return fit

with open('/home/yasin/Documents/Code/iut/ai/Max-SAT/input.txt') as fd:
    data = fd.readlines()
    variable_num,clause_num = map(int,data[0].split())
    vars = [[]]*clause_num
    for index in range(clause_num):
        vars[index] = list(map(int,data[index+1].split()))[:-1]

candidate = random.choices([True,False],k=variable_num)

while(1):
    current_fitness = fitness(candidate,vars)
    neighbors_fitness = []
    for i in range(variable_num):
        temp = copy.deepcopy(candidate)
        temp[i] = not temp[i]
        temp = fitness(temp,vars)
        neighbors_fitness.append(temp)
    good_neighbors = [
        index for index,value in enumerate(neighbors_fitness)
        if value>current_fitness
    ]
    if len(good_neighbors) == 0:
        print(f'Final solution found with fitness = {current_fitness}\nvalues: ')
        for iterator in range(variable_num):
            print(f'X{iterator}={candidate[iterator]}',end=' ')
        print('')
        break
    weights = [
        value for index,value in enumerate(neighbors_fitness)
        if value>current_fitness
    ]
    choosen = random.choices(good_neighbors,weights,k=1)
    choosen = choosen[0]
    candidate[choosen] = not candidate[choosen]

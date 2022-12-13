import random
import copy

TABU_TENUR = 5
ITERATION_COUNT = 1000

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
tabu_table = [0]*variable_num
iter = 1
while(1):
    current_fitness = fitness(candidate,vars)
    max_index = -1
    max_fit = -1
    if iter < ITERATION_COUNT:
        for i in range(variable_num):
            if tabu_table[i] == 0:
                temp = copy.deepcopy(candidate)
                temp[i] = not temp[i]
                temp = fitness(temp,vars)
                if temp > max_fit:
                    max_fit = temp
                    max_index = i
    else:
        for i in range(variable_num):
            temp = copy.deepcopy(candidate)
            temp[i] = not temp[i]
            temp = fitness(temp,vars)
            if temp > max_fit:
                max_fit = temp
                max_index = i
                candidate[max_index] = not candidate[max_index]
        print(f'final solution found with fitness = {current_fitness}\nvalues: ')
        for iterator in range(variable_num):
            print(f'X{iterator}={candidate[iterator]}',end=' ')
        print('')
        break

    candidate[max_index] = not candidate[max_index]
    for i in range(variable_num):
        if tabu_table[i] != 0 : tabu_table[i] -= 1
    tabu_table[max_index] = TABU_TENUR
    iter += 1
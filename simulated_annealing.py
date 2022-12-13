import random
import numpy as np
import math

INITIAL_TEMPRATURE = 1000

def set_temprature(temp):
    temp *= 0.999
    return temp

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
temprature = INITIAL_TEMPRATURE
i = 0
while(1):
    if temprature <= 0.1:
        print(f'final solution found with fitness = {current_fitness}\nvalues: ')
        for iterator in range(variable_num):
            print(f'X{iterator}={candidate[iterator]}',end=' ')
        print('')
        break
    current_fitness = fitness(candidate,vars)
    neighbor = candidate.copy()
    neighbor[i%variable_num] = not neighbor[i%variable_num]
    neighborFit = fitness(neighbor,vars)
    if neighborFit > current_fitness:
        candidate = neighbor
    elif np.random.rand() < math.exp((neighborFit-current_fitness)/temprature):
            candidate = neighbor
    i += 1
    temprature = set_temprature(temprature)
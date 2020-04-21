#import pandas as pd
#from pulp import *

import pulp
from decimal import getcontext, Decimal
import numpy as np
from random import seed
from random import randint
from random import gauss
import json

getcontext().prec = 3
cases = 17615
#ventilator = 10000
ventilators = 0
used = .14 * cases - .05 * cases
while (int(ventilators) < used):
    ventilators = input ("Enter number of ventilators: ")
    if (int(ventilators) < used):
        print ("Please enter a number greater than " + str(round(used)) + " for the number of ventilators")

#ventilators = "10000"
ventilator = int(ventilators)


ventilator = ventilator - used

import requests

url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"

querystring = {"country":"India"}

headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "1785afdd39msh2137b157fb3ce6bp1b8682jsna9019ab09790"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

newcases = data['latest_stat_by_country'][0]['active_cases']

cases = int(newcases.replace(',',''))

print ("Given that 14% of cases are severe and 5% of cases are critical, we will allocate ventilators to those patients first. This takes away a total of " + str(round(used)) + " ventilators")

print ("There are " + str(cases) + " cases and only " + str(int(ventilator)) + " ventilators")

# directory the data is saved
in_dir = '/Users/Vineet/Documents/Linear/covid19-ventilators'


age_groups = [0,10,20,30,40,50,60,70,80]
percents = [.0364, .0806, .2040, .2366, .1669, .1439, .0959, .0301, 0.004, 0.001]
num_aff = [0,0,0,0,0,0,0,0,0,0]
life = [0,0,0,0,0,0,0,0,0,0]
survWvent = [.77, .73, .67, .63, .58, .23, .21, .16, .16]
survWO = [.4, .35, .35, .3, .25, .12, .15, .08, .08]
arrrate = [.01, .06, .08, .12, .16, .2, .25, .06, .06]
num_cases = [0,0,0,0,0,0,0,0,0,0]
years = np.array([0,0,0,0,0,0,0,0,0])
ventilator_usage = [0,0,0,0,0,0,0,0,0]

x = 0
# Number Cases per Age Bracket
for i in percents:
    num_cases[x] = cases * i
    num_cases[x] = round(num_cases[x])
    x = x + 1


# Life Expenctancies per Age Bracket
x = 0
for i in age_groups:
    expectancy = 68.7 - i - 5.5;
    if expectancy >= 0:
        life[x] = expectancy
        life[x] = round(life[x],1)
    x = x + 1

# print patients in each age bracket
print ("Patients in each age group")
print ("O - 10 years: " + str(round(num_cases[0])) + " patients")
print ("11 - 20 years: " + str(round(num_cases[1])) + " patients")
print ("21 - 30 years: " + str(round(num_cases[2])) + " patients")
print ("31 - 40 years: " + str(round(num_cases[3])) + " patients")
print ("41 - 50 years: " + str(round(num_cases[4])) + " patients")
print ("51 - 60 years: " + str(round(num_cases[5])) + " patients")
print ("61 - 70 years: " + str(round(num_cases[6])) + " patients")
print ("71 - 80 years: " + str(round(num_cases[7])) + " patients")
print ("81 - 90 years: " + str(round(num_cases[8])) + " patients")

x = 0

seed(1)
for _ in range(int(ventilator)):
    value = gauss(35, 17)
    x = x + 1
   
        
    if value < 10:
        ventilator_usage[0] = ventilator_usage[0] + 1
    elif (value < 20):
        ventilator_usage[1] = ventilator_usage[1] + 1
    elif (value < 30):
        ventilator_usage[2] = ventilator_usage[2] + 1
    elif (value < 40):
        ventilator_usage[3] = ventilator_usage[3] + 1
    elif (value < 50):
        ventilator_usage[4] = ventilator_usage[4] + 1
    elif (value < 60):
        ventilator_usage[5] = ventilator_usage[5] + 1
    elif (value < 70):
        ventilator_usage[6] = ventilator_usage[6] + 1
    elif (value < 80):
        ventilator_usage[7] = ventilator_usage[7] + 1
    else:
        ventilator_usage[8] = ventilator_usage[8] + 1
        
print ("Ventilator usage in each age group")
print ("O - 10 years: " + str(round(ventilator_usage[0])) + " patients")
print ("11 - 20 years: " + str(round(ventilator_usage[1])) + " patients")
print ("21 - 30 years: " + str(round(ventilator_usage[2])) + " patients")
print ("31 - 40 years: " + str(round(ventilator_usage[3])) + " patients")
print ("41 - 50 years: " + str(round(ventilator_usage[4])) + " patients")
print ("51 - 60 years: " + str(round(ventilator_usage[5])) + " patients")
print ("61 - 70 years: " + str(round(ventilator_usage[6])) + " patients")
print ("71 - 80 years: " + str(round(ventilator_usage[7])) + " patients")
print ("81 - 90 years: " + str(round(ventilator_usage[8])) + " patients")

totalyears = survWvent[0] * round(life[0],1) * ventilator_usage[0] + survWO[0]*round(life[0],1)*(num_cases[0]-ventilator_usage[0]) + survWvent[1]*round(life[1],1) * ventilator_usage[1] + survWO[1]*round(life[1],1)*(num_cases[1]-ventilator_usage[1]) + survWvent[2]*round(life[2],1) * ventilator_usage[2] + survWO[2]*round(life[2],1)*(num_cases[2]-ventilator_usage[2]) + survWvent[3]*round(life[3],1) * ventilator_usage[3] + survWO[3]*round(life[3],1)*(num_cases[3]-ventilator_usage[3]) + survWvent[4]*round(life[4],1) * ventilator_usage[4] + survWO[4]*round(life[4],1)*(num_cases[4]-ventilator_usage[4]) + survWvent[5]*round(life[5],1) * ventilator_usage[5] + survWO[5]*round(life[5],1)*(num_cases[5]-ventilator_usage[5]) + survWvent[6]*round(life[6],1) * ventilator_usage[6] + survWO[6]*round(life[6],1)*(num_cases[6]-ventilator_usage[6]) + .16 * ventilator_usage[7] + .08*(num_cases[7]-ventilator_usage[7])  + .16 * ventilator_usage[8] + .08*(num_cases[8]-ventilator_usage[8])     
print ("Current life years expected upon random selection of patients using a normal distribution to emulate 'first come first serve' policy: " + str(round(totalyears)))




model = pulp.LpProblem("Life year maximizing problem", pulp.LpMaximize)

# Variables

A = pulp.LpVariable('0-10', lowBound=0, cat='Integer')
B = pulp.LpVariable('11-20', lowBound=0, cat='Integer')
C = pulp.LpVariable('21-30', lowBound=0, cat='Integer')
D = pulp.LpVariable('31-40', lowBound=0, cat='Integer')
E = pulp.LpVariable('41-50', lowBound=0, cat='Integer')
F = pulp.LpVariable('51-60', lowBound=0, cat='Integer')
G = pulp.LpVariable('61-70', lowBound=0, cat='Integer')
H = pulp.LpVariable('71-80', lowBound=0, cat='Integer')
I = pulp.LpVariable('81-90', lowBound=0, cat='Integer')

# Constraints

model += survWvent[0] * life[0]* A + survWO[0]*life[0]*(num_cases[0]-A) \
    + survWvent[1] * life[1] * B + survWO[1]*life[1]*(num_cases[1]-B) \
    + survWvent[2] * life[2] * C + survWO[2]*life[2]*(num_cases[2]-C) \
    + survWvent[3] * life[3] * D + survWO[3]*life[3]*(num_cases[3]-D) \
    + survWvent[4] * life[4] * E + survWO[4]*life[4]*(num_cases[4]-E) \
    + survWvent[5] * life[5] * F + survWO[5]*life[5]*(num_cases[5]-F) \
    + survWvent[6] * life[6] * G + survWO[6]*life[6]*(num_cases[6]-G) \
    + survWvent[7] * life[7] * H + survWO[7]*life[7]*(num_cases[7]-H) \
    + survWvent[8] * life[8] * I + survWO[8]*life[8]*(num_cases[8]-I) 

model += A <= num_cases[0] 
model += B <= num_cases[1] 
model += C <= num_cases[2] 
model += D <= num_cases[3] 
model += E <= num_cases[4] 
model += F <= num_cases[5]
model += G <= num_cases[6]
model += H <= num_cases[7]
model += I <= num_cases[8]
model += A + B + C + D + E + F + G + H + I <= ventilator

model.solve()
print (pulp.LpStatus[model.status])

# Print our decision variable values
print ("Ventilator usage in each age group")
print ("O - 10 years: " + str(A.varValue) + " patients")
print ("11 - 20 years: " + str(B.varValue) + " patients")
print ("21 - 30 years: " + str(C.varValue) + " patients")
print ("31 - 40 years: " + str(D.varValue) + " patients")
print ("41 - 50 years: " + str(E.varValue) + " patients")
print ("51 - 60 years: " + str(F.varValue) + " patients")
print ("61 - 70 years: " + str(G.varValue) + " patients")
print ("71 - 80 years: " + str(H.varValue) + " patients")
print ("81 - 90 years: " + str(I.varValue) + " patients")





# Print our objective function value


print ("Total life years through optimization of ventilator usage: " + str(round(pulp.value(model.objective))))


difference = int(round(pulp.value(model.objective))) - totalyears
print ("By optimizing ventilator usage, we were able to increase expected life years by " + str(round(difference)))




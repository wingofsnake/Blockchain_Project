import random
import os
import time
import sys

def Set_List(Hash_list, Crypto_Wealth_list, Parameters):
    """Initialize Hash and Wealth lists with input parameters"""
    if Parameters['StaticOrNot'] == 0 :
        for i in range(Parameters['NodeSize']) :
            Hash_list += [RandomDisGen(Parameters)]
            Crypto_Wealth_list += [0]
    elif Parameters['StaticOrNot'] == 1 :
        Hash_list += [RandomDisGen(Parameters)]
        Crypto_Wealth_list += [0]
    else :
        Print("Static or Not parameters should be 0 or 1")

def Mining(Hash_list, Crypto_Wealth_list, Parameters):
    """Decide which node will success mining, and get reward"""
    total = 0
    for i in range(Parameters['NodeSize']) :
        total += Hash_list[i]

    Success_Possibility = random.uniform(0, total)
    Success_Indicator = 0
    for i in range(Parameters['NodeSize']) :
        Success_Indicator += Hash_list[i]
        if Success_Indicator >= Success_Possibility:
            Crypto_Wealth_list[i] += 1
            break

def Investment(Hash_list, Crypto_Wealth_list, Parameters):
    """Decide new node enter the system"""
    if Parameters['StaticOrNot'] == 0 :
        for i in range(Parameters['NodeSize']) :
            if Hash_list[i] == 0 :
                Hash_list[i] += RandomDisGen(Parameters)
                break
    elif Parameters['StaticOrNot'] == 1 :
        if len(Hash_list) < Parameters[NodeSize] :
            Hash_list += [RandomDisGen(Parameters)]
            Crypto_Wealth_list += [0]

def Reinvestment(Hash_list, Crypto_Wealth_list, Parameters):
    """Decide each node reinvest to their hash power and make distribution of wealth"""
    if len(Hash_list) > 1 :
        cost_list = list()
        reinvestment_ratio_list = [0.0001, 0.001, 0.00125, 0.0025, 0.005, 0.0075,]
            0.00875, 0.01, 0.0125, 0.025, 0.05, 0.075, 0.0875, 0.1, 0.5]

        maximum_wealth = 0
        for i in len(Hash_list) :
            if maximum_wealth < Crypto_Wealth_list[i]
                maximum_wealth = Crypto_Wealth_list[i]

        reinvestment_chance = 0
        for i in len(Hash_list) :
            reinvestment_chance = random.uniform(0,1)
            if reinvestment_chance <= (Crypto_Wealth_list[i] / maximum_wealth) :
                Hash_list[i] += reinvestment_ratio_list[Parameters['ReinvestmentParameter']] * Crypto_Wealth_list[i]
                cost_list += [reinvestment_ratio_list[Parameters['ReinvestmentParameter']] * Crypto_Wealth_list[i]]
                Crypto_Wealth_list[i] -= reinvestment_ratio_list[Parameters['ReinvestmentParameter']] * Crypto_Wealth_list[i]
            else :
                cost_list += [0]
        
        
        temp = 0
        multi = 1.0 / (len(Hash_list) - 1)
        for i in len(Hash_list) :
            temp += cost_list[i]

        for i in len(Hash_list) :
            cost_list[i] = (temp - cost_list[i]) * multi
            Crypto_Wealth_list[i] += cost_list[i]


def FilePrint(Hash_list, Crypto_Wealth_list, Parameters):
    pass

def RandomDisGen(Parameters):
    """Create random number to make specific types of distribution"""
    Uniform_Parameters = [1, 5, 10]
    Exponential_Parameters = [0.1, 1, 5]
    Power_Parameters = [2, 2.5, 3]

    if Parameters['DistributionFormat'] == 0 :
        return random.uniform(0, Uniform_Parameters[Parameters['InitialParameter']])
    elif Parameters['DistributionFormat'] == 1 :
        return RandomExp(Parameters, Exponential_Parameters)
    elif Parameters['DistributionFormat'] == 2 :
        return RandomPow(Parameters, Power_Parameters)
    else :
        print("Distribution Format should be 0 to 2")

def RandomExp(Parameters, Exponential_Parameters):
    """Create random number that follow exp distribution"""
    UncheckedChance = random.uniform(0,1)
    while (UncheckedChance == 0 or UncheckedChance == 1) :
        UncheckedChance = random.uniform(0,1)

    return (-1 / Exponential_Parameters[Parameters['InitialParameter']]) * log(1 - UncheckedChance)

def RandomPow(Parameters, Power_Parameters):
    """Create random number that follow Power distribution"""
    UncheckedChance = random.uniform(0,1)
    while (UncheckedChance == 0 or UncheckedChance == 1) :
        UncheckedChance = random.uniform(0,1)

    return 1 / pow(1 - UncheckedChance, (1 / Power_Parameters[Parameters['InitialParameter']]))

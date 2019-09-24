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
    pass

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
    UncheckedChance = random.uniform(0,1)
    while (UncheckedChance == 0 or UncheckedChance == 1) :
        UncheckedChance = random.uniform(0,1)

    return (-1 / Exponential_Parameters[Parameters['InitialParameter']]) * log(1 - UncheckedChance)

def RandomPow(Parameters, Power_Parameters):
    UncheckedChance = random.uniform(0,1)
    while (UncheckedChance == 0 or UncheckedChance == 1) :
        UncheckedChance = random.uniform(0,1)

    return 1 / pow(1 - UncheckedChance, (1 / Power_Parameters[Parameters['InitialParameter']]))

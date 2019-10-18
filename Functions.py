import random
import os
import time
import sys
import csv
import math

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
        print("Static or Not parameters should be 0 or 1")

def Mining(Hash_list, Crypto_Wealth_list, Parameters):
    """Decide which node will success mining, and get reward"""
    total = 0
    for i in range(len(Hash_list)) :
        total += Hash_list[i]

    Success_Possibility = random.uniform(0, total)
    Success_Indicator = 0
    for i in range(len(Hash_list)) :
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
        if len(Hash_list) < Parameters['NodeSize'] :
            Hash_list += [RandomDisGen(Parameters)]
            Crypto_Wealth_list += [0]

def Reinvestment(Hash_list, Crypto_Wealth_list, Parameters):
    """Decide each node reinvest to their hash power and make distribution of wealth"""
    if len(Hash_list) > 1 :
        cost_list = list()
        reinvestment_ratio_list = [0.0001, 0.0005, 0.001, 0.00125, 0.0025, 0.005, 0.0075,
            0.00875, 0.01, 0.0125, 0.025, 0.05, 0.075, 0.0875, 0.1, 0.5]

        maximum_wealth = 0
        for i in range(len(Hash_list)) :
            if maximum_wealth < Crypto_Wealth_list[i] :
                maximum_wealth = Crypto_Wealth_list[i]
        for i in range(len(Hash_list)):
            Hash_list[i] += reinvestment_ratio_list[Parameters['ReinvestmentParameter']] * Crypto_Wealth_list[i]
            cost_list += [reinvestment_ratio_list[Parameters['ReinvestmentParameter']] * Crypto_Wealth_list[i]]
            Crypto_Wealth_list[i] -= reinvestment_ratio_list[Parameters['ReinvestmentParameter']] * Crypto_Wealth_list[i]
        """
        reinvestment_chance = 0
        for i in range(len(Hash_list)) :
            reinvestment_chance = random.uniform(0,1)
            if reinvestment_chance <= (Crypto_Wealth_list[i] / maximum_wealth) :
                Hash_list[i] += reinvestment_ratio_list[Parameters['ReinvestmentParameter']] * Crypto_Wealth_list[i]
                cost_list += [reinvestment_ratio_list[Parameters['ReinvestmentParameter']] * Crypto_Wealth_list[i]]
                Crypto_Wealth_list[i] -= reinvestment_ratio_list[Parameters['ReinvestmentParameter']] * Crypto_Wealth_list[i]
            else :
                cost_list += [0]
        """
        
        temp = 0
        multi = 1.0 / (len(Hash_list) - 1)
        for i in range(len(Hash_list)) :
            temp += cost_list[i]

        for i in range(len(Hash_list)) :
            cost_list[i] = (temp - cost_list[i]) * multi
            Crypto_Wealth_list[i] += cost_list[i]

def FilePrint(Hash_list, Crypto_Wealth_list, Parameters):
    """Print out CSV file of hash power and crypto-currency"""

    filename_hash = str(Parameters['Repeat']) + 'h' + 'di' + str(Parameters['DistributionFormat']) + 'dp' + str(Parameters['InitialParameter']) + 's' + str(Parameters['NodeSize']) + 'n' + str(Parameters['ProcessingNumber']) + 'G' + str(Parameters['StaticOrNot']) + 're' + str(Parameters['ReinvestmentParameter']) + '.csv'
    fileout_hash = open(filename_hash, 'w')
    wrh = csv.writer(fileout_hash)
    wrh.writerow(['Hash', 'Accumulated frequency'])

    ach = 0
    for i in range(len(Hash_list) - 1) :
        ach += 1
        if Hash_list[i+1] < Hash_list[i] :
            wrh.writerow([Hash_list[i], ach])

    ach += 1
    wrh.writerow([Hash_list[Parameters['NodeSize'] - 1], ach])
    fileout_hash.close()

    filename_crypto = str(Parameters['Repeat']) + 'c' + 'di' + str(Parameters['DistributionFormat']) + 'dp' + str(Parameters['InitialParameter']) + 's' + str(Parameters['NodeSize']) + 'n' + str(Parameters['ProcessingNumber']) + 'G' + str(Parameters['StaticOrNot']) + 're' + str(Parameters['ReinvestmentParameter']) + '.csv'
    fileout_crypto = open(filename_crypto, 'w')
    wrc = csv.writer(fileout_crypto)
    wrc.writerow(['Cryptocurrency, Accumulated frequency'])

    acc = 0
    for i in range(len(Crypto_Wealth_list) - 1) :
        acc += 1
        if Crypto_Wealth_list[i+1] < Crypto_Wealth_list[i] :
            wrc.writerow([Crypto_Wealth_list[i], acc])

    acc += 1
    wrc.writerow([Crypto_Wealth_list[Parameters['NodeSize'] - 1], acc])
    fileout_crypto.close()

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
    while UncheckedChance == 0 or UncheckedChance == 1:
        UncheckedChance = random.uniform(0,1)

    return (-1 / Exponential_Parameters[Parameters['InitialParameter']]) * math.log(1 - UncheckedChance)

def RandomPow(Parameters, Power_Parameters):
    """Create random number that follow Power distribution"""
    UncheckedChance = random.uniform(0,1)
    while UncheckedChance == 0 or UncheckedChance == 1:
        UncheckedChance = random.uniform(0,1)

    return 1.0 / pow(1 - UncheckedChance, (1.0 / Power_Parameters[Parameters['InitialParameter']]))

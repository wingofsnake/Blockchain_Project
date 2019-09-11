import random
import os
import time
import sys

def Set_List(Hash_list, Crypto_Wealth_list, Parameters):
    """Initialize Hash and Wealth lists with input parameters"""
    if Parameters['StaticOrNot'] == 0
        for i in range(Parameters['NodeSize'])
            Hash_list += RandomDisGen(Parameters)
            Crypto_Wealth_list += 0
    else if Parameters['StaticOrNot'] == 1
        Hash_list += RandomDisGen(Parameters)
        Crypto_Wealth_list += 0

def Mining(Hash_list, Crypto_Wealth_list, Parameters):
    pass

def Investment(Hash_list, Crypto_Wealth_list, Parameters):
    pass

def Reinvestment(Hash_list, Crypto_Wealth_list, Parameters):
    pass

def FilePrint(Hash_list, Crypto_Wealth_list, Parameters):
    pass

def RandomDisGen(Parameters):
    """Create random number to make specific types of distribution"""
    Uniform_Parameters = [1, 5, 10]
    Exponential_Parameters = [0.1, 1, 5]
    Power_Parameters = [2, 2.5, 3]

    if Parameters['DistributionFormat'] == 0
        return random.uniform(0, Uniform_Parameters[Parameters['InitialParameter']])
    else if Parameters['DistributionFormat'] == 1
        return RandomExp(Parameters, Exponential_Parameters)
    else if Parameters['DistributionFormat'] == 2
        return RandomPow(Parameters, Power_Parameters)

def RandomExp(Parameters, Exponential_Parameters):
    pass

def RandomPow(Parameters, Power_Parameters):
    pass

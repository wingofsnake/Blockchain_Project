#import section
import sys

#from concurrent import futures

from Functions import Set_List, Mining, Investment, Reinvestment, FilePrint()

#define functions
def set_parameter(Parameters):
    """Set parameters with system argument values"""

    Parameters['Repeat'] = int(sys.argv[1])
    Parameters['StaticOrNot'] = int(sys.argv[2])
    Parameters['DistributionFormat'] = int(sys.argv[3])
    Parameters['InitialParameter'] = int(sys.argv[4])
    Parameters['NodeSize'] = int(sys.argv[5])
    Parameters['ProcessingNumber'] = int(sys.argv[6])
    Parameters['ReinvestmentParameter'] = int(sys.argv[7])

def processing(Hash_list, Crypto_Wealth_list, Parameters):
    """Call Set_List function, Mining function, Investment function,
    Reinvestment function, and fileIO function"""

    Set_List(Hash_list, Crypto_Wealth_list, Parameters)
    Mining(Hash_list, Crypto_Wealth_list, Parameters)
    Investment(Hash_list, Crypto_Wealth_list, Parameters)
    Reinvestment(Hash_list, Crypto_Wealth_list, Parameters)

    FilePrint(Hash_list, Crypto_Wealth_list, Parameters)

if __name__ == '__main__':

    #define dictionary for parameters
    Parameters = {'Repeat': 0, 'StaticOrNot' : 0,
    'DistributionFormat': 0, 'InitialParameter': 0, 'NodeSize': 0,
    'ProcessingNumber': 0, 'ReinvestmentParameter': 0}

    set_parameter(Parameters)

    #define main two variables
    Hash_list = list()
    Crypto_Wealth_list = list()

    processing(Hash_list, Crypto_Wealth_list, Parameters)



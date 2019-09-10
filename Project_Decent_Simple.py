#import section
import sys

#define main two variables

Hash_list = list()
Crypto_list = list()

#define functions


def set_parameter(Parameters):
    """Set parameters with system argument values"""
    Parameters['Repeat'] = int(sys.argv[1])
    Parameters['Repeat'] = int(sys.argv[2])
    Parameters['Repeat'] = int(sys.argv[3])
    Parameters['Repeat'] = int(sys.argv[4])
    Parameters['Repeat'] = int(sys.argv[5])
    Parameters['Repeat'] = int(sys.argv[6])
    Parameters['Repeat'] = int(sys.argv[7])

#Main function

if __name__ == '__name__':
    #define dictionary for parameters
    Parameters = {'Repeat': 0, 'StaticOrNot' : 0,
    'DistributionFormat': 0, 'InitialParameter': 0, 'NodeSize': 0,
    'ProcessingNumber': 0, 'ReinvestmentParameter': 0}

    print (1)
    set_parameter(Parameters)
    print (2)


    for key in Parameters.keys():
        print(key, ":". Parameters[key])

    print (4)
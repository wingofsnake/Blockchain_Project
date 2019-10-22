import sys
import os
import time

from multiprocessing import Process

from Functions import Set_List, Mining, Investment, Reinvestment, FilePrint

#define functions
def set_parameter(Parameters):
    """Set parameters with system argument values"""

    Parameters['Repeat'] = int(sys.argv[1])
    Parameters['NumCore'] = int(sys.argv[2])
    #Parameters['StaticOrNot'] = int(sys.argv[2])
    #Parameters['DistributionFormat'] = int(sys.argv[3])
    #Parameters['InitialParameter'] = int(sys.argv[4])
    #Parameters['NodeSize'] = int(sys.argv[5])
    #Parameters['ProcessingNumber'] = int(sys.argv[6])
    #Parameters['ReinvestmentParameter'] = 16

def processing_multi(Hash_list, Crypto_Wealth_list, Parameters, reinvestment_ratio_list):
    """Call Set_List function, Mining function, Investment function,
    Reinvestment function, and fileIO function"""

    copied_dic = Parameters.copy()

    for repeat in range(Parameters['Repeat']) :
        for Dis in range(Parameters['DistributionFormat']) :
            for Ini in range(Parameters['InitialParameter']) :
                for Growth in range(Parameters['StaticOrNot']) :
                    for reinv in range(int((Parameters['ReinvestmentParameter']/Parameters['NumCore']))) :

                        copied_dic['Repeat'] = repeat
                        copied_dic['DistributionFormat'] = Dis
                        copied_dic['InitialParameter'] = Ini
                        copied_dic['StaticOrNot'] = Growth
                        copied_dic['ReinvestmentParameter'] = (reinv * Parameters['NumCore'])
                        print(copied_dic)

                        Hash_list = list()
                        Crypto_Wealth_list = list()

                        Set_List(Hash_list, Crypto_Wealth_list, copied_dic)


                        procs = []
                        for i in range(Parameters['NumCore']) :
                            proc = Process(target = processing, args = (Hash_list, Crypto_Wealth_list, copied_dic, i, reinvestment_ratio_list))
                            procs.append(proc)
                            proc.start()

                        for proc in procs :
                            proc.join()
                        #sys.exit()

def processing(Hash_list, Crypto_Wealth_list, copied_dic, index, reinvestment_ratio_list) :

    copied_dic['ReinvestmentParameter'] = copied_dic['ReinvestmentParameter'] + index
    pid = os.getpid()
    for i in range(copied_dic['ProcessingNumber']) :
        Mining(Hash_list, Crypto_Wealth_list, copied_dic)
        Investment(Hash_list, Crypto_Wealth_list, copied_dic)
        Reinvestment(Hash_list, Crypto_Wealth_list, copied_dic, reinvestment_ratio_list)
        if (i % 1000) == 0:
            print('{0}th calculation by process id: {1}'.format(i, pid))
        #print('{0}th calculation by process id: {1}'.format(i, pid))

    Hash_list.sort(reverse = True)
    Crypto_Wealth_list.sort(reverse = True)

    FilePrint(Hash_list, Crypto_Wealth_list, copied_dic)

    print('Dis = ' + str(copied_dic['DistributionFormat']) + ' Par = ' + str(copied_dic['InitialParameter']) + ' G = ' + str(copied_dic['StaticOrNot']) + ' Reinv  = ' + str(copied_dic['ReinvestmentParameter'] + index))

if __name__ == '__main__':

    #define dictionary for parameters
    Parameters = {'Repeat': 1, 'StaticOrNot': 2,
    'DistributionFormat': 3, 'InitialParameter': 3, 'NodeSize': 100000,
    'ProcessingNumber': 100000, 'ReinvestmentParameter': 16, 'NumCore':1}
    reinvestment_ratio_list = [0.0001, 0.0005, 0.001, 0.00125, 0.0025, 0.005, 0.0075,
                               0.00875, 0.01, 0.0125, 0.025, 0.05, 0.075, 0.0875, 0.1, 0.5]

    set_parameter(Parameters)
    print(Parameters)

    #define main two variables
    Hash_list = list()
    Crypto_Wealth_list = list()

    processing_multi(Hash_list, Crypto_Wealth_list, Parameters, reinvestment_ratio_list)
    print(Parameters['NodeSize'])









import csv
import glob
import os
import sys

import matplotlib.pyplot as plt
import math

from Drawing_Graph import Opening_files, Making_list

def Reshape_Data(Hash_list, Ac_list, Hash_loged_list, Ac_loged_list):
    for i in range(64):
        Max_val = Hash_list[i][0]
        Min_val = Hash_list[i][len(Hash_list[i]) - 1]
        division_ratio = Max_val - Min_val
        Hash_loged_value = list()
        Ac_loged_value = list()
        if division_ratio == 0:
            division_ratio = 1
        for index in range(len(Hash_list[i])):
            Hash_list[i][index] = (((Hash_list[i][index] - Min_val) * 9.0) / division_ratio) + 1
            Ac_loged_value += [math.log(Ac_list[i][index])]
            Hash_loged_value += [math.log(Hash_list[i][index])]
        Hash_loged_list.append(Hash_loged_value)
        Ac_loged_list.append(Ac_loged_value)

def ploting_LineartoLinear_RWB(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    output_file_name = input_file_name[path_length + 1: total_length - 18] + 're2rdi1' + 't1.png'
    for i in range(len(ratio_list)):
        plt.plot(Hash_list[i + 36], Ac_list[i + 36], label=ratio_list[i], linewidth=0.5)
        plt.scatter(Hash_list[i + 36], Ac_list[i + 36], s=1)

    if HorC == 0:
        plt.title('Hash-Accumulated Frequency')
        plt.xlabel('Hash')
    else:
        plt.title('Cryptocurrency-Accumulated Frequency')
        plt.xlabel('Cryptocurrency')
    plt.ylabel('Accumulated Frequency')
    plt.legend()
    plt.savefig(output_file_name, dpi=350)

    plt.close()

def ploting_LineartoLog_RWB(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    output_file_name = input_file_name[path_length + 1: total_length - 18] + 're2rdi1' + 't2.png'
    for i in range(len(ratio_list)):
        plt.plot(Hash_list[i + 36], Ac_list[i + 36], label=ratio_list[i], linewidth=0.5)
        plt.scatter(Hash_list[i + 36], Ac_list[i + 36], s=1)

    if HorC == 0:
        plt.title('Hash-Accumulated Frequency')
        plt.xlabel('Hash')
    else:
        plt.title('Cryptocurrency-Accumulated Frequency')
        plt.xlabel('Cryptocurrency')
    plt.ylabel('Accumulated Frequency')
    plt.legend()
    plt.savefig(output_file_name, dpi=350)

    plt.close()

def ploting_LogtoLog_RWB(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    output_file_name = input_file_name[path_length + 1: total_length - 18] + 're2rdi1' + 't3.png'
    for i in range(len(ratio_list)):
        plt.plot(Hash_list[i + 36], Ac_list[i + 36], label=ratio_list[i], linewidth=0.5)
        plt.scatter(Hash_list[i + 36], Ac_list[i + 36], s=1)

    if HorC == 0:
        plt.title('Hash-Accumulated Frequency')
        plt.xlabel('Hash')
    else:
        plt.title('Cryptocurrency-Accumulated Frequency')
        plt.xlabel('Cryptocurrency')
    plt.ylabel('Accumulated Frequency')
    plt.legend()
    plt.savefig(output_file_name, dpi=350)

    plt.close()

def ploting_LineartoLinear_Reinvbase(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    for j in range(4):
        output_file_name = input_file_name[path_length + 1 : total_length - 18] + 're' + str(j) + 't1.png'
        for i in range(len(ratio_list)):
            plt.plot(Hash_list[i + j*16], Ac_list[i + j*16], label=ratio_list[i], linewidth=0.5)
            plt.scatter(Hash_list[i + j*16], Ac_list[i + j*16], s=1)

        if HorC == 0:
            plt.title('Hash-Accumulated Frequency')
            plt.xlabel('Hash')
        else:
            plt.title('Cryptocurrency-Accumulated Frequency')
            plt.xlabel('Cryptocurrency')
        plt.ylabel('Accumulated Frequency')
        plt.legend()
        plt.savefig(output_file_name, dpi = 350)

        plt.close()

def ploting_LineartoLog_Reinvbase(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    for j in range(4):
        output_file_name = input_file_name[path_length + 1: total_length - 18] + 're' + str(j) + 't2.png'
        for i in range(len(ratio_list)):
            plt.plot(Hash_list[i + j * 16], Ac_list[i + j * 16], label=ratio_list[i], linewidth=0.5)
            plt.scatter(Hash_list[i + j * 16], Ac_list[i + j * 16], s=1)

        if HorC == 0:
            plt.title('Hash-Accumulated Frequency')
            plt.xlabel('Hash')
        else:
            plt.title('Cryptocurrency-Accumulated Frequency')
            plt.xlabel('Cryptocurrency')
        plt.ylabel('Accumulated Frequency')
        plt.legend()
        plt.savefig(output_file_name, dpi=350)

        plt.close()


def ploting_LogtoLog_Reinvbase(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    for j in range(4):
        output_file_name = input_file_name[path_length + 1: total_length - 18] + 're' + str(j) + 't3.png'
        for i in range(len(ratio_list)):
            plt.plot(Hash_list[i + j * 16], Ac_list[i + j * 16], label=ratio_list[i], linewidth=0.5)
            plt.scatter(Hash_list[i + j * 16], Ac_list[i + j * 16], s=1)

        if HorC == 0:
            plt.title('Hash-Accumulated Frequency')
            plt.xlabel('Hash')
        else:
            plt.title('Cryptocurrency-Accumulated Frequency')
            plt.xlabel('Cryptocurrency')
        plt.ylabel('Accumulated Frequency')
        plt.legend()
        plt.savefig(output_file_name, dpi=350)

        plt.close()

def ploting_LineartoLinear_Redibase(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    for j in range(4):
        output_file_name = input_file_name[path_length + 1: total_length - 18] + 'rdi' + str(j) + 't1.png'
        for i in range(len(ratio_list)):
            plt.plot(Hash_list[(i + (12 * int(i/4))) + j * 4], Ac_list[(i + (12 * int(i/4))) + j * 4], label=ratio_list[i], linewidth=0.5)
            plt.scatter(Hash_list[(i + (12 * int(i/4))) + j * 4], Ac_list[(i + (12 * int(i/4))) + j * 4], s=1)

        if HorC == 0:
            plt.title('Hash-Accumulated Frequency')
            plt.xlabel('Hash')
        else:
            plt.title('Cryptocurrency-Accumulated Frequency')
            plt.xlabel('Cryptocurrency')
        plt.ylabel('Accumulated Frequency')
        plt.legend()
        plt.savefig(output_file_name, dpi=350)

        plt.close()

def ploting_LineartoLog_Redibase(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    for j in range(4):
        output_file_name = input_file_name[path_length + 1: total_length - 18] + 'rdi' + str(j) + 't2.png'
        for i in range(len(ratio_list)):
            plt.plot(Hash_list[(i + (12 * int(i / 4))) + j * 4], Ac_list[(i + (12 * int(i / 4))) + j * 4],
                     label=ratio_list[i], linewidth=0.5)
            plt.scatter(Hash_list[(i + (12 * int(i / 4))) + j * 4], Ac_list[(i + (12 * int(i / 4))) + j * 4], s=1)

        if HorC == 0:
            plt.title('Hash-Accumulated Frequency')
            plt.xlabel('Hash')
        else:
            plt.title('Cryptocurrency-Accumulated Frequency')
            plt.xlabel('Cryptocurrency')
        plt.ylabel('Accumulated Frequency')
        plt.legend()
        plt.savefig(output_file_name, dpi=350)

        plt.close()

def ploting_LogtoLog_Redibase(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    for j in range(4):
        output_file_name = input_file_name[path_length + 1: total_length - 18] + 'rdi' + str(j) + 't3.png'
        for i in range(len(ratio_list)):
            plt.plot(Hash_list[(i + (12 * int(i / 4))) + j * 4], Ac_list[(i + (12 * int(i / 4))) + j * 4],
                     label=ratio_list[i], linewidth=0.5)
            plt.scatter(Hash_list[(i + (12 * int(i / 4))) + j * 4], Ac_list[(i + (12 * int(i / 4))) + j * 4], s=1)

        if HorC == 0:
            plt.title('Hash-Accumulated Frequency')
            plt.xlabel('Hash')
        else:
            plt.title('Cryptocurrency-Accumulated Frequency')
            plt.xlabel('Cryptocurrency')
        plt.ylabel('Accumulated Frequency')
        plt.legend()
        plt.savefig(output_file_name, dpi=350)

        plt.close()

def ploting_LineartoLinear_Rewardbase(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    for j in range(4):
        output_file_name = input_file_name[path_length + 1: total_length - 18] + 'rw' + str(j) + 't1.png'
        for i in range(len(ratio_list)):
            plt.plot(Hash_list[i*4 + j], Ac_list[i*4 + j],
                     label= ratio_list[i], linewidth=0.5)
            plt.scatter(Hash_list[i*4 + j], Ac_list[i*4 + j], s=1)

        if HorC == 0:
            plt.title('Hash-Accumulated Frequency')
            plt.xlabel('Hash')
        else:
            plt.title('Cryptocurrency-Accumulated Frequency')
            plt.xlabel('Cryptocurrency')
        plt.ylabel('Accumulated Frequency')
        plt.legend()
        plt.savefig(output_file_name, dpi=350)

        plt.close()

def ploting_LineartoLog_Rewardbase(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    for j in range(4):
        output_file_name = input_file_name[path_length + 1: total_length - 18] + 'rw' + str(j) + 't2.png'
        for i in range(len(ratio_list)):
            plt.plot(Hash_list[i * 4 + j], Ac_list[i * 4 + j],
                     label=ratio_list[i], linewidth=0.5)
            plt.scatter(Hash_list[i * 4 + j], Ac_list[i * 4 + j], s=1)

        if HorC == 0:
            plt.title('Hash-Accumulated Frequency')
            plt.xlabel('Hash')
        else:
            plt.title('Cryptocurrency-Accumulated Frequency')
            plt.xlabel('Cryptocurrency')
        plt.ylabel('Accumulated Frequency')
        plt.legend()
        plt.savefig(output_file_name, dpi=350)

        plt.close()

def ploting_LogtoLog_Rewardbase(Hash_list, Ac_list, input_file_name, ratio_list, HorC, total_length, path_length):
    for j in range(4):
        output_file_name = input_file_name[path_length + 1: total_length - 18] + 'rw' + str(j) + 't3.png'
        for i in range(len(ratio_list)):
            plt.plot(Hash_list[i * 4 + j], Ac_list[i * 4 + j],
                     label=ratio_list[i], linewidth=0.5)
            plt.scatter(Hash_list[i * 4 + j], Ac_list[i * 4 + j], s=1)

        if HorC == 0:
            plt.title('Hash-Accumulated Frequency')
            plt.xlabel('Hash')
        else:
            plt.title('Cryptocurrency-Accumulated Frequency')
            plt.xlabel('Cryptocurrency')
        plt.ylabel('Accumulated Frequency')
        plt.legend()
        plt.savefig(output_file_name, dpi=350)

        plt.close()

if __name__ == '__main__':

    input_path_Hash = "D:\Dropbox\PhD Research\Blockchain_Code\Python\Data\Exp_Reward\Hash\Rit1"
    input_path_crypto = "D:\Dropbox\PhD Research\Blockchain_Code\Python\Data\Exp_Reward\Cryptocurrency\Rit1"
    input_files_Hash = glob.glob(os.path.join(input_path_Hash, '*.csv'))
    input_files_crypto = glob.glob(os.path.join(input_path_crypto, '*.csv'))

    reinvestment_ratio_list = ['rdi=0.0001, rw=1', 'rdi=0.0001, rw=10', 'rdi=0.0001, rw=30', 'rdi=0.0001, rw=50',\
                               'rdi=0.001 rw=1', 'rdi=0.001 rw=10', 'rdi=0.001 rw=30', 'rdi=0.001 rw=50',\
                               'rdi=0.01 rw=1', 'rdi=0.01 rw=10', 'rdi=0.01 rw=30', 'rdi=0.01 rw=50',\
                               'rdi=0.1 rw=1', 'rdi=0.1 rw=10', 'rdi=0.1 rw=30', 'rdi=0.1 rw=50']
    redistribution_ratio_list = ['re=0.0001, rw=1', 're=0.0001, rw=10', 're=0.0001, rw=30', 're=0.0001, rw=50', \
                               're=0.001 rw=1', 're=0.001 rw=10', 're=0.001 rw=30', 're=0.001 rw=50', \
                               're=0.01 rw=1', 're=0.01 rw=10', 're=0.01 rw=30', 're=0.01 rw=50', \
                               're=0.1 rw=1', 're=0.1 rw=10', 're=0.1 rw=30', 're=0.1 rw=50']
    reward_ratio_list = ['re=0.0001, rdi=0.0001', 're=0.0001, rdi=0.001', 're=0.0001, rdi=0.01', 're=0.0001, rdi=0.1', \
                               're=0.001, rdi=0.0001', 're=0.001, rdi=0.001', 're=0.001, rdi=0.01', 're=0.001, rdi=0.1',\
                               're=0.01, rdi=0.0001', 're=0.01, rdi=0.001', 're=0.01, rdi=0.01', 're=0.01, rdi=0.1',\
                               're=0.1, rdi=0.0001', 're=0.1, rdi=0.001', 're=0.1, rdi=0.01', 're=0.1, rdi=0.1']
    RW_ratio_list = [1, 10, 30, 50]
    i = 0
    while i < len(input_files_Hash):
        Hash_list = list()
        Ac_list = list()

        Hash_loged_list = list()
        Ac_loged_list = list()

        Opening_files(Hash_list, Ac_list, i, input_files_Hash, 64)
        Reshape_Data(Hash_list, Ac_list, Hash_loged_list, Ac_loged_list)

        ploting_LineartoLinear_RWB(Hash_list, Ac_list, input_files_Hash[i], RW_ratio_list, 0,
                                         len(input_files_Hash[i]), len(input_path_Hash))
        ploting_LineartoLog_RWB(Hash_list, Ac_loged_list, input_files_Hash[i], RW_ratio_list, 0,
                                      len(input_files_Hash[i]), len(input_path_Hash))
        ploting_LogtoLog_RWB(Hash_loged_list, Ac_loged_list, input_files_Hash[i], RW_ratio_list, 0,
                                   len(input_files_Hash[i]), len(input_path_Hash))
        i=i+64

    j = 0
    while j < len(input_files_Hash):
        Hash_list = list()
        Ac_list = list()

        Hash_loged_list = list()
        Ac_loged_list = list()

        Opening_files(Hash_list, Ac_list, j, input_files_crypto, 64)
        Reshape_Data(Hash_list, Ac_list, Hash_loged_list, Ac_loged_list)

        ploting_LineartoLinear_RWB(Hash_list, Ac_list, input_files_crypto[j], RW_ratio_list, 1,
                                         len(input_files_crypto[j]), len(input_path_crypto))
        ploting_LineartoLog_RWB(Hash_list, Ac_loged_list, input_files_crypto[j], RW_ratio_list, 1,
                                      len(input_files_crypto[j]), len(input_path_crypto))
        ploting_LogtoLog_RWB(Hash_loged_list, Ac_loged_list, input_files_crypto[j], RW_ratio_list, 1,
                                   len(input_files_crypto[j]), len(input_path_crypto))
        
        j = j + 64




"""
    i = 0
    while i < len(input_files_Hash):
        Hash_list = list()
        Ac_list = list()

        Hash_loged_list = list()
        Ac_loged_list = list()

        Opening_files(Hash_list, Ac_list, i, input_files_Hash, 64)
        Reshape_Data(Hash_list, Ac_list, Hash_loged_list, Ac_loged_list)

        ploting_LineartoLinear_Reinvbase(Hash_list, Ac_list, input_files_Hash[i], reinvestment_ratio_list, 0, len(input_files_Hash[i]), len(input_path_Hash))
        ploting_LineartoLog_Reinvbase(Hash_list, Ac_loged_list, input_files_Hash[i], reinvestment_ratio_list, 0,
                                    len(input_files_Hash[i]), len(input_path_Hash))
        ploting_LogtoLog_Reinvbase(Hash_loged_list, Ac_loged_list, input_files_Hash[i], reinvestment_ratio_list, 0,
                                    len(input_files_Hash[i]), len(input_path_Hash))

        ploting_LineartoLinear_Redibase(Hash_list, Ac_list, input_files_Hash[i], redistribution_ratio_list, 0,
                                         len(input_files_Hash[i]), len(input_path_Hash))
        ploting_LineartoLog_Redibase(Hash_list, Ac_loged_list, input_files_Hash[i], redistribution_ratio_list, 0,
                                      len(input_files_Hash[i]), len(input_path_Hash))
        ploting_LogtoLog_Redibase(Hash_loged_list, Ac_loged_list, input_files_Hash[i], redistribution_ratio_list, 0,
                                   len(input_files_Hash[i]), len(input_path_Hash))

        ploting_LineartoLinear_Rewardbase(Hash_list, Ac_list, input_files_Hash[i], reward_ratio_list, 0,
                                         len(input_files_Hash[i]), len(input_path_Hash))
        ploting_LineartoLog_Rewardbase(Hash_list, Ac_loged_list, input_files_Hash[i], reward_ratio_list, 0,
                                      len(input_files_Hash[i]), len(input_path_Hash))
        ploting_LogtoLog_Rewardbase(Hash_loged_list, Ac_loged_list, input_files_Hash[i], reward_ratio_list, 0,
                                   len(input_files_Hash[i]), len(input_path_Hash))

        i = i + 64

    j = 0
    while j < len(input_files_Hash):
        Hash_list = list()
        Ac_list = list()

        Hash_loged_list = list()
        Ac_loged_list = list()

        Opening_files(Hash_list, Ac_list, j, input_files_crypto, 64)
        Reshape_Data(Hash_list, Ac_list, Hash_loged_list, Ac_loged_list)

        ploting_LineartoLinear_Reinvbase(Hash_list, Ac_list, input_files_crypto[j], reinvestment_ratio_list, 1,
                                         len(input_files_crypto[j]), len(input_path_crypto))
        ploting_LineartoLog_Reinvbase(Hash_list, Ac_loged_list, input_files_crypto[j], reinvestment_ratio_list, 1,
                                      len(input_files_crypto[j]), len(input_path_crypto))
        ploting_LogtoLog_Reinvbase(Hash_loged_list, Ac_loged_list, input_files_crypto[j], reinvestment_ratio_list, 1,
                                   len(input_files_crypto[j]), len(input_path_crypto))

        ploting_LineartoLinear_Redibase(Hash_list, Ac_list, input_files_crypto[j], redistribution_ratio_list, 1,
                                        len(input_files_crypto[j]), len(input_path_crypto))
        ploting_LineartoLog_Redibase(Hash_list, Ac_loged_list, input_files_crypto[j], redistribution_ratio_list, 1,
                                     len(input_files_crypto[j]), len(input_path_crypto))
        ploting_LogtoLog_Redibase(Hash_loged_list, Ac_loged_list, input_files_crypto[j], redistribution_ratio_list, 1,
                                  len(input_files_crypto[j]), len(input_path_crypto))

        ploting_LineartoLinear_Rewardbase(Hash_list, Ac_list, input_files_crypto[j], reward_ratio_list, 1,
                                          len(input_files_crypto[j]), len(input_path_crypto))
        ploting_LineartoLog_Rewardbase(Hash_list, Ac_loged_list, input_files_crypto[j], reward_ratio_list, 1,
                                       len(input_files_crypto[j]), len(input_path_crypto))
        ploting_LogtoLog_Rewardbase(Hash_loged_list, Ac_loged_list, input_files_crypto[j], reward_ratio_list, 1,
                                    len(input_files_crypto[j]), len(input_path_crypto))
        j = j + 64
"""
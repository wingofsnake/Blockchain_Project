import csv
import glob
import os
import matplotlib.pyplot as plt
import math

def Opening_files (Hash_list, Ac_list, i, input_files) :
    for index in range(16):
        csv_file = open(input_files[index + i], 'r', encoding='utf-8')
        csv_reader = csv.reader(csv_file)
        Hash_value = list()
        Ac_value = list()
        header = next(csv_reader)
        Making_list(Hash_value, Ac_value, csv_reader)
        Hash_list.append(Hash_value)
        Ac_list.append(Ac_value)
        csv_file.close()

def Making_list (Hash_value, Ac_value, csv_reader) :

    for line in csv_reader :
        if len(line) == 0 :
            continue
        else:
            Hash_value.append(float(line[0]))
            Ac_value.append(int(line[1]))

def ploting_LineartoLinear(Hash_list, Ac_list, input_file_name, reinvestment_ratio_list, HorC) :
    if HorC == 0 :
        output_file_name = input_file_name[57:81] + 't1.png'
    else:
        output_file_name = input_file_name[66:90] + 't1.png'

    for i in range(16) :
        Max_val = Hash_list[i][0]
        Min_val = Hash_list[i][len(Hash_list[i]) - 1]
        division_ratio = Max_val - Min_val
        for index in range(len(Hash_list[i])) :
            #Hash_list[i][index] = (((Hash_list[i][index] - Min_val) * 9.0) / division_ratio) + 1
            Hash_list[i][index] = Hash_list[i][index]/Min_val
        plt.plot(Hash_list[i], Ac_list[i], label = reinvestment_ratio_list[i], linewidth = 0.5)
        plt.scatter(Hash_list[i], Ac_list[i], s = 1)
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

def ploting_LineartoLog(Hash_list, Ac_list, input_file_name, reinvestment_ratio_list, HorC):
    if HorC == 0:
        output_file_name = input_file_name[57:81] + 't2.png'
    else:
        output_file_name = input_file_name[66:90] + 't2.png'
    for i in range(16):
        for index in range(len(Hash_list[i])):
            Ac_list[i][index] = math.log(Ac_list[i][index])
        plt.plot(Hash_list[i], Ac_list[i], label=reinvestment_ratio_list[i], linewidth=0.5)
        plt.scatter(Hash_list[i], Ac_list[i], s=1)
    if HorC == 0 :
        plt.title('Hash-log(Accumulated Frequency)')
        plt.xlabel('Hash')
    else :
        plt.title('Cryptocurrency-log(Accumulated Frequency)')
        plt.xlabel('Cryptocurrency')
    plt.ylabel('log(Accumulated Frequency)')
    plt.legend()
    plt.savefig(output_file_name, dpi=350)

    plt.close()

def ploting_LogtoLog(Hash_list, Ac_list, input_file_name, reinvestment_ratio_list, HorC):

    if HorC == 0 :
        output_file_name = input_file_name[57:81] + 't3.png'
    else:
        output_file_name = input_file_name[66:90] + 't3.png'
    for i in range(16):
        for index in range(len(Hash_list[i])):
            Hash_list[i][index] = math.log(Hash_list[i][index])
        plt.plot(Hash_list[i], Ac_list[i], label=reinvestment_ratio_list[i], linewidth=0.5)
        plt.scatter(Hash_list[i], Ac_list[i], s=1)
    if HorC == 0:
        plt.title('log(Hash)-log(Accumulated Frequency)')
        plt.xlabel('log(Hash)')
    else:
        plt.title('log(Cryptocurrency)-log(Accumulated Frequency)')
        plt.xlabel('log(Cryptocurrency)')
    plt.ylabel('log(Accumulated Frequency)')
    plt.legend()
    plt.savefig(output_file_name, dpi=350)

    plt.close()


if __name__ == '__main__':

    input_path_Hash = "E:\Dropbox\PhD Research\Blockchain_Code\Python\Data\Hash"
    input_path_crypto = "E:\Dropbox\PhD Research\Blockchain_Code\Python\Data\Cryptocurrency"
    input_files_Hash = glob.glob(os.path.join(input_path_Hash, '*.csv'))
    input_files_crypto = glob.glob(os.path.join(input_path_crypto, '*.csv'))
    reinvestment_ratio_list = [0.0001, 0.0005, 0.001, 0.00125, 0.0025, 0.005, 0.0075,
                               0.00875, 0.01, 0.0125, 0.025, 0.05, 0.075, 0.0875, 0.1, 0.5]


    i = 0
    while i < len(input_files_Hash) :
        Hash_list = list()
        Ac_list = list()
        Opening_files(Hash_list, Ac_list, i, input_files_Hash)
        ploting_LineartoLinear(Hash_list, Ac_list, input_files_Hash[i], reinvestment_ratio_list, 0)
        ploting_LineartoLog(Hash_list, Ac_list, input_files_Hash[i], reinvestment_ratio_list, 0)
        ploting_LogtoLog(Hash_list, Ac_list, input_files_Hash[i], reinvestment_ratio_list, 0)
        i = i + 16
    """j = 0
    while j < len(input_files_crypto) :
        crypto_list = list()
        Ac_list = list()
        Opening_files(crypto_list, Ac_list, j, input_files_crypto)
        ploting_LineartoLinear(crypto_list, Ac_list, input_files_crypto[j], reinvestment_ratio_list, 1)
        ploting_LineartoLog(crypto_list, Ac_list, input_files_crypto[j], reinvestment_ratio_list, 1)
        ploting_LogtoLog(crypto_list, Ac_list, input_files_crypto[j], reinvestment_ratio_list, 1)
        j = j + 16"""





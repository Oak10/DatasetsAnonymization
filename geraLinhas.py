#!/usr/bin/env python

from ast import arg
import sys
import random

def getRandomStringFromArray(arrayStrings):
    return arrayStrings[random.randint(0,len(arrayStrings)-1)]



def main(argv):
    try:
        outputFileName = 'out.txt'

        fileLeitura = open(argv[1], 'r')
        lines = fileLeitura.read().splitlines() 
        fileEscrita = open(outputFileName, "w")

        for i in range(int(argv[2])):
            fileEscrita.writelines(getRandomStringFromArray(lines)+'\n')

        fileLeitura.close()
        fileEscrita.close()
    
    except:
        print('usage: ', argv[0], ' <inputfile> <number_of_lines>')
        sys.exit(2)

    print ('Input file is ' , argv[1], ', output file is ', outputFileName, ', times ' + argv[2]  )


if __name__ == "__main__":
   main(sys.argv)

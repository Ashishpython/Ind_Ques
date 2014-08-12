#! /usr/bin/python
# -*- encoding: ASCII -*-
# Author - Ashish Jain
# Script reads STDIN for data

import csv #csv module for reading csv file
from collections import OrderedDict, namedtuple

def get_name_max_price(input_file):
    """ Use the tuple DS to get maximum share value and the corresponding time """
    with open(input_file) as f:
        reader = csv.reader(f)
        tup = namedtuple('tup', ['price', 'pname', 'hours'])
        output = OrderedDict()
        names = next(reader)[2:]
        for name in names:
            #initialize the dict
            output[name] = tup(0, 'pname', 'hours')
        for row in reader:
            pname, hours = row[:2]
            for name, price in zip(names, map(int, row[2:])): # map(int, prices)
                if output[name].price < price:
                    output[name] = tup(price, pname, hours)
    return output

def get_name_min_price(input_file):
    """ Use the tuple DS to get maximum share value and the corresponding time """
    with open(input_file) as f:
        reader = csv.reader(f)
        tup = namedtuple('tup', ['price', 'pname', 'hours'])
        output = OrderedDict()
        names = next(reader)[2:]
        for name in names:
            #initialize the dict
            output[name] = tup(next(reader)[2:][0], 'pname', 'hours')
        for row in reader:
            pname, hours = row[:2] 
            for name, price in zip(names, map(int, row[2:])): # map(int, prices)
                if output[name].price > price:
                    output[name] = tup(price, pname, hours)
    return output
def result_pattern(d):
    """ Result pattern"""
    print "Highest Cost representer"
    print "<Name>:<hours>:<cost>"
    for d1,d2 in d.items():
        print str(d2[1])+":"+str(d2[2])+":"+str(d2[0])
        
def result_pattern2(d):
    """ Result pattern"""
    print "Lowest Cost representer"
    print "<Name>:<hours>:<cost>"
    for d1,d2 in d.items():
        print str(d2[1])+":"+str(d2[2])+":"+str(d2[0])
        
def main(): # Can take a input_csv file importing modules
    try:
        flat_tuples = get_name_max_price('input.csv')
        flat_tuples2 = get_name_min_price('input.csv') 
        return (result_pattern(flat_tuples)+result_pattern2(flat_tuples2))
    except:
        return "[Critical]: Something wrong in CSV format. Plese verify."
if __name__ == "__main__":
    main() # Drive the startup

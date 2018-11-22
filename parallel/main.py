import numpy as np
import random
import string
import time
import re
import threading

import multiprocessing
from multiprocessing import Pool
from multiprocessing import Process
import os
from multiprocessing import Queue
from multiprocessing.pool import ThreadPool
from threading import Thread
import multiprocessing as mp

def multiplyArrays(NpArrays, indexFrom, indexTo, output, placeInQueue):
    if isinstance(indexFrom, int) and isinstance(indexTo, int):
        if indexTo>indexFrom:
            result = np.mat(NpArrays[indexFrom]) * np.mat(NpArrays[indexFrom + 1])
            for i in range(indexFrom+2, indexTo+1):
                result = np.mat(result) * np.mat(NpArrays[i])
            output.put(result)


if __name__ == '__main__':

    Arrays = []
    NpArrays = []
    F = []
    n = 0
    try:
        fp = open("C:/Users/sthottam/Downloads/matrices-2.txt","r")
        line = fp.readline()
        dimensions = []
        arr = []
        table = []
        while line:
            if line.find("-------------------------") != -1:
                1==1
            elif line.find("Matrix") != -1:
                test = re.search('Matrix # (.+?)\[(.+?) x (.+?)]', line)
                if test:
                    if len(table) > 0:
                        Arrays.append(table)
                    temp = [test.group(1), test.group(2), test.group(3)]
                    dimensions.append(temp)
                    temp = []
            else:
                data = line.split(' ')
                for i in data:
                    if i=="":
                        data.remove(i)
                for i in data:
                    if i.find("[[") != -1:
                        table = []
                        arr = []
                        i = re.sub("\[\[", " ", i)
                    elif i.find("[") != -1:
                        if len(arr) > 0:
                            table.append(arr)
                        arr = []
                        i = re.sub('\[', " ", i)
                    elif i.find("]]") != -1:
                        i = re.sub(']]', " ", i)
                        i = float(i)
                        arr.append(i)
                        if len(arr) > 0:
                            table.append(arr)
                        arr = []
                    if i != "" and isinstance(i, str):
                        i = re.sub('\[\[', " ", i)
                        i = re.sub('\[', " ", i)
                        i = re.sub(']', " ", i)
                        i = re.sub(']]', " ", i)
                        i = re.sub('\n', " ", i)
                    i = float(i)
                    arr.append(i)
            try:
                line = fp.readline()
            except:
                break
    except:
        print("error")
    finally:
        Arrays.append(table)
        fp.close()
        if len(Arrays) != len(dimensions):
            print("error")
        for k in range(0,len(Arrays)):
            arrayDimensions = dimensions[k]
            dimension1 = arrayDimensions[1]
            dimension2 = arrayDimensions[2]
            NpArrays.append(np.array(Arrays[k]))

    print("WITHOUT threads")
    start_time = time.time()
    numberOfMatrices = len(NpArrays)
    result = np.matrix(NpArrays[0]) * np.matrix(NpArrays[1])
    for x in range(2, len(NpArrays)):
        result = np.matrix(result) * np.matrix(NpArrays[x])
    print(result)
    time1 = time.time() - start_time
    print("time: %s" % (time.time() - start_time))


    print("WITH multi-thread")
    output = mp.Queue()
    numberOfThreads = multiprocessing.cpu_count()
    rangee = int(numberOfMatrices/numberOfThreads)
    limit = list(range(0, numberOfMatrices, rangee))
    if limit[-1] < numberOfMatrices-1:
        limit.append(numberOfMatrices)
    processes = []
    start_time = time.time()
    for i in range(0,numberOfThreads):
        if i != numberOfThreads:
            p = Process(target = multiplyArrays, args=(NpArrays, limit[i], limit[i+1]-1, output, i))
        else:
            p = Process(target = multiplyArrays, args = (NpArrays, limit[i], limit[i+1], output, i))
        p.start()
        processes.append(p)
    start_time = time.time()
    for p in processes:
        p.join()
    effects = [output.get() for p in processes]
    multiplyArrays(effects, 0, len(effects)-1, output, numberOfThreads+1)
    matrix = output.get(-1)
    print(matrix)
    time2 = time.time() - start_time
    print("time: %s" % (time.time() - start_time))
    print("time difference is ", time1/time2)
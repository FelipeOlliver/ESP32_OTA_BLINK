# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 22:25:55 2021

@author: Trixlog
"""

import os
import sys
from pathlib import Path
import math

package = []
page = []
with open('blink_blue3.bin', 'r+b') as file:
    size = math.ceil((len(file.read()))/128)
    print(size)
    byte = file.read(1)
    #package.append(byte)
    #while byte != b'':
    i=0
    j=0
    while i<size:
        file.seek(128*i)
        while j<127:    
            #print(byte)
            byte = file.read(1)
            package.append(byte)
            j=j+1
        
        #print(package)

        page.append(package)
        print(page[i])
        print("\n")


        
        i=i+1
        j=0
        package.clear()


    #file.seek(2, 0)
    #file.write(b'\xFF')
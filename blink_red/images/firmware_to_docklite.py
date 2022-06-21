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

myfile = Path('packages_sender.ptp')
myfile.touch(exist_ok=True)
with open(myfile,'w+') as pkg:
    pkg.writelines("VERSION\n")
    pkg.writelines("8\n")
    pkg.writelines("\n")
    pkg.writelines("COMMSETTINGS\n")
    pkg.writelines("0\n")
    pkg.writelines("COM19\n")
    pkg.writelines("COM2\n")
    pkg.writelines("115200\n")
    pkg.writelines("2\n")
    pkg.writelines("63\n")
    pkg.writelines("4\n")
    pkg.writelines("0\n")
    pkg.writelines("0\n")
    pkg.writelines("\n")
    pkg.writelines("COMMDISPLAY\n")
    pkg.writelines("0\n")
    pkg.writelines("\n")
    pkg.writelines("VERSATAP\n")
    pkg.writelines("0\n")


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
                    
                    
                package_string = str(package)
                    
                #with open(myfile,'w+') as pkg:
                pkg.writelines("SEND\n")
                pkg.writelines(str(i)+"\n")
                pkg.writelines("Package"+str(i)+"\n")
                pkg.writelines(package_string+"\n")
                pkg.writelines("0\n")
                pkg.writelines("5\n")
                pkg.writelines("\n")
        
                i=i+1
                j=0
                package.clear()


    #file.seek(2, 0)
    #file.write(b'\xFF')
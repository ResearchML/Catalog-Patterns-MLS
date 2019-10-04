import csv
import sys
import os
from subprocess import call

declarationFile = 'C:/Users/Administrator.WKS01/Desktop/Document These/Recherche/Practice/DeclarationsByClass.txt'

with open(declarationFile, 'rU') as f:
    freader = csv.reader(f, delimiter = '|', quoting=csv.QUOTE_NONE)
    count = 1
    auxPackageName = ""
    for row in freader:
        classString = row[1]
        declarations = row[0]
        start = classString.find("/classes")+9
        j = classString[start:]
        fullClass = classString[start:]
        className = fullClass[:fullClass.rfind(".", 0, len(fullClass))].replace("/",".")
        packageFullName = j[0:j.rfind("/", 0, len(j) + 1)].replace("/", ".")

        if(packageFullName == auxPackageName):
            count = count + 1
        else:
            auxPackageName = packageFullName
            print packageFullName, count
            count = 1;
        #print className+","+declarations

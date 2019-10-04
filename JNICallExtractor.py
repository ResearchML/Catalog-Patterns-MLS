import csv
import sys
import os
from subprocess import call

# declarationFile = 'C:/Users/Administrator.WKS01/Desktop/Document These/Recherche/Practice/JNIDeclarations.txt'
declarationFile = 'C:/Users/Administrator.WKS01/Desktop/Document These/Recherche/Practice/ListOfNativeMethods.txt'
methodCalls = set()

with open(declarationFile, 'rU') as f:
    freader = csv.reader(f, delimiter = ':', quoting=csv.QUOTE_NONE)
    for row in freader:
        classString = row[0]
        methodString = row[2]
        start = classString.find("/classes")+9
        fullClass = classString[start:]
        classFile = fullClass[fullClass.rfind("/", 0, len(fullClass)) + 1:]
        className = classFile[0:classFile.rfind(".", 0, len(classFile))]

        m = methodString[0:methodString.rfind("(", 0, len(methodString))]
        methodName = m[m.rfind(" ",0, len(m)):len(m)].strip()
        methodCalls.add(className + "." + methodName)

packages = {}
classes = {}
# methods = {}

PATH = 'C:/Users/Administrator.WKS01/Desktop/Document These/Recherche/JNI programs/jdk-473db5c4c2c9/jdk-473db5c4c2c9/src'
result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(PATH) for f in filenames if os.path.splitext(f)[1] == '.java']
for javaFile in result:
    if javaFile.find("\\classes") > -1:
        start = javaFile.find("\\classes") + 9
        j = javaFile[start:]
        className = j[0:j.rfind(".", 0, len(fullClass) + 1)].replace("\\", ".")
        packageFullName = j[0:j.rfind("\\", 0, len(fullClass) + 1)].replace("\\", ".")
        levels = packageFullName.split(".")

        cLevels = 0
        packageName = ""
        for level in levels:
            cLevels = cLevels + 1
            packageName = packageName + level + "."
            if cLevels == 2:
                break

        packageName = packageName[0:len(packageName)-1]
        print("Searching on " + className)

        with open(javaFile) as f:
            lines = f.readlines()
            for line in lines:
                for methodName in methodCalls:
                    if (line.find(methodName) > -1):
                        # if methods.has_key(methodName):
                        #     methods[methodName] = methods[methodName] + 1
                        # else:
                        #     methods[methodName] = 1

                         if classes.has_key(className):
                            classes[className] = classes[className] + 1
                         else:
                            classes[className] = 0

                         if packages.has_key(packageName):
                            packages[packageName] = packages[packageName] + 1
                         else:
                            packages[packageName] = 0

print("Result by Package")
for key in packages.keys():
    print("{0},{1}".format(key, packages.get(key)))

print("Result by classes")
for key in classes.keys():
 print("{0},{1}".format(key, classes.get(key)))

#
# print("Result by methods")
# for key in methods.keys():
#     print("{0},{1}".format(key, methods.get(key)))



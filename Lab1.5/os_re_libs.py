import os
import re

fileFolder = r'C:\Users\aa.seleznev\PycharmProjects\p4ne\Lab1.5\config_files\\'  # who doesn't adore MS?
findLine = 'ip address'

fileList = os.listdir(fileFolder)
fileExt = r".txt"
clListIP = []

for file in fileList:
    file = fileFolder + file
    if file.endswith(fileExt):
        with open(file) as f:
            for line in f.readlines():
                if re.match('^ip address (.*)', line):
                    clListIP.append(line.rstrip())

clListIP = list(set(clListIP))  # delete repeat items
for item in clListIP:
    print(item)

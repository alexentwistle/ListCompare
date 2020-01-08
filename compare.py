# Compares two csv files. Outputs items that are IN FILETWO but NOT IN FILEONE as 'update.csv'.

with open('old.csv', 'r') as t1, open('new.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
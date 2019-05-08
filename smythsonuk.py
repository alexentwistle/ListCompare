# Specific to Smythson UK.

# Compare two csv files. Find items that are IN FILETWO BUT NOT IN FILEONE.

with open('uksitemap.csv', 'r') as t1, open('ukspider.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('foundbyspiderbutnotinsitemap.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
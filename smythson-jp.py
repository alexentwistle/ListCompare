# Specific to Smythson UK.

# Compare two csv files. Find items that are IN FILETWO BUT NOT IN FILEONE.

with open('jp-sitemap.csv', 'r') as t1, open('jp-spider.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('jp-foundbyspiderbutnotinsitemap.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
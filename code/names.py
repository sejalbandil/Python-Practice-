names = list()
filename = open("input.txt")
outputfile= open("output1.txt", "a")
outputfile.truncate(0)
for line in sorted(filename, key = lambda line: line.split(",")[0]):
    outputfile.write (str(line))
    outputfile.write ("\n")

outputfile.close()

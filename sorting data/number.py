numbers = list()
filename = open("input.txt")
outputfile= open("output2.txt", "a")
outputfile.truncate(0)
for line in sorted(filename, key = lambda line: int(line.split(",")[1])):
    outputfile.write (str(line))
    outputfile.write ("\n")

outputfile.close()

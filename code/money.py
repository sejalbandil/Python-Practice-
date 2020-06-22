numbers = list()
filename = open("input.txt")
outputfile= open("output3.txt", "a")
outputfile.truncate(0)
for line in sorted(filename, key = lambda line: int(line.replace("$","").split(",")[2])):
    outputfile.write (str(line))
    outputfile.write ("\n")

outputfile.close()

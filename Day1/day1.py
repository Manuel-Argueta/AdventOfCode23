def getListOfNums(inputText):
    text = inputText
    numList = []
    validDigits = {"one": "1", "two": "2", "three":"3", "four": "4", "five": "5", "six":"6","seven": "7", "eight": "8", "nine":"9"}
    i = 0
    currentSubString = ""
    while (i < len(text)):
        currentSubString += text[i]
        if (currentSubString.isnumeric()):
            numList.append(currentSubString)
            text = text[i+1:]
            currentSubString = ""
            i = 0
        elif (currentSubString in validDigits):
            numList.append(validDigits[currentSubString])
            text = text[i:]
            currentSubString = ""
            i = 0
        elif (len(currentSubString) == len(text)):
            text = currentSubString[1:]
            currentSubString = ""
            i = 0
        else:
            i += 1
    return numList


def main():
    f = open("input.txt","r")
    totalValue = 0
    lineNum = 0
    for line in f:
        line = line.strip()
        listOfNums = getListOfNums(line)
        totalValue += int(listOfNums[0] + listOfNums[len(listOfNums)-1])
    print(totalValue)





if __name__ == "__main__":
    main()
def main():
    f = open("input.txt", "r")
    sumGames = 0
    for line in f:
        isValid = True
        line = line.strip()
        splitIdx = line.index(":")
        currentID = line[:splitIdx].split()[1]
        line = line[splitIdx+2:]
        allSets = line.split(';')
        minBlue, minRed, minGreen = 0, 0, 0
        for currSet in allSets:
            allDraws = currSet.split(',')
            for draw in allDraws:
                currDraw = draw.split()
                currDice, currColor = int(currDraw[0]), currDraw[1]
                if currColor == 'blue':
                    minBlue = max(minBlue,currDice)
                elif currColor == 'green':
                    minGreen = max(minGreen,currDice)
                else: 
                    minRed = max(minRed,currDice)
        sumGames += (minRed * minGreen * minBlue)
    print(sumGames)




if __name__ == "__main__":
    main()
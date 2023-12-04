def main():
    f = open("input.txt","r")
    cardNumber = 1
    allCards, allScratchers = {}, {}
    total = 0
    for line in f:
        allCards[cardNumber] = 0
        line = line.strip()
        startIndex = line.index(":")
        newLine = line[startIndex+2:].split("|")
        winningList = newLine[0].split()
        numList = newLine[1].split()
        for winNum in winningList:
            for i in range(len(numList)):
                if winNum == numList[i]:
                    allCards[cardNumber] += 1
        cardNumber += 1

    for card in allCards:
        allScratchers[card] = 0

    for card in allCards:
        find_scratchers(allCards, card, allScratchers)

    for card in allScratchers:
        total += allScratchers[card]
    print(total)

def find_scratchers(allCards, card, allScratchers):
    allScratchers[card] += 1
    if allCards[card] == 0:
        return
    for i in range(1, allCards[card] + 1):
        find_scratchers(allCards, card + i, allScratchers)
    
    #PART 1 SOLUTION
    # f = open("input.txt","r")
    # totalValue = 0
    # for line in f:
    #     line = line.strip()
    #     cardValue = 0
    #     startIndex = line.index(":")
    #     newLine = line[startIndex+2:].split("|")
    #     winningList = newLine[0].split()
    #     numList = newLine[1].split()
    #     print(winningList , numList)
    #     for winNum in winningList:
    #         for i in range(len(numList)):
    #             if winNum == numList[i]:
    #                 if cardValue == 0:
    #                     cardValue = 1
    #                 else: 
    #                     cardValue *= 2
    #     totalValue += cardValue
    #     print(cardValue)
    # print(totalValue)


if __name__ == "__main__":
    main() 
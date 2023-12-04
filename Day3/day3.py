def main():
    boardHeight = 0
    boardWidth = 0
    board = []
    allNums = []
    allGears = []
    f = open("input.txt", "r")
    sum = 0
    for line in f:
        line = line.strip()
        board.append(list(line))
        currNum = ""
        xyPos = []
        idx = 0
        while idx != len(line):
            if (line[idx].isdigit()):
                currNum += line[idx]
                xyPos.append([idx, boardHeight])
            else: 
                if currNum != "":
                    allNums.append({currNum : xyPos})
                    currNum = ""
                    xyPos = []
                if line[idx] == "*":
                    allGears.append([idx, boardHeight])
            idx += 1
            if idx == len(line) and currNum != "":
                allNums.append({currNum : xyPos})
        boardHeight += 1
    boardWidth = boardHeight
    for gear in allGears:
        currNums = []
        possNums = [[gear[0] + 1, gear[1]],
            [gear[0] + 1, gear[1] - 1],
            [gear[0] + 1, gear[1] + 1],
            [gear[0] - 1, gear[1] - 1],
            [gear[0] - 1, gear[1] + 1],
            [gear[0] - 1, gear[1]],
            [gear[0], gear[1] + 1],
            [gear[0], gear[1] - 1]] 
        for newNum in possNums:
            if newNum[0] in range(boardWidth) and newNum[1] in range(boardHeight):
                    for num in allNums:
                        for key in num:
                            validIndexes = num[key]
                            if newNum in validIndexes:
                                if key not in currNums:
                                   currNums.append(key)
        if (len(currNums) == 2):
            sum += int(currNums[0]) * int(currNums[1])
    print(sum)
 
    # PART 1 SOLUTION
    # boardHeight = 0
    # boardWidth = 0
    # board = []
    # allNums = []
    # f = open("input.txt", "r")
    # sum = 0
    # for line in f:
    #     line = line.strip()
    #     boardWidth = len(list(line))
    #     board.append(list(line))
    #     currNum = ""
    #     xyPos = []
    #     idx = 0
    #     while idx != len(line):
    #         if (line[idx].isdigit()):
    #             currNum += line[idx]
    #             xyPos.append([idx, boardHeight])
    #         else: 
    #             if currNum != "":
    #                 allNums.append({currNum : xyPos})
    #                 currNum = ""
    #                 xyPos = []
    #         idx += 1
    #         if idx == len(line) and currNum != "":
    #             allNums.append({currNum : xyPos})
    #     boardHeight += 1

    # for num in allNums:
    #     allNeigh = set()
    #     for key in num:
    #         for neigh in num[key]:
    #             possNeighs = [[neigh[0] + 1, neigh[1]],
    #                         [neigh[0] + 1, neigh[1] - 1],
    #                         [neigh[0] + 1, neigh[1] + 1],
    #                         [neigh[0] - 1, neigh[1] - 1],
    #                         [neigh[0] - 1, neigh[1] + 1],
    #                         [neigh[0] - 1, neigh[1]],
    #                         [neigh[0], neigh[1] + 1],
    #                         [neigh[0], neigh[1] - 1]] 
    #             for possNeigh in possNeighs:
    #                 if possNeigh[0] in range(boardWidth) and possNeigh[1] in range(boardHeight):
    #                     if not board[possNeigh[1]][possNeigh[0]].isdigit():
    #                         allNeigh.add(board[possNeigh[1]][possNeigh[0]])
    #         if (len(allNeigh)) > 1:
    #             sum += int(key)
    # print(sum)                    

if __name__ == "__main__":
    main() 
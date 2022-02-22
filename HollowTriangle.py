def hollow_triangle(n):
    firstFloor = 1
    length = int(2*n-1)
    finalResult = 0
    resultToPrint = [] 
    spaceInBetween = 1
    for x in range(n):
        spaceBetweeen = int((length - firstFloor)/2)
        if x < 1:
            finalResult = "_"*spaceBetweeen + "#"*firstFloor + "_"*spaceBetweeen
        elif x + 1 < n:
            finalResult = "_"*spaceBetweeen + "#"*1+"_"*spaceInBetween+"#"*1 + "_"*spaceBetweeen
            spaceInBetween += 2
        else:
            finalResult = "#"*length
        firstFloor +=2
        resultToPrint.append(finalResult)
    return resultToPrint
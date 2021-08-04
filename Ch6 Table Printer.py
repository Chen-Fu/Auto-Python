tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)   
    width = len(tableData)
    length = len(tableData[0])

    #determine column width
    for i in range(width):
        for j in range(length):
            colWidths[i] = max(colWidths[i],len(tableData[i][j]))

    #print results
    for j in range(length):
        for i in range(width):
            if i == width-1:
                print(tableData[i][j].rjust(colWidths[i]))
            else:
                print(tableData[i][j].rjust(colWidths[i]),end = ' ')

printTable(tableData)

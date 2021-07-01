#Character Picture Grid
#Copy the following grid value, and write code that uses it to print the image.
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]  # 9 x 6

#print a 6 x 9 string

width = len(grid[0]) #6
height = len(grid) #9

for j in range(width):
    for i in range(height-1):
        print(grid[i][j],end = '')
    print(grid[height-1][j])


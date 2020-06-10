def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print(arr[i][j]), 
        print('\n')
    print('\n')
def check_rule_row(grid,row,col,i):
	for j in grid[row]:
		if j==i:
			return False
	return True

def check_rule_col(grid,row,col,i):
	for j in range(0,len(grid)):
		if grid[j][col] == i:
			return False
	return True

def check_rule_box(grid,row,col,num):
	x = row - row%3
	y = col - col%3
	for i in range(x,x+3):
		for j in range(y,y+3):
			if grid[i][j] == num:
				return False
	return True

def empty_location(grid,pos):
	for i in range(0,9):
		for j in range(0,9):
			if grid[i][j]==0:
				pos[0] = i
				pos[1] = j
				return True
	return False
def sudoku(grid,m):
    m = m+1
    pos = [0,0]
    row = pos[0]
    col = pos[1]
    if not empty_location(grid,pos):
            print(m)
    if not empty_location(grid,pos):
    	return True
    row = pos[0]
    col = pos[1]
    #print(row)
    #print(col)
    for i in range(1,10):            
    	if check_rule_row(grid,row,col,i) and check_rule_col(grid,row,col,i) and check_rule_box(grid,row,col,i):
    		grid[row][col] = i
    		m = m+1
    		if sudoku(grid,m):
    			return True
    		grid[row][col] = 0
    		m = m+1
    	#print("!")
    return False
if __name__=="__main__": 
      
    grid =[[0 for x in range(9)]for y in range(9)] 
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    m = 0
    if(sudoku(grid,m)): 
        print_grid(grid)
        #print(m)
    else: 
        print("No solution exists")


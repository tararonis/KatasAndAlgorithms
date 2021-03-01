#https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/train/python

#board[i][j]
def done_or_not(sudoku_board):
    #check the rows
    for row in sudoku_board:
        nums_in_row = set()
        for dig in row:
            if dig in nums_in_row:
                print('{} in row {}'.format(dig, row))
                return 'Try again!'
            nums_in_row.add(dig)
    #check the columns
    for column_ind in range(len(sudoku_board)):
        dig_in_row = set(["test"])
        for digit_ind in range(len(sudoku_board)):
            if sudoku_board[column_ind][digit_ind] in dig_in_row:                             
                return 'Try again!'
            dig_in_row.add(str(sudoku_board[column_ind][digit_ind]))
    #check the regions
    for cnt_of_regions_lines in range(len(sudoku_board)/3):
        for regions in range(3):
            for row in sudoku_board[cnt_of_regions_lines*3+regions]



        
    

    
    #if all ok - return Finished!
    return 'Finished!'



print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))
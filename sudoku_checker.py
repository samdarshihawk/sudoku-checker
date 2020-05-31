def check_sudoku(my_sudoku):
    max_num=len(my_sudoku)
    check_list = list(range(1,max_num+1))
    #to check the number of sudoku within nxn
    if type(my_sudoku[0][0])==int:
        pass
    else:
        return(False)
# check the range of the number
    for i in my_sudoku:
        for num in i:
            if num not in check_list:
                return(False)
            else:
                pass
# check occurence of number row-wise
    for z in my_sudoku:
        for e in z:
            if z.count(e) > 1:
                return(False)
            else:
                pass
# check occurence of number column-wise
    for g in range(max_num):
        column = []
        for z in range(max_num):
            column.append(my_sudoku[z][g])
        for i in column:
            if column.count(i) >  1:
                return(False)
            else:
                pass
    
    return(True)
        
            

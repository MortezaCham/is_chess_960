def is_chess_960(row):
    lst = list(row)
    index_b = []
    index_r = []

    for indx , value in enumerate(lst):
        if value == 'b':
            index_b.append(indx)
        if value == 'r':
            index_r.append(indx)
            
    result = (index_b[1] - index_b[0]) % 2
    
    if result != 0 and index_r[0] < lst.index('K') < index_r[1]:
        return True
    else:
        return False
    



    

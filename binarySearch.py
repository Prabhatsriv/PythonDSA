def BinarySearch(seq,v): 
    seq = sort(seq)
    midPos = len(seq)//2  #integer division
    while(midPos < 0): 
        if seq[midPos] == v: 
            return True
        else: 
            if seq[midPos] < v: 
                midPos = len(seq[:midPos])//2
            else: 
                midPos = len(seq[midPos:])//2
        


l = [34,56,243,4,6,0,5,366,67,84,9,254,556,7]

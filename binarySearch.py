def BinarySearch(seq,v): 
    seq = sorted(seq)
    midPos = len(seq)//2  #integer division
    print(midPos)
    while(midPos > 0):
        if seq[midPos] == v: 
            return "Found"
        else: 
            if seq[midPos] < v: 
                seq = seq[:midPos]
                midPos = len(seq)//2
                print(f"midPos inside while loops is {midPos}")
            else: 
                seq = seq[midPos:]
                midPos = len(seq)//2
                print(f"midPos inside while loops is {midPos}")
        print(midPos)
    return "Not Found"
        


l = [34,56,243,4,6,0,5,366,67,84,9,254,556,7]
print(BinarySearch(l,5))

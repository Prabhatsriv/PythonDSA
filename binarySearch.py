def BinarySearch(seq, v):
    seq = sorted(seq)
    midPos = len(seq) // 2  # integer division
    print(midPos)
    while midPos > 0:
        if seq[midPos] == v:
            return "Found in the List"
        else:
            if seq[midPos] < v:
                seq = seq[:midPos]
                midPos = len(seq) // 2
                print(f"midPos inside while loops is {midPos}")
            else:
                seq = seq[midPos:]
                midPos = len(seq) // 2
                print(f"midPos inside while loops is {midPos}")
        if seq[midPos] == v:
            return "Found in the list"
        print(midPos)
    return "Not Found and this one should go to Feature001"


l = [34, 56, 243, 4, 6, 0, 5, 366, 67, 84, 9, 254, 556, 7]
print(BinarySearch(l, 5))

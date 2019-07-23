def pawn(arr):
    no_jumps =0
    i=0
    while i < (len(arr)) and i > -1:
        value = arr[i]
        if value:
            arr[i]=0
            no_jumps +=1
            i+= value
        else:
            return -1
    return no_jumps


print(pawn([2,3,-1,1,3]))#4
print(pawn([1,-1,1,1]))#-1
print(pawn([1,1,1,1,1,1,1,1,1,1,2,0,-2]))#-1
print(pawn([1,2,3,1,0]))#-1
print(pawn([5,4,2,1]))#1
print(pawn([-1,3,2,5,4,1]))#1
print(pawn([1]*100000))#100000

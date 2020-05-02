count = 0
def TowerOfHanoi(n , source, destination, auxilliary):
    global count
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    count += 1
    TowerOfHanoi(n-1, source, auxilliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    count += 1
    TowerOfHanoi(n-1, auxilliary, destination, source)

TowerOfHanoi(4, 'A', 'B', 'C')
print("--------------------")
print("Count: ", count + 1)
def onsqrtime(n):
    iteration=0
    for i in range (0,n):
        for j in range (0,n):
            print("*", end="")
            iteration+=1
        print("")    
    print("/n when is : ", n,"iteration is :",iteration)
onsqrtime(4)
onsqrtime(5)
onsqrtime(6)            
            
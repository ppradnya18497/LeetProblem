List=[2,7,8,5]
target=9
newlist=[]
for i in range(len(List)):
    for p in range(i+1,len(List)):
        if List[i]+List[p] == target:
            print(List[i],List[p])
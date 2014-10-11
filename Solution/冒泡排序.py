def bubble(bubbleList):
    listLength=len(bubbleList)
    while listLength>0:
        for i in range(listLength-1):
            if bubbleList[i]>bubbleList[i+1]:
                bubbleList[i],bubbleList[i+1] = bubbleList[i+1], bubbleList[i]
        listLength-=1
    return bubbleList
    
lst = [1,3,4,56,3,2,5,6,8,9]
print(bubble(lst))
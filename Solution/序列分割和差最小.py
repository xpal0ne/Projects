lst1 = [2,2,3,5,6,7,8,98,9,0,32,4]
lst2 = [4,45,6,6,7,8,8,9,0,0,0,98,7,6,45,43,3,99]
new_lst = lst1 +lst2
max_lst = []
min_lst = []

while len(new_lst) > 1:
    max_number = max(new_lst)
    min_number = min(new_lst)
    if sum(min_lst)+max_number+min_number < sum(max_lst):
        min_lst.append(min_number)
        min_lst.append(max_number)
    else:
        max_lst.append(min_number)
        min_lst.append(max_number)
    new_lst.remove(max_number)
    new_lst.remove(min_number)
    if len(new_lst) == 1:
        if sum(max_lst)+new_lst[0] - sum(min_lst) >  sum(max_lst)-new_lst[0] - sum(min_lst):
            min_lst.extend(new_lst)
        else:
            max_lst.extend(new_lst)
    if sum(max_lst) < sum(min_lst):
         max_lst, min_lst = min_lst, max_lst 
         
print(sum(max_lst), max_lst)
print(sum(min_lst), min_lst)
    

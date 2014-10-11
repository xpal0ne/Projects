ff = open(r'D:\a\test.txt')
content = ff.read()
lst = content.split()
d_lst = {}
for i in set(lst):
    num = lst.count(i)
    d_lst[i] = num
new_d = sorted(d_lst.items(), key = lambda d: d[1], reverse = True)
print ('Rank', 'Str    ','Num')
for i,j in enumerate(new_d):
    if i <10:
        print (str(i+1)+'   ',j[0],j[1])
ff.close()
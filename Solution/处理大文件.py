buffsize = 10
bigfile = open('test.txt')
allfile = []

i = 0
while True:
    filepart = bigfile.readlines(buffsize)      
    if not filepart: break    
    with open('Filepart%d .txt' % i, 'w') as tempfile:
        tempfile.writelines(filepart)
        allfile.append('Filepart%d .txt' % int(i))
        i += 1
      
allst = [chr(x) for x in range(97,123)]

for i in allfile:
    with open(i) as files:
        for eachline in files.readlines():
            for i in allst:
                if eachline.lower().startswith(i):
                    with open('%s.txt'% i, 'a') as filehandler:
                        filehandler.write(eachline)
                

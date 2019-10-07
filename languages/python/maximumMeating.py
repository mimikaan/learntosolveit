'''Here s is a list that contains the starting time of the meating and f contains the finishing time of the meating
  We are creating a function so that maximum meatings could be organized'''
def sort_tup(tup):
    lst = len(tup)
    for i in range(0,lst):
        for j in range(0,lst-i-1):
            if (tup[j][1]>tup[j+1][1]):
                tup[j][1],tup[j+1][1] = tup[j+1][1],tup[j][1]
    return tup
s=[1,3,0,5,8,5]
f=[2,4,6,7,9,9]
result = zip(s,f)
result = sort_tup(result)
last_finish = 0
for i in result:
    if i[0] >= last_finish:
        print(i)
        last_finish = i[1]


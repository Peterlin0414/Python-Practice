n = eval(input())

#n:表示要印幾列
for j in range(n):
    #j:表示現在印到第幾列=0~4
    #n-j:現在這列印幾個*號=5~1
    for i in range(n-j):
        #i:現在印到第幾個*號
        print('*',end='')
    print()

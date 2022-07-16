from random import random
from time import perf_counter

def calPI(N = 100):
    print(N)
    hits = 0
    start = perf_counter()
    for i in range(1, N*N+1):
        #print(N)
        print("已计算{}次".format(i))
        x, y = random(), random()
        #print(N)
        dist = pow(x ** 2 + y ** 2, 0.5)
        #print(N)
        if dist <= 1.0:
            print(N)
            hits += 1
    pi = (hits * 4) / (N * N)
    use_time = perf_counter() - start
    return pi, use_time
c = int(input("测试多少次（测试一次需运行0.0003665999975055456秒）:"))
#print(c)
PI, use_time = calPI(c)
print('计算得出的pai为: {}'.format(PI))
print('用时: {} 秒'.format(use_time))






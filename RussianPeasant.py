#Programming project #1
#Comparing Exponentiation Algorithms

import timeit

test_code_1 = """
def naive_exponentiation(a,b):
    tot = 1
    for i in range (b):
        tot = tot*a

    return tot,b
naive_exponentiation(5,0)
"""

test_code_2="""
def russian_Peasant(a,b):
    if (b == 0):
        return 1
    temp,count = 1,0
    while b > 1: 
        count+=1
        if (b%2==0):
            a = a * a
            b = b/2
        else:
            temp = temp * a
            a = a * a
            b = b//2
    return temp * a,count
russian_Peasant(5,0)
"""
test_code_3 = """
def russian_Peasant_Recursive(a,b):
    if(b==0):
        return 1
    if(b%2==0):
        return russian_Peasant_Recursive(a*a,b/2)
    else:
        return a*russian_Peasant_Recursive(a*a,b//2)
russian_Peasant_Recursive(5,0)
"""

elapsed_time1 = timeit.timeit(test_code_1, number=100)/100
elapsed_time2 = timeit.timeit(test_code_2, number=100)/100
elapsed_time3 = timeit.timeit(test_code_3, number=100)/100

print(elapsed_time1)
print(elapsed_time2)
print(elapsed_time3)
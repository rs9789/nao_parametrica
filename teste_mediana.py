import math

a = [80, 94, 92, 70, 78, 83, 90, 88, 87, 90, 89, 91]
b = [63, 57, 71, 82, 70, 61, 85, 66, 72, 66]

def median_test(a, b):
    comb_list = a + b
    comb_list.sort()
    if len(comb_list) % 2 == 0:
        center = int(len(comb_list)/2)
        median = ((comb_list[center-1])+(comb_list[center]))/2
    else:
        median = comb_list[int((len(comb_list)+1)/2)-1]

    A = len([x for x in a if x > median])
    B = len([x for x in b if x > median])
    C = len([x for x in a if x <= median])
    D = len([x for x in b if x <= median])

    result = round(math.comb(A+C, A)*math.comb(B+D, B)/math.comb(A+B+C+D, A+B), 4)
    print(result)

median_test(a,b)

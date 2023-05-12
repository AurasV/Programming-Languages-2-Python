from multipledispatch import dispatch

"Create a function named “calculate” which must be overloaded with decorators:"


"""
Next call “calculate(list, list)” must return “first” if first list elements sum 
is max, return “second” if second list elements sum is max, or return “equal” if 
results are equal. 
"""
@dispatch(list, list)
def calculate(list_a, list_b):
    if sum(list_a) > sum(list_b):
        return "First"
    elif sum(list_a) < sum(list_b):
        return "Second"
    else:
        return "Equal"


"""
Next call “calculate(list, int)” must return number of elements from list which 
are greater or equal than int parameter.
"""
@dispatch(list, int)
def calculate(list_c, int_d):
    nr = 0
    for i in list_c:
        if i >= int_d:
            nr += 1
    return nr


"""
Next call “calculate(int, list)” must return number of elements from list which 
are lower or equal than int parameter.
"""
@dispatch(int, list)
def calculate(int_e, list_f):
    nr = 0
    for i in list_f:
        if i <= int_e:
            nr += 1
    return nr


"""
Next call “calculate(list)” must return a tuple with min and max element in list. 
If list is empty, then  return “empty”.
"""
@dispatch(list)
def calculate(list_g):
    try:
        min = list_g[0]
        max = list_g[0]
        for i in list_g:
            if min > i:
                min = i
            if max < i:
                max = i
        return min, max
    except IndexError:
        return "Empty"


"""
Next call “calculate(list,list,int A,int B)” return “yes” if max-min from range(A,B) 
from first list is greater or equal than max-min from range(A,B) from second list, 
or return “no” if it is lower. If A or B are not in lists range, raise a message 
with this error (A and B represent starting index and ending index for both lists). 
Example: calculate([1,2,3,4,5,6],[2,4,2,2,2],1,3) must return “yes”.
"""
@dispatch(list, list, int, int)
def calculate(list_h, list_i, int_j, int_k):
    try:
        max_1 = max(list_h[int_j:int_k + 1])
        min_1 = min(list_h[int_j:int_k + 1])
        max_2 = max(list_i[int_j:int_k + 1])
        min_2 = min(list_i[int_j:int_k + 1])
        if (max_1 - min_1) >= (max_2 - min_2):
            return "Yes"
        else:
            return "No"
    except ValueError:
        return "Out of range!"


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [2, 3, 4, 9]
    d = []
    c = 2
    test1 = [1, 2, 3, 4, 5, 6]
    test2 = [2, 4, 2, 2, 2]
    #print("Greater List Sum: " + calculate(a, b))
    #print("Number of Elements greater or equal: " + str(calculate(a, c)))
    #print("Number of Elements smaller or equal: " + str(calculate(c, a)))
    #print("Max and Min in List: " + str(calculate(a)))
    print("Greater Max - Min?: " + calculate(test1, test2, 1, 3))

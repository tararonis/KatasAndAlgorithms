#https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(arr):   
    for i in range(len(arr)):        
        if sum(arr[0:i]) == sum(arr[i+1:len(arr)]):
            return i   
    return -1       


print(find_even_index([1,2,3,4,3,2,1]))
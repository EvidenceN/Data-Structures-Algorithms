# My initial reaction to the question (Might be wrong, we will see)
# find the maximum value in list 1
# Find the maximum value in list 2
# Or...if it's a single list, find the 2 highest values and multiple them together. 
# Multiply them together

# Solution so far

# Sort in descending order
# Get the first 2 values
# Multiply them together

def max_pairwise(number:list):
    number.sort(reverse = True)
    return number[0] * number[1] 

#print(max_pairwise([1,2,3, 16, 56, 89, 78, 61, 45]))
if __name__ == '__main__':
    _ = int(input())
    input_value = list(map(int, input().split()))  
    #print(input_value)
    print(max_pairwise(input_value))
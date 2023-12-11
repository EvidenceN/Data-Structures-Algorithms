# My Naive first impression algorithm on how to solve it. 

# Find the minimum value between a and b.

# See if Largest value is divisible by smallest value without a fraction. If yes, then that’s the GCD. If no, then find the number 1 smaller than previous number and see if it can do the division on both without fraction, then next smallest, and next smallest.

def fraction(a:int, b:int):
    smallest_value = min(a, b)
    first_division = a/smallest_value
    print(first_division)
    print(type(first_division))
    second_division = b//smallest_value
    print(second_division)
    print(type(second_division))
    if type(first_division) != float and type(second_division) != float:
        return smallest_value
    else:
        pass

if __name__ == '__main__':
    a = 10
    b = 4
    fraction(a, b)
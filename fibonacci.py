# The premise of the project is that the value is the sum of the last 2 values. 
# with the first 2 digits always 0,1
# So, fibonacci value of 100 will have 100 digits, and the last digit will be the sum of the previous 2 digits
# Let's code it up. 

def fibonacci(input_value:int) -> int :
    # value_list = [0, 1]
    # if len(value_list) <= 2:
    #     final_value = value_list[-1]
    # else:
    #     for i in range(1, input_value):
    #         value_list.append(value_list[-1] + value_list[-2])

    value_list = [0,1]
    if input_value == 0:
        return input_value
    elif input_value == 1:
        return input_value
    else:
        for i in range(1,input_value): # The first 2 values is already present. I need to calculate the next 98. Which will be 99-1. With Python Range, input_value of 100 will result in 99 iterations. So, 99-1 = 98
            value_list.append(value_list[-1] + value_list[-2])        

    return value_list[-1]   

# re-write the code to be
# if value of input = 0 then return 0 ; if = 1 then return 1 ; else 

print(fibonacci(6000))


# not_list = [1,2,3,4]
# testing = not_list,
# print(type(testing))        
# print(testing) 
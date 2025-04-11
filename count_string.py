import time

#interim_variable = [1 for char_variable in string if char_variable.isalnum()]
#total = sum(interim_variable)
#print(total)


#letters = sum(1 for char in string)
#print(f"The number of letters in the string is: {letters}")
def len_using_lists(string):
    t_list = [1 for char in string if char.isalnum()]
    return sum(t_list)

def len_using_len(string):
    t_sum = len(string)
    s_sum = string.count(' ')
    return (t_sum - s_sum)

def len_using_replace(string):
    str2 = string.replace(' ','')
    return len(str2)

methods = [len_using_lists, len_using_len, len_using_replace]

def get_input_and_calc_len():
    string = input("Please enter a string: ")
    for i in range(3):
        start = time.perf_counter()
        print(f"The length of \'{string}\' is: {methods[i](string)}")
        end = time.perf_counter()
        print(f"time took by {methods[i].__name__} = {end-start:.6f}")

get_input_and_calc_len()        



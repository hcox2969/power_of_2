# check if an number is a power of 2 or not in a given list:

import math

input_list = [2, 4, 6, 4, 100, 31]
output_list = []

x = 4
def check_log2(x):
    return(math.log10(x)/math.log10(2));

def check_power2(x):
    print('-----')
    print('Checking if input number {} is power of 2'.format(x))

# check base
    check_output = (math.ceil(check_log2(x)) == math.floor(check_log2(x)))

    output_list.append(bool(check_output))

    if check_output:
        print('The number {} is power of 2!'. format(x))

    else:
        print('Number {} is NOT power of 2'. format(x))

    return check_output



#Run a loop on my input list to check power of 2 for x in input_list:

check_power2(x)

output_dict = {'input': input_list,
'Is_Power_2_check': output_list}

output_dict

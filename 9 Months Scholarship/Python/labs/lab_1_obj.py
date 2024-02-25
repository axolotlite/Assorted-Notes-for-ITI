vowels = ['a','e','i','o','u']
# This is lab 1
def problem_1(string):
    """Write a program that counts up the number of vowels [a, e, i, o,u] contained in the string."""
    total_count=0
    for ch in vowels:
        total_count+=string.count(ch)
    return total_count
def problem_2(array):
    """Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output."""
    #array=[0,0,0,0,0]
    #for i in range(5):
    #    array[i] = input(f"{i}> ")
    #ascending
    array.sort()
    print(f"Ascending Order: {array}")
    #descending, reversing the string should be faster than resorting it
#    array.sort(reverse=True)
    print(f"Descending Order: {array[::-1]}")
def problem_3(string):
    """Write a program that prints the number of times the string 'iti' occurs in anystring."""
    return(string.count('iti'))
def problem_4(string):
    """Write a program that remove all vowels from the input word and generate a brief version of it."""
    for ch in vowels:
        string = string.replace(ch,"")
    return string
def problem_5(string):
    """Write a program that prints the locations of "i" character in any string you added."""
    loc_array=[]
    for idx,ch in enumerate(string):
        print(ch)
        if ch == 'i':
            loc_array.append(idx)
    return loc_array
def problem_6(num):
    """Write a program that generate a multiplication table from 1 to the number passed."""
    num = int(num)
    mult_array=[]
    for i in range(1,num):
        for j in range(1,num):
            mult_array.append([i,j,i*j])
#            print(f"{i}*{j} = {i*j}")
    return(mult_array)
def problem_7(num):
    """Write a program that build a Mario pyramid with a given height"""
    num = int(num)
    ind = num - 1
    string=""
    while(ind+1):
        print(ind*" " + (num - ind)*"*")
        ind-=1
    return("")
#print(problem_5("iti is iti and iti was iti and i am iti and you are iti"))
#print(problem_6(4))
#problem_2()
problems = {
    1:
    {"desc": "Write a program that counts up the number of vowels [a, e, i, o,u] contained in the string.","call":problem_1,"inp":"input a string containing vowels"},
    2:
    {"desc": "Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.","call":problem_2,"inp":"input 5 strings"},
    3:
    {"desc":"Write a program that prints the number of times the string 'iti' occurs in anystring.","call":problem_3,"inp":"input a string containing 'iti'"},
    4:
    {"desc": "Write a program that remove all vowels from the input word and generate a brief version of it.","call":problem_4,"inp":"input a string"},
    5:
    {"desc": "Write a program that prints the locations of 'i' character in any string you added.","call":problem_5,"inp":"input a string"},
    6:
    {"desc": "Write a program that generate a multiplication table from 1 to the number passed.","call":problem_6,"inp":"input a number"},
    7:
    {"desc": "Write a program that build a Mario pyramid ","call":problem_7,"inp":"input the height of the pyramid"},
        }


from labs import *
selected_lab = None
def greet():
    filename=__file__.split("/")[-1]
    greeting=f"This is an interactive lab runner\nwrite h, to see a list of available commands:"
    print(greeting)
def help():
    help_string = """
    These are the available inputs:
    l)oad a lab
    s)how available problems in a lab
    r)un a problem
    """
    print(help_string)

def load(num):
    global selected_lab
    if num == []:
        num = input("lab number > ")
    else:
        num = num[0]
    match num:
        case "1":
            selected_lab = lab_1
        case "2":
            print("lab doesn't exist yet")
        case "3":
            print("lab doesn't exist yet")
        case "4":
            print("lab doesn't exist yet")
        case "5":
            print("lab doesn't exist yet")
        case "6":
            print("lab doesn't exist yet")
        case "7":
            print("lab doesn't exist yet")
        case _:
            print("lab doesn't exist")
    print(f"There are {len(selected_lab.problems)} problems in this lab, use (s) to see them")
def show_labs():
    problems = selected_lab.problems
    for lab in problems:
        print(f"{lab}: {problems[lab]['desc']}")
def run_lab(num):
    if num == []:
        num = input("lab number > ")
    else:
        num = num[0]
    num = int(num)
    problem = selected_lab.problems[num]
    print(f"{problem['desc']}\n{problem['inp']}")
    if num == 5:
        array = [0,0,0,0,0]
        for i in range(5):
            array[i] = input(f"{i} >> ")
        params = array
    else:
        params = input("input>> ")
    print(problem["call"](params))
def interactive():
    greet()
    #placeholder
    while(True):
#        print("@>> ",end="")
        user_input=input("@>> ").split()
        func, params = user_input[0],user_input[1:]
#        print(func,params)
#        exit(0)
        match func:
            case "e" | "q" | "exit" | "quit":
                print("exiting...")
                exit(0)
            case "h" | "help":
                help()
            case "l":
                load(params)
            case "s":
               show_labs()
            case "r":
                run_lab(params)
#selected_lab = lab_1
#print(selected_lab.problems)
interactive()
#lab_1.problem_1("Hello")

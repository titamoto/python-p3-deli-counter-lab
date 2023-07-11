katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        index = 0
        num_and_name_list = []
        while index < len(katz_deli):
            num_and_name_list.append(str(index+1) + f". {katz_deli[index]}")
            index += 1
        print("The line is currently: " + " ".join(num_and_name_list))

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
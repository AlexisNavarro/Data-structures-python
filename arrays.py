def add(names):
    print("\nin the add method")

    position = int(input("Select what position to add a name "))
    name = input("Select what name you want to add ")

    size = len(names) + 1
    new_arr = []*size 
    holder = ""

    count = 0

    #add at the beginning of the list
    if position == 0:      
        for i in range(1):
            new_arr.append(name)
        for items in names:
            new_arr.append(items)
        print(new_arr)
    
    #add anywhere at the list based on the index. Avoided using the insert function.
    else:
        for i in range(size):
            if i != position:
                new_arr.append(names[count])
                count+=1
            else:
                new_arr.append(name)
            print(new_arr)
        

def remove(names):
    print("in the remove method")

    position = int(input("Select what position to remove a name "))
 
    names.pop(position)

    #verify that a pop and the index adjustment has been done.
    for i in range(len(names)):
        print("index:", i, "name", names[i])



def single_array():
    print("\ninside single array")

    names = ["John","Alexis","Jose"]

    loop_type = input("1.in range loop\n2. i in names loop ")

    if int(loop_type) == 1:
        for i in range(len(names)):
            print(names[i])
    elif int(loop_type) == 2:
        for i in names:
            print(i)

    user_in = input("1. add elements to the array\n2. remove elements from the array ")

    match int(user_in):
        case 1:
            add(names)
        case 2:
            remove(names)



def double_array():
    print("inside double array")

def main():
    user_in = input("1. for singly array list\n2. for doubly array list ")

    match int(user_in):
        case 1:
            single_array()
        case 2:
            double_array()




if __name__ == '__main__':
    main()

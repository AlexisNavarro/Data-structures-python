#This implementation of arrays, I will be focusing on 1-D and 2-D arrays, but I will NOT be using the numpy library
#since I want to demonstrate my knowledge in arrays

#method to add values to a 1-D array
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
        
#method to remove values of a 1-D array
def remove(names):
    print("in the remove method")

    position = int(input("Select what position to remove a name "))
 
    names.pop(position)

    #verify that a pop and the index adjustment has been done.
    for i in range(len(names)):
        print("index:", i, "name", names[i])


#method that creates a 1-D array with different implementations
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


#method that creates a 2-D array with different implementations
def double_array():
    print("inside double array")

    rows = 5
    cols = 5
    double_arr=[]

    population_type = int(input("1. in range loop\n2. easy population "))
    
    if population_type == 1:
    #using a for loop to create a 2d array of 0's
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(0)
            double_arr.append(col)
        print(double_arr)

    elif population_type == 2: 
        double_arr = [[0]*cols]*rows
        
        for row in double_arr:
            print(row)


    user_in = input("1. add elements to the array\n2. remove elements from the array ")
    match int(user_in):
        case 1:
            add_double(double_arr)
        case 2:
            remove_double(double_arr)
    
def add_double(double_arr):
    print("in double add method")

    number = int(input("please insert a number to add to the array: "))
    row = int(input("please insert a row index: "))
    cols = int(input("please insert a column index: "))

    for i in range(len(double_arr)):
        for j in range(len(double_arr[i])):
            if row == i and cols == j:
                print("found the position!")
                double_arr[i][j] = number
    
    for i in double_arr:
        for item in i:
             print(item, end = " ")

#remove method to remove a value of a 2-D array. Can't really remove a value in a collection of arrays, USING NONE TO INDICICATE REMOVAL
def remove_double(double_arr):
    print("inside the remove for 2-D array method")
    row = int(input("please insert a row index: "))
    cols = int(input("please insert a column index: "))

    for i in range(len(double_arr)):
        for j in range(len(double_arr[i])):
            if row == i and cols == j:
                print("found the position!")
                double_arr[i][j] = None

    col = 0
    for row in double_arr:
            print(row)
    '''
    for i in double_arr:
            for item in i:
                print("column: ",col," row ", item, end = " ")
                count +=1
    '''


def main():
    user_in = input("1. for singly array list\n2. for doubly array list ")

    match int(user_in):
        case 1:
            single_array()
        case 2:
            double_array()




if __name__ == '__main__':
    main()

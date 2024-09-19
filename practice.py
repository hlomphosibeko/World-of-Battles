def board():
    """
    This function returns a number of dots entered by a user.
    """
    row = input("Enter number of rows you want...\n")
    column = input("Enter number of columns you want...\n")

    #for ind in range(dots):
        #print(".")
    [[print("*") for ind in range(int(row))] for dot in range(int(column))]   
    
def my_adder(row, column):
    #print(row + column)
    return row + column    

#board()
x = my_adder(2, 3)
print(x)
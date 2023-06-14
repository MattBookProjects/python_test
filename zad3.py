def get_input(promp):
    while True:
        a = input(promp)
        if a.isnumeric() and int(a) >=1 and int(a) <= 8:
            return int(a)
        else:
            print("Please enter a number form 1 to 8")


def can_queen_move(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    else:
        return False
    

first_square_row = get_input("Enter first square row: ")
first_square_column = get_input("Enter first square column: ")
second_square_row = get_input("Enter second square row: ")
second_square_column = get_input("Enter second square column: ")

if can_queen_move(first_square_row, first_square_column, second_square_row, second_square_column):
    print("YES")
else:
    print("NO")
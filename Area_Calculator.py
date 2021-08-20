import math
# function definition.
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"you'll need {num_of_cans} cans of paint.")

test_h = int(input("Height of Wall: \n "))
test_w = int(input("Width of Wall: \n"))

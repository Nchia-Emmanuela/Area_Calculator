import math
# function definition.
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)

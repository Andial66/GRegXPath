from math import cos, radians

# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    rad = radians(x)                             # cos works with radians
    numspaces = int(20 * cos(rad) + 20)          # scale to 0-40 spaces
    st = ' ' * numspaces + 'o'                   # place 'o' after the spaces
    return st

def main():
    for i in range(0, 1800, 12):
        s = make_dot_string(i)
        print(s)

main()
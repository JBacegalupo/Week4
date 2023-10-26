def print_header(msg):
    print("***** " + str(msg))

def find_min(a , b):
    if a == b:
        return "values are the same"
    elif a < b:
        return a
    else:
        return b

cube = lambda a: a * a * a
print(cube(3))

def f_read(filename):
    with open(filename, "r") as f:
        # content = f.read()        # whole file in contents(string) 
        # for line in f:            # access contents line by line
        # content = f.readlines()   # all lines into list

        content = f.readlines()
        return content

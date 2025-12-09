from file_read import f_read

dial = 50
dial_size = 100 # 0-99

count = 0
magnitude = 0
content = f_read("input.txt")
with open("out.txt", 'a') as w:
    for line in content:
        magnitude = int(line[1:]) # string slicing - start at 1 and go to end
        if line[0] != 'R':
            magnitude = -(magnitude)
        dial = dial + magnitude 
        # we want the Euclidian remainder to be language agnostic, since i want to port this to cpp and rust
        wrapped = ((dial % dial_size) + dial_size) % dial_size
        # print(f"{line:l}|{dial:l}|{wrapped:l}")
        
        dial = wrapped
        if dial == 0:
            count+=1
print(count)
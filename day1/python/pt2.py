from file_read import f_read

dial = 50
dial_size = 100 # 0-99

count = 0
magnitude = 0
content = f_read("input.txt")
with open("out.txt", 'a') as w:
    for line in content:
        prev_dial = dial
        magnitude = int(line[1:]) # string slicing - start at 1 and go to end
        if line[0] != 'R':
            magnitude = -(magnitude)
        dial = dial + magnitude 
        # we want the Euclidian remainder to be language agnostic, since i want to port this to cpp and rust
        wrapped = ((dial % dial_size) + dial_size) % dial_size
        dial = wrapped

        # check if it crossed zero or landed on it 
        dir = line[0]
        if dir ='R':
            diff = magnitude - (prev_dial + 1 ) # since 0-99 
            diff += 1
        elif dir :
            diff = magnitude - (dial_size - prev_dial )
            diff += 1
        count = count + ( diff // dial_size)




print(count)
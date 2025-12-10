from file_read import f_read

dial = 50
dial_size = 100  # 0-99

count = 0
magnitude = 0
content = f_read("input.txt")

with open("out.txt", 'w') as w:
    w.write("NEW FILE\n")
with open("out.txt", 'a') as w:
    for line in content:
        line = line.strip()

        prev_dial = dial
        dir = line[0]
        
        # let M be the Magnitude 
        M = int(line[1:])  # string slicing - start at 1 and go to end
        
        # Let m be the signed value
        if (dir == 'R'):
            m = M
        else:
            m = -M
        
        # new dial value 
        dial = dial + m



        # we want the Euclidian remainder to be language agnostic, since i want to port this to cpp and rust
        wrapped = ((dial % dial_size) + dial_size) % dial_size
        dial = wrapped



        if (dir == 'R'):
            if (M >= (100-prev_dial)):
                
                count += ((M - (100-prev_dial)) // 100) + 1
        else:
            if (prev_dial) <= M:
                if prev_dial == 0:
                    count += ((M-prev_dial) // 100)
                else:
                    count += ((M-prev_dial) // 100) + 1
        w.write(f"|line: {line:10}  | dial:{prev_dial:2}->{dial:2}| count:{count:10} |\n")
        print(f"{line}")
print(count)

import sys

try:
    file = open(sys.argv[1])
    for line in file:
        file.readlines()

    position = 0
    for line in lines:
        if position == 11:
            file.close()
            break
        if line != "":
            print(line.strip)
            position += 1

except IOerror:
    print(f"Error reading File: {sys.argv[1]}")
except IndexError:
    print(f"Error reading File: {sys.argv[1]}")



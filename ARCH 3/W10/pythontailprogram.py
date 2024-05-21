import sys

try:
    file = open(sys.argv[1])
    lines = file.readlines()

    position = 0
    lines_list = []
    for line in reversed(lines):
        if position == 11:
            file.close()
            break
        if line != "":
            lines_list.append(line)
            position += 1
    for line in reversed(lines_list):
        print(line.strip())

except IOError:
    print(F"Error Reading File: {sys.exc_info()[0]}")
except IndexError:
    print(F"Error Reading File: {sys.exc_info()[0]}")


if __name__ == "__main__":
    pass

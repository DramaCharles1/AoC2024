import sys
import re

def main(input):
    lines = []
    with open(input) as file:
        lines = file.readlines()
        result = 0
        regex = "mul\\(\\d*,\\d*\\)"
        regex2 = "\\d*,\\d*"
    for line in lines:
        mul_arr = re.findall(regex,line)
        #print(mul_arr)
        mul:str
        for mul in mul_arr:
            x = re.findall(regex2,mul)
            #print(x)
            i:str
            for i in x:
                mul_nmbr = i.split(",")
                result += int(mul_nmbr[0]) * int(mul_nmbr[1])
            #print(x)
    print(f"Part 1: {result}")
    print("=======Part 2=========")
    lines = []
    with open(input) as file:
        lines = file.readlines()
        result = 0
        regex = "(mul\\(\\d*,\\d*\\))|(do\\(\\))|(don't\\(\\))"
        regex2 = "\\d*,\\d*"
        enable = True
    for line in lines:
        mul_arr = re.findall(regex,line)
        print(mul_arr)
        mul:str
        for mul in mul_arr:
            if not enable and mul[1] != '':
                enable = True
            if enable and mul[2] != '':
                enable = False
            if mul[0] != '':
                x = re.findall(regex2,mul[0])
                for i in x:
                    mul_nmbr = i.split(",")
                    if enable:
                        result += int(mul_nmbr[0]) * int(mul_nmbr[1])

    print(f"Part 2: {result}")
if __name__ == "__main__":
    main(sys.argv[1])
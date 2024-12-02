import sys

def main(input):
    lines = []
    with open(input) as file:
        lines = file.readlines()

    reports = 0
    line: str

    for line in lines:
        print("new report")
        levels = line.split(" ")
        reports += 1
        increase = None
        last_increase = None
        for i in range(0, len(levels) - 1):
            levels[i] = levels[i].replace('\n','')
            diff = int(levels[i]) - int(levels[i + 1])
            if  0 < abs(diff) < 4:
                if diff > 0:
                    increase = True
                else:
                    increase = False
                if increase == last_increase or last_increase == None:
                    last_increase = increase
                else:
                    print("unsafe report")
                    reports -= 1
                    break #second condition not met
            else:
                print("unsafe report")
                reports -= 1
                break #first condition not met
    print(f"Part 1: {reports}")

    reports = 0
    for line in lines:
        print("new report")
        levels = line.split(" ")
        increase = None
        last_increase = None
        safe_counter = 0
        for i in range(0, len(levels) - 1):
            levels[i] = levels[i].replace('\n','')
            diff = int(levels[i]) - int(levels[i + 1])
            if  0 < abs(diff) < 4:
                if diff > 0:
                    increase = True
                else:
                    increase = False
                if increase == last_increase or last_increase == None:
                    safe_counter += 1
                    last_increase = increase
                else:
                    print("unsafe level")
                    #break #second condition not met
            else:
                print("unsafe level")
                #break #first condition not met
            if safe_counter == len(levels) - 1 or safe_counter == len(levels) - 2:
                reports += 1
        print(f"safe counter: {safe_counter}")
    print(f"Part 2: {reports}")
    #print(f"Part 2: {sim_score}")
if __name__ == "__main__":
    main(sys.argv[1])
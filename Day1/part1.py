import sys

def main(input):
    lines = []
    with open(input) as file:
        lines = file.readlines()
    left = []
    right =  []
    for line in lines:
        #line.replace(" ","")
        # print(line)
        # print(line[0:5])
        # print(line[8:13])
        left.append(int(line[0:5]))
        right.append(int(line[8:13]))
        #left.append(line[0])
        #right.append(line[4])
    #print(left)
    #print(right)
    left.sort()
    right.sort()
    #print(left)
    #print(right)
    total_distance = 0
    sim_score = 0
    multiply = 0
    for i in range(0,len(left)):
        total_distance += abs(left[i] - right[i])
        #part 2:
        for j in range(0,len(right)):
            if left[i] == right[j]:
                #print("found")
                multiply += 1
        print(multiply)
        sim_score += left[i] * multiply
        multiply = 0

    print(f"Part 1: {total_distance}")
    print(f"Part 2: {sim_score}")
if __name__ == "__main__":
    main(sys.argv[1])
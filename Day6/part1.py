import sys

def main(input):
    lines = []
    with open(input) as file:
        #Create map with coord (x,y)
        #Find every X, then M, A, S in every direction
        lines = file.readlines()
        X_MAX = len(lines[0]) - 1
        Y_MAX = len(lines)
        print(f"X_MAX: {X_MAX}")
        print(f"Y_MAX: {Y_MAX}")
        coords = {}

        for y in range(0,Y_MAX):
            for x in range(0,X_MAX):
                coords[f"{x},{y}"] = lines[y][x]
                temp = coords[f"{x},{y}"]
        guard_start_pos = ""
        guard_direction = ""
        guard_position = ""
        distinct_positions = 0

        for y in range(0,Y_MAX):
            for x in range(0,X_MAX):
                if coords[f"{x},{y}"] == "^":
                    guard_start_pos = f"{x},{y}"
                    guard_direction = "^"
                if coords[f"{x},{y}"] == ">":
                    guard_start_pos = f"{x},{y}"
                    guard_direction = ">"
                if coords[f"{x},{y}"] == "v":
                    guard_start_pos = f"{x},{y}"
                    guard_direction = "v"
                if coords[f"{x},{y}"] == "<":
                    guard_start_pos = f"{x},{y}"
                    guard_direction = "<"
        print(f"start pos: {guard_start_pos}")
        guard_position = guard_start_pos

        # i = 0
        # for y in range(0,Y_MAX):
        #     i = 0
        #     for x in range(0,X_MAX):
        #         i += 1
        #         #print(i)
        #         if i == X_MAX:
        #             print(coords[f"{x},{y}"],end="\n")
        #             #print("here")
        #         else:
        #             print(coords[f"{x},{y}"],end="")

        #Check if #, then update direction
        #Update position
        try:
            while True:
                cur_x = int(guard_position.split(",")[0])
                cur_y = int(guard_position.split(",")[1])
                if guard_direction == "^":
                    if coords[f"{cur_x},{cur_y - 1}"] == "#":
                        guard_direction = ">"
                        coords[guard_position] = guard_direction
                    else:
                        coords[guard_position] = "X"
                        guard_position = f"{cur_x},{cur_y - 1}"
                        coords[guard_position] = "^"
                elif guard_direction == ">":
                    if coords[f"{cur_x + 1},{cur_y}"] == "#":
                        guard_direction = "v"
                        coords[guard_position] = guard_direction
                    else:
                        coords[guard_position] = "X"
                        guard_position = f"{cur_x + 1},{cur_y}"
                        coords[guard_position] = ">"
                elif guard_direction == "v":
                    if coords[f"{cur_x},{cur_y + 1}"] == "#":
                        guard_direction = "<"
                        coords[guard_position] = guard_direction
                    else:
                        coords[guard_position] = "X"
                        guard_position = f"{cur_x},{cur_y + 1}"
                        coords[guard_position] = "<"
                elif guard_direction == "<":
                    if coords[f"{cur_x - 1},{cur_y}"] == "#":
                        guard_direction = "^"
                        coords[guard_position] = guard_direction
                    else:
                        coords[guard_position] = "X"
                        guard_position = f"{cur_x - 1},{cur_y}"
                        coords[guard_position] = "<"
                #print("---------------")
                # i = 0
                # for y in range(0,Y_MAX):
                #     i = 0
                #     for x in range(0,X_MAX):
                #         i += 1
                #         #print(i)
                #         if i == X_MAX:
                #             print(coords[f"{x},{y}"],end="\n")
                #             #print("here")
                #         else:
                #             print(coords[f"{x},{y}"],end="")
        except KeyError:
            print("guard is leaving")
        
        distinct_positions += 1 #start pos
        for y in range(0,Y_MAX):
            for x in range(0,X_MAX):
                if coords[f"{x},{y}"] == "X":
                    distinct_positions += 1
        print(f"Result part 1: {distinct_positions}")

if __name__ == "__main__":
    main(sys.argv[1])
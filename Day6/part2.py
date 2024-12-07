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
        original_coords =  {}
        obstacle_hit_coords = {}

        for y in range(0,Y_MAX):
            for x in range(0,X_MAX):
                coords[f"{x},{y}"] = lines[y][x]

        guard_start_direction = ""
        guard_start_pos = ""
        guard_direction = ""
        guard_position = ""
        loop_positions = 0
        original_coords = coords.copy()

        for y in range(0,Y_MAX):
            for x in range(0,X_MAX):
                if coords[f"{x},{y}"] == "^":
                    guard_start_pos = f"{x},{y}"
                    guard_start_direction = "^"
                if coords[f"{x},{y}"] == ">":
                    guard_start_pos = f"{x},{y}"
                    guard_start_direction = ">"
                if coords[f"{x},{y}"] == "v":
                    guard_start_pos = f"{x},{y}"
                    guard_start_direction = "v"
                if coords[f"{x},{y}"] == "<":
                    guard_start_pos = f"{x},{y}"
                    guard_start_direction = "<"
        print(f"start pos: {guard_start_pos}")
        print(f"start direction: {guard_start_direction}")
        guard_position = guard_start_pos
        guard_direction = guard_start_direction
        print("---------------")
        j = 0
        for k in range(0,Y_MAX):
            j = 0
            for l in range(0,X_MAX):
                j += 1
                #print(i)
                if j == X_MAX:
                    print(original_coords[f"{l},{k}"],end="\n")
                    #print("here")
                else:
                    print(original_coords[f"{l},{k}"],end="")
        #Update map with obstacle for each valid postion
        #Check if guard_position == guard_start_pos and guard_direction == guard_start_direction
        for y in range(0,Y_MAX):
            for x in range(0,X_MAX):
                coords = original_coords.copy()
                guard_position = guard_start_pos
                guard_direction = guard_start_direction
                coords[f"{x},{y}"] = "#"
                if x == 3 and y == 6:
                    print("---------------")
                    j = 0
                    for k in range(0,Y_MAX):
                        j = 0
                        for l in range(0,X_MAX):
                            j += 1
                            #print(i)
                            if j == X_MAX:
                                print(coords[f"{l},{k}"],end="\n")
                                #print("here")
                            else:
                                print(coords[f"{l},{k}"],end="")
                    print(f"coords[guard_position] = {coords[guard_position]}")
                    print(f"obstacle_hit_coords[guard_position] = {obstacle_hit_coords[guard_position]}")
                    
                try:
                    while True:
                        cur_x = int(guard_position.split(",")[0])
                        cur_y = int(guard_position.split(",")[1])
                        if guard_direction == "^":
                            if coords[f"{cur_x},{cur_y - 1}"] == "#":
                                obstacle_hit_coords[guard_position] = guard_direction
                                guard_direction = ">"
                                coords[guard_position] = guard_direction
                            else:
                                coords[guard_position] = "X"
                                guard_position = f"{cur_x},{cur_y - 1}"
                                coords[guard_position] = "^"
                        elif guard_direction == ">":
                            if coords[f"{cur_x + 1},{cur_y}"] == "#":
                                obstacle_hit_coords[guard_position] = guard_direction
                                guard_direction = "v"
                                coords[guard_position] = guard_direction
                            else:
                                coords[guard_position] = "X"
                                guard_position = f"{cur_x + 1},{cur_y}"
                                coords[guard_position] = ">"
                        elif guard_direction == "v":
                            if coords[f"{cur_x},{cur_y + 1}"] == "#":
                                obstacle_hit_coords[guard_position] = guard_direction
                                guard_direction = "<"
                                coords[guard_position] = guard_direction
                            else:
                                coords[guard_position] = "X"
                                guard_position = f"{cur_x},{cur_y + 1}"
                                coords[guard_position] = "<"
                        elif guard_direction == "<":
                            if coords[f"{cur_x - 1},{cur_y}"] == "#":
                                obstacle_hit_coords[guard_position] = guard_direction
                                guard_direction = "^"
                                coords[guard_position] = guard_direction
                            else:
                                coords[guard_position] = "X"
                                guard_position = f"{cur_x - 1},{cur_y}"
                                coords[guard_position] = "<"
                        if coords[guard_position] == obstacle_hit_coords[guard_position]:
                            print("loop position found")
                            loop_positions += 1
                            #coords = original_coords
                            break
                except KeyError:
                    #coords = original_coords
                    print("guard is leaving")
                    print(obstacle_hit_coords)

        print(f"Result part 2: {loop_positions}")

if __name__ == "__main__":
    main(sys.argv[1])
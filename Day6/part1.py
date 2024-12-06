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
        guard_positions = 0
        guard_direction = "up"
        guard_position = ""

        for y in range(0,Y_MAX):
            for x in range(0,X_MAX):
                if coords[f"{x},{y}"] == "^":
                    guard_start_pos = f"{x},{y}"
        print(f"start pos: {guard_start_pos}")
        guard_position = guard_start_pos

        try:
            while True:
                if guard_direction == "up":
                    if coords[f"{x},{y + 1}" == "#"]:
                        guard_direction = "right"
                        coords[guard_position] == "X"
                    else:
                        coords[guard_position] == "X"
                if guard_direction == "right":
                    if coords[f"{x + 1},{y}" == "#"]:
                        guard_direction = "down"
                        coords[guard_position] == "X"
                    else:
                        coords[guard_position] == "X"
        except KeyError:
            print("guard is leaving")

if __name__ == "__main__":
    main(sys.argv[1])
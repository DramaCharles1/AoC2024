import sys

def main(input):
    lines = []
    xmas_count = 0
    mas_count = 0
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
                #print(f"coord: {x},{y} = {temp}")
        
        
        for y in range(0,Y_MAX):
            for x in range(0,X_MAX):
                if coords[f"{x},{y}"] == "X":
                    #Check all directions
                    try:
                        #Right
                        if coords[f"{x + 1},{y}"] == "M":
                            if coords[f"{x + 2},{y}"] == "A":
                                if coords[f"{x + 3},{y}"] == "S":
                                    print("Found Right")
                                    xmas_count += 1
                    except KeyError:
                        print("Not a valid coord")
                    #Right-Down
                    try:
                        if coords[f"{x + 1},{y - 1}"] == "M":
                            if coords[f"{x + 2},{y - 2}"] == "A":
                                if coords[f"{x + 3},{y - 3}"] == "S":
                                    print("Found Right-Down")
                                    xmas_count += 1
                    except KeyError:
                        print("Not a valid coord")
                    #Down
                    try:
                        if coords[f"{x},{y - 1}"] == "M":
                            if coords[f"{x},{y - 2}"] == "A":
                                if coords[f"{x},{y - 3}"] == "S":
                                    xmas_count += 1
                                    print("Found Down")
                    except KeyError:
                        print("Not a valid coord")
                    #Left-Down
                    try:
                        if coords[f"{x - 1},{y - 1}"] == "M":
                            if coords[f"{x - 2},{y - 2}"] == "A":
                                if coords[f"{x - 3},{y - 3}"] == "S":
                                    xmas_count += 1
                                    print("Found Left-Down")
                    except KeyError:
                        print("Not a valid coord")
                    #Left
                    try:
                        if coords[f"{x - 1},{y}"] == "M":
                            if coords[f"{x - 2},{y}"] == "A":
                                if coords[f"{x - 3},{y}"] == "S":
                                    xmas_count += 1
                                    print("Found Left")
                    except KeyError:
                        print("Not a valid coord")
                    #Left-Up
                    try:
                        if coords[f"{x - 1},{y + 1}"] == "M":
                            if coords[f"{x - 2},{y + 2}"] == "A":
                                if coords[f"{x - 3},{y + 3}"] == "S":
                                    xmas_count += 1
                                    print("Found Left-Up")
                    except KeyError:
                        print("Not a valid coord")
                    #Up
                    try:
                        if coords[f"{x},{y + 1}"] == "M":
                            if coords[f"{x},{y + 2}"] == "A":
                                if coords[f"{x},{y + 3}"] == "S":
                                    xmas_count += 1
                                    print("Found Up")
                    except KeyError:
                        print("Not a valid coord")
                    #Right-Up
                    try:
                        if coords[f"{x + 1},{y + 1}"] == "M":
                            if coords[f"{x + 2},{y + 2}"] == "A":
                                if coords[f"{x + 3},{y + 3}"] == "S":
                                    xmas_count += 1
                                    print("Found Right-Up")
                    except KeyError:
                        print("Not a valid coord")
        print(f"Part 1: {xmas_count}")

        for y in range(0,Y_MAX):
            for x in range(0,X_MAX):
                if coords[f"{x},{y}"] == "A":
                    #Check all combinations of X-MAS
                    try:
                        #1
                        #M.S
                        #.A.
                        #M.S
                        if coords[f"{x - 1},{y + 1}"] == "M":
                            if coords[f"{x + 1},{y + 1}"] == "S":
                                if coords[f"{x - 1},{y - 1}"] == "M":
                                    if coords[f"{x + 1},{y - 1}"] == "S":
                                        print(f"Found X-MAS 1 with A coord: {x},{y}")
                                        mas_count += 1
                    except KeyError:
                        print("Not a valid coord")
                    try:
                        #2
                        #S.M
                        #.A.
                        #S.M
                        if coords[f"{x - 1},{y + 1}"] == "S":
                            if coords[f"{x + 1},{y + 1}"] == "M":
                                if coords[f"{x - 1},{y - 1}"] == "S":
                                    if coords[f"{x + 1},{y - 1}"] == "M":
                                        print(f"Found X-MAS 2 with A coord: {x},{y}")
                                        mas_count += 1
                    except KeyError:
                        print("Not a valid coord")
                    try:
                        #3
                        #M.M
                        #.A.
                        #S.S
                        if coords[f"{x - 1},{y + 1}"] == "M":
                            if coords[f"{x + 1},{y + 1}"] == "M":
                                if coords[f"{x - 1},{y - 1}"] == "S":
                                    if coords[f"{x + 1},{y - 1}"] == "S":
                                        print(f"Found X-MAS 3 with A coord: {x},{y}")
                                        mas_count += 1
                    except KeyError:
                        print("Not a valid coord")
                    try:
                        #4
                        #S.S
                        #.A.
                        #M.M
                        if coords[f"{x - 1},{y + 1}"] == "S":
                            if coords[f"{x + 1},{y + 1}"] == "S":
                                if coords[f"{x - 1},{y - 1}"] == "M":
                                    if coords[f"{x + 1},{y - 1}"] == "M":
                                        print(f"Found X-MAS 4 with A coord: {x},{y}")
                                        mas_count += 1
                    except KeyError:
                        print("Not a valid coord")
        print(f"Part 2: {mas_count}")

if __name__ == "__main__":
    main(sys.argv[1])
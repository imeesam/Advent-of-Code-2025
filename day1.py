with open("input1.txt") as f:
    input_text = f.read().strip()

rotations = input_text.strip().split("\n")

def solve_safe_password_part2(rotations):
    current_pos = 50
    password_count = 0

    for rotation in rotations:
        rotation = rotation.strip()
        if not rotation:
            continue
        
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'R':
            for _ in range(distance):
                current_pos = (current_pos + 1) % 100
                if current_pos == 0:
                    password_count += 1
        else:  # direction == 'L'
            for _ in range(distance):
                current_pos = (current_pos - 1) % 100
                if current_pos == 0:
                    password_count += 1

    return password_count



password = solve_safe_password_part2(rotations)
print("Password:", password)

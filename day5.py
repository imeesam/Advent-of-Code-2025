def count_fresh_ingredients(lines):
    ranges = []
    ids = []

    # Split into two parts around blank line
    blank_index = lines.index("")

    # Parse ranges
    for line in lines[:blank_index]:
        a, b = map(int, line.split("-"))
        ranges.append((a, b))

    # Parse ingredient IDs
    for line in lines[blank_index+1:]:
        if line.strip():
            ids.append(int(line.strip()))

    fresh_count = 0

    for id_num in ids:
        for a, b in ranges:
            if a <= id_num <= b:
                fresh_count += 1
                break  # no need to check more ranges

    return fresh_count

with open("input5.txt") as f:
    lines = [line.strip() for line in f]

print(count_fresh_ingredients(lines))


#----------------------------------------------------------------


def count_total_fresh_ids(lines):
    ranges = []

    for line in lines:
        if "-" in line:
            a, b = map(int, line.split("-"))
            ranges.append((a, b))


    ranges.sort()

    merged = []
    start, end = ranges[0]

    for a, b in ranges[1:]:
        if a <= end + 1:  # overlap or touching
            end = max(end, b)
        else:
            merged.append((start, end))
            start, end = a, b

    merged.append((start, end))


    total = 0
    for a, b in merged:
        total += (b - a + 1)

    return total

with open("input5.txt") as f:
    lines = [line.strip() for line in f]

print(count_total_fresh_ids(lines))

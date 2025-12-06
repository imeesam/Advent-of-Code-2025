with open("input2.txt") as f:
    input_text = f.read().strip()

def prble_2(input_str):
    start_s,end_s = input_str.split("-")
    total = 0
    start =  int(start_s)
    end =  int(end_s)
    for n in range(start, end+1):
        s = str(n)
        if len(s) % 2 == 0:
            half = len(s) // 2
            if s[:half] == s[half:]:
                total+=n

    return total
print(prble_2(input_text))

# -------------------------------------


def is_invalid(n):
    s = str(n)
    for l in range(1, len(s)//2 + 1):  
        if len(s) % l != 0:
            continue
        pattern = s[:l]
        repeats = len(s) // l
        if pattern * repeats == s:
            return True
    return False

def sum_invalid_ids(input_text):
    ranges = input_text.strip().split(",")
    total = 0
    
    for r in ranges:
        r = r.strip()
        if not r:
            continue
        start_str, end_str = r.split("-")
        start = int(start_str)
        end = int(end_str)
        
        for n in range(start, end + 1):
            if is_invalid(n):
                total += n
                    
    return total


print(sum_invalid_ids(input_text))
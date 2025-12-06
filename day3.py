with open("input3.txt") as f:
    input_text = f.read().strip()

joltages = input_text.strip().split("\n")

def max_joltage_sum(banks):
    total = 0
    for bank in banks:
        max_joltage = 0
        n = len(bank)
        for i in range(n):
            for j in range(i+1, n):
                joltage = int(bank[i] + bank[j])
                if joltage > max_joltage:
                    max_joltage = joltage
        total += max_joltage
    return total

print(max_joltage_sum(joltages))


#----------------------------------

banks = input_text.strip().split("\n")

def max_joltage_k_digits(bank, k):
    stack = []
    n = len(bank)
    
    for i, digit in enumerate(bank):
        # While stack has smaller digits and we can still pick enough digits later
        while stack and digit > stack[-1] and len(stack) - 1 + (n - i) >= k:
            stack.pop()
        if len(stack) < k:
            stack.append(digit)
    
    return int("".join(stack))

def total_max_joltage(banks, k=12):
    total = 0
    for bank in banks:
        total += max_joltage_k_digits(bank, k)
    return total

result = total_max_joltage(banks, 12)
print(result)


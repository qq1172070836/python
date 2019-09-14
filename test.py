all_step = 0

def go(step):
    global all_step
    n = all_step + step
    all_step = n
    return all_step

print(go(2))
print(go(3))
print(go(5))
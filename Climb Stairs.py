n = 6

def step_tree(n, cur_stair, steps):

    if cur_stair == n:
        print("Result: ", steps)
        return steps[0]+steps[1]

    steps = steps[0]+steps[1], steps[0]
    print(steps)
    print("Total Steps: %d" % (steps[0] + steps[1]))
    cur_stair += 1
    return step_tree(n, cur_stair, steps)

print(step_tree(n, 2, (1, 1)))
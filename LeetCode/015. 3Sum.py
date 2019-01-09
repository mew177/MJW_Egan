def bs(nums, l, r, tar):
    if l == r - 1:
        return -1
    mid = (l + r) / 2
    if nums[mid] == tar:
        return mid
    elif nums[mid] > tar:
        return bs(nums, l, mid, tar)
    elif nums[mid] < tar:
        return bs(nums, mid, r, tar)

nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

sol = []

for i in range(len(nums)):
    print("+++++ " + str(nums[i]) + " +++++++")
    for j in range(i + 1, len(nums)):
        tar = -(nums[i] + nums[j])
        print(tar)
        k = bs(nums, j, len(nums), tar)
        if k != -1 and i != k and j != k and i != j:
            new = sorted([nums[i], nums[j], nums[k]])
            if new not in sol:
                sol.append(new)
print(sol)

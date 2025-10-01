def unique_elements(lst):
    unq = []
    for i in lst:
        if i not in unq:
            unq.append(i)
    return unq

nums = list(map(int, input().split()))
print(unique_elements(nums))
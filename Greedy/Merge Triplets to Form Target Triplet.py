def mergeTriplets(triplets, target):
    
    s = set()
    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue
        else:
            for i, num in enumerate(t):
                if num == target[i]:
                    s.add(i)
    
    return len(s) == 3

print(mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))
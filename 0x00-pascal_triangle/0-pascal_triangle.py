def pascal_triangle(n):
    cache = [[1]]
    for i in range(1, n):
        tmp = [0] + cache[-1] + [0]
        new = []
        for j in range(len(cache) + 1):
            new.append(tmp[j] + tmp[j + 1])
        cache.append(new)
        
    return cache

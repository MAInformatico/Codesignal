def startupName(companies):
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    res = set(companies[0] + companies[1] + companies[2]) ^ (cmp1 ^ cmp2 ^ cmp3)
    return list(sorted(list(res)))

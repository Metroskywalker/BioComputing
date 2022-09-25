def psa(seq1, seq2, match, miss, gap):
    """ i is horizontal, j is vertical"""
    i = list(seq1)
    j = list(seq2)
    p = [0, 0, 0]
    """ make sure j is the longest sequence"""
    if len(i) > len(j):
        i = list(seq2)
        j = list(seq1)
    """ setup for answer list"""
    ans = []
    for ver in range(len(j)+1):
        ans.append([])
        for hor in range(len(i)+1):
            ans[ver].append(0)
    """ first line of results are gaps"""
    ans[0][0] = 0
    for hor in range(len(i)):
        ans[0][hor+1] = ans[0][hor] + gap
    for ver in range(len(j)):
        ans[ver+1][0] = ans[ver][0] + gap
    """ actual calculation"""
    for ver in range(len(j)):
        for hor in range(len(i)):
            if i[hor] == j[ver]:
                p[0] = ans[ver][hor] + match
            else:
                p[0] = ans[ver][hor] + miss
            p[1] = ans[ver][hor+1] + gap
            p[2] = ans[ver+1][hor] + gap
            ans[ver+1][hor+1] = max(p)
    """ print results"""
    for num in range(len(ans)):
        print(ans[num])

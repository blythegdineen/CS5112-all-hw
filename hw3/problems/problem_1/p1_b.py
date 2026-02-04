# Problem 1b


def maximal_bipartite_match(g) -> int:
    match_count = 0
    docs = len(g)
    hospitals = len(g[0])
    matches = [-1] * hospitals

    def matching(d):
        # for each hospital, check doctor's preference and match
        for h in range(hospitals):
            if g[d][h] and seen[h] == False:
                seen[h] = True
                if matches[h] == -1 or matching(matches[h]):
                    matches[h] = d
                    return True
        return False

    for d in range(docs):
        seen = [False] * hospitals
        if matching(d):
            match_count +=1

    return match_count
# wordA : ACAYKP
# wordB : CAPCAK


wordA = tuple(' ' + input().strip())
wordB = tuple(' ' + input().strip())

lenA, lenB = len(wordA), len(wordB)

cache = [[0 for _ in range(lenA)] for _ in range(lenB)]
#      A  C  A  Y  K  P
#   0  0  0  0  0  0  0
# C 0  0  1  1  1  1  1
# A 0  1
# P 0  1
# C 0  1
# A 0  1
# K 0  1
for i in range(1, lenB):
    for j in range(1, lenA):
        if wordA[j] == wordB[i]: # 현재 문자가 같으면
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i][j-1], cache[i-1][j])

print(cache[lenB-1][lenA-1])



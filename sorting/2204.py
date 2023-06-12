import sys; input=sys.stdin.readline

while True:
    n=int(input())
    if n==0:
        break

    g_word=''
    for i in range(n):
        tmp_word=input().rstrip()
        if i==0:
            g_word=tmp_word
        elif tmp_word.lower() < g_word.lower():
            g_word=tmp_word
    print(g_word)
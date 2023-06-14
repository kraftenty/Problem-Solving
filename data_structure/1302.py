import sys; input=sys.stdin.readline

books=dict()
N=int(input())
for n in range(N):
    title=input().rstrip()
    if title in books:
        books[title]+=1
    else:
        books[title]=1

max=0
maxBookTitle=''
sorted_books = dict(sorted(books.items()))
for book in sorted_books:
    if(sorted_books[book] > max):
        max=sorted_books[book]
        maxBookTitle=book

print(maxBookTitle)
with open('things.txt','r') as things:
    li = list(things.read().split())

li.sort(reverse=True)
result = ''
for elem in li:
    result = result + (elem + '\n')
with open('rethings.txt','w') as rethings:
    rethings.write(result)
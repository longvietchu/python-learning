i = 1
while i < 5:
    print(i)
    i += 1

print('with if')
j = 1
while j < 5:
    print(j)
    if j == 2:
        break
    j += 1

print('with range')
for k in range(8):
    print(k)

number_list = range(0,100)
print(number_list)
print("=" * 50)
even = range(0,100, 2)
odd = range(1,100, 2)
print(even)
print("=" * 50)
print(odd)

print("=" * 50)

r = range(0,100)
print(r)
for i in r[::-2]:
    print(i)

print("=" * 50)

statement = "seikooc tnaw i"
print(statement[::-1])   # Allow statment to go in reversed order, counting 1 backards.

o = range(0,100,4)
print(o)

i = o[::5]  # Will multiply "4*5" and count by 20's
print(i)

for individuals in i:
    print(individuals)

j = o[::2]
for experiment in j:
    print(j)

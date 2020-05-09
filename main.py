print("Hello")
# Не так может много примеров(уже знаком с Python), не хватает времени столько печатать , если что) ыыы

# Numbers
x = 5
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(-x, -y)
print(abs(x), abs(y))
print(divmod(x, y))
print(x ** y)
print(pow(x, y, 3))

# Lists
l = [1, 2, 3]

l.append(4)
print(l)
l.extend([5, 6])
print(l)
l.insert(0, 0)
print(l)
l.remove(0)
print(l)
print(l.pop(2))
l.sort()
print(l)
l.reverse()
print(l)
print(l.count(5))
l2 = l.copy()
print(l2)
l.clear()
print(l)

# Indexes and slices
d = [1, 44, 33, 15, 0, 5]
print(d[0])
print(d[-1])
print(d[2:])
print(d[:])
print(d[:4])
print(d[::2])
print(d[::-1])
print(d[:-2])
print(d[1:4:-1])
del d[-3]
print(d)
print(d[-2::-1])

# Tuples
a = (1, 2, 3, 4, 5, 6, 7, 10)
print(a.__sizeof__())
print(tuple("Hello Max"))
b = ("d",)
print(b)
print(a[3])
print(a[:-1])
print(a[2:5])

# Dictionaries
smth = {"name": "Max", "number": 22}
print(smth["name"], smth["number"])
print(smth.keys())
print(smth.values())
print(smth.items())
smth.setdefault("age", 50)
print(smth)
smth2 = smth.copy()
print(smth2)
smth.update({"lol": 4, "kek": 0})
print(smth)
smth.clear()
print(smth)





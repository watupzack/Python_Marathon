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






# Set mutable
a = set()
print(a)
a = set("hello")
a = {"a", "b", "c", "d"}
print(a)
words = [2, 5, 33, 40]
set_words = set(words)
print(len(set_words))
print("hello" in set_words)
set_words2 = set_words.copy()
set_words2.add(100)
set_words.remove(33)
set_words.pop()
print(set_words)
set_words.clear()
print(set_words)
print(set_words2)

# Frozen set immutable
b = set("qwerty")
c = frozenset("qwerty")
print(b == c)
b.add(44)
# wrong c.add(2)
print(type(b | c))
print(type(b - c))

# Byte strings
bs = b"bytes"
print("Байты".encode("utf-8"))
print(bytes("bytes", encoding="utf-8"))
print(bytes([50, 100, 22, 33, 19]))
print(chr(50), chr(20), chr(100))
print(b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8'))

# Bytearray
bs2 = bytearray(b"hello world!")
print(bs[0])
print(bs2)
bs2[0] = 105
print(bs2)

# String
s = "Hello Andy's Pizza"
s2 = " Good3"
long_s = """
hello
andy
lol123

"""
print(r"Hello Andy's Pizza")
print("I\n am\n Maxim")
print(s + s2)
print(s2 * 3)
print(len(s))
print(s[:3] + " " + s2[:4])
print(s.split(" "))
print(s.islower())
print(s.startswith("Hell"))
print(s2.isalpha())
s2.capitalize()
print(s2)

print("I have {} apples".format(4))
print("I have %d applications and %d apples" % (33, 56))


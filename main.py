print("Hello")

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


# 🐍 Cheat Sheet — Bloc 2 : Loops & Strings

> Quick reference card. No essays — just the syntax you need.

---

## 🔁 `for` Loop

```python
# Loop over a range
for i in range(5):
    print(i)          # 0 1 2 3 4

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)          # 1 3 5 7 9

# Loop over a string
for char in "hello":
    print(char)       # h e l l o

# Loop with index
for i, char in enumerate("hello"):
    print(i, char)    # 0 h  1 e  2 l ...
```

---

## 🔄 `while` Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1        # 0 1 2 3 4

# Infinite loop with break
while True:
    answer = input("Type 'quit' to stop: ")
    if answer == "quit":
        break
```

---

## ⏭ `break` / `continue` / `else`

```python
for i in range(10):
    if i == 3:
        continue      # skip 3, keep going
    if i == 7:
        break         # stop at 7
    print(i)          # 0 1 2 4 5 6

# else on a loop — runs if loop finished WITHOUT break
for i in range(5):
    if i == 10:
        break
else:
    print("No break happened")   # prints
```

---

## 🔢 ASCII & `ord()` / `chr()`

```python
ord('A')    # 65  — character → ASCII code
ord('a')    # 97
ord('0')    # 48

chr(65)     # 'A' — ASCII code → character
chr(97)     # 'a'
chr(66)     # 'B'

# Print alphabet with ASCII
for i in range(26):
    print(chr(ord('a') + i), end=' ')   # a b c d ... z
```

### Useful ASCII ranges
| Range | Characters |
|-------|-----------|
| 65–90 | A–Z |
| 97–122 | a–z |
| 48–57 | 0–9 |

---

## 🔤 Strings

### Basics
```python
s = "Hello, World!"

len(s)          # 13  — length
s[0]            # 'H' — first character
s[-1]           # '!' — last character
s[0:5]          # 'Hello' — slicing [start:stop]
s[::2]          # every 2nd character
s[::-1]         # reversed string
```

### Common methods
```python
s.upper()           # 'HELLO, WORLD!'
s.lower()           # 'hello, world!'
s.strip()           # removes leading/trailing spaces
s.replace("o", "0") # 'Hell0, W0rld!'
s.split(", ")       # ['Hello', 'World!']
s.count("l")        # 3
s.startswith("He")  # True
s.endswith("!")     # True
"llo" in s          # True — substring check
```

### String building
```python
# Concatenation
greeting = "Hello" + " " + "World"

# f-string (preferred)
name = "Alice"
print(f"Hello, {name}!")

# Join a list of strings
words = ["one", "two", "three"]
print(", ".join(words))     # one, two, three
```

---

## 🧠 Common Mistakes

| Mistake | Why it breaks | Fix |
|---------|--------------|-----|
| `for i in range(1, 5)` expecting 5 | `range` stop is exclusive | `range(1, 6)` |
| infinite `while` loop | condition never becomes False | make sure something changes each iteration |
| `s[len(s)]` | index out of range | last index is `len(s) - 1` |
| `s = s + char` in a loop | works but slow | use a list + `"".join()` |
| forgetting `end=""` in print | newline after each char | `print(char, end="")` |

---

## ⚡ Quick Reference

```python
# Count vowels in a string
text = input("Enter text: ")
count = 0
for char in text.lower():
    if char in "aeiou":
        count += 1
print(f"Vowels: {count}")

# Print alphabet in reverse using ASCII
for i in range(25, -1, -1):
    print(chr(ord('a') + i), end=' ')   # z y x ... a
```
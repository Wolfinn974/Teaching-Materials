# 🐍 Cheat Sheet — Bloc 1 : Basics

> Quick reference card. No essays — just the syntax you need.

---

## 📦 Variables & Types

```python
# Assigning a variable
name = "Alice"       # str  — text
age = 17             # int  — whole number
height = 1.72        # float — decimal number
is_cool = True       # bool — True or False

# Check the type
print(type(age))     # <class 'int'>
```

### Type conversion
```python
x = "42"
x = int(x)       # str → int
x = float(x)     # str → float
x = str(42)      # int → str
```

### Quick type rules
| Type | Example | Quotes? |
|------|---------|---------|
| `str` | `"hello"` | ✅ |
| `int` | `42` | ❌ |
| `float` | `3.14` | ❌ |
| `bool` | `True` / `False` | ❌ |

---

## 🖨 Output — `print()`

```python
print("Hello!")                        # Hello!
print("My name is", name)             # My name is Alice
print(f"I am {age} years old")        # I am 17 years old  ← f-string (preferred)
print("Score:", 42, "pts")            # Score: 42 pts
```

---

## ⌨️ Input — `input()`

```python
name = input("What is your name? ")   # always returns a str
age  = int(input("How old are you? ")) # convert if you need a number
```

> ⚠️ `input()` **always** returns a string. Convert it if you need a number.

---

## 🔢 Operators

### Arithmetic
```python
10 + 3   # 13   addition
10 - 3   # 7    subtraction
10 * 3   # 30   multiplication
10 / 3   # 3.33 division (always float)
10 // 3  # 3    integer division (floor)
10 % 3   # 1    modulo (remainder)
10 ** 3  # 1000 exponent
```

### Comparison — returns `True` or `False`
```python
x == y   # equal
x != y   # not equal
x > y    # greater than
x < y    # less than
x >= y   # greater than or equal
x <= y   # less than or equal
```

### Logical
```python
True and False   # False — both must be True
True or False    # True  — at least one must be True
not True         # False — inverts the value
```

---

## 🔀 Conditions — `if / elif / else`

```python
score = 75

if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")
```

> ⚠️ **Indentation matters.** Python uses spaces (4) — not curly braces.

### Inline condition (ternary)
```python
label = "pass" if score >= 60 else "fail"
```

---

## 🧠 Common Mistakes

| Mistake | Why it breaks | Fix |
|---------|--------------|-----|
| `age = input(...)` then `age + 1` | input is a `str`, can't add int | `int(input(...))` |
| `if x = 5` | single `=` is assignment | `if x == 5` |
| wrong indentation | Python reads it as outside the block | use 4 spaces consistently |
| `print(f"age: {age}")` with no `f` | curly braces printed literally | don't forget the `f` |

---

## ⚡ Quick Reference

```python
# Full basic program structure
name  = input("Your name: ")
age   = int(input("Your age: "))

if age >= 18:
    print(f"Welcome, {name}!")
else:
    print(f"Sorry {name}, you must be 18+.")
```
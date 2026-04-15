# 🐍 Cheat Sheet — Bloc 3 : Functions & Algorithms

> Quick reference card. No essays — just the syntax you need.

---

## 🧩 Defining & Calling Functions

```python
# Define
def greet(name):
    print(f"Hello, {name}!")

# Call
greet("Alice")        # Hello, Alice!

# With return value
def add(a, b):
    return a + b

result = add(3, 5)    # 8
```

---

## 📥 Parameters & Arguments

```python
# Default parameter
def greet(name, loud=False):
    if loud:
        print(f"HELLO, {name.upper()}!")
    else:
        print(f"Hello, {name}!")

greet("Alice")              # Hello, Alice!
greet("Alice", loud=True)   # HELLO, ALICE!

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2])   # low=1, high=7
```

---

## 🔭 Scope — Where Variables Live

```python
x = 10          # global variable

def my_func():
    y = 5       # local variable — only exists inside the function
    print(x)    # ✅ can read global
    print(y)    # ✅ local is fine

my_func()
print(y)        # ❌ NameError — y doesn't exist outside
```

> ⚠️ Avoid modifying global variables inside functions — pass values as parameters instead.

```python
# ❌ Bad habit
total = 0
def add_to_total(n):
    global total          # works but messy
    total += n

# ✅ Better
def add(total, n):
    return total + n

total = add(total, 5)
```

---

## 🔁 Recursion (intro)

```python
# A function that calls itself
def countdown(n):
    if n <= 0:            # base case — ALWAYS needed
        print("Go!")
        return
    print(n)
    countdown(n - 1)      # recursive call

countdown(3)    # 3 2 1 Go!
```

> ⚠️ Always define a **base case** — without it, recursion never stops and crashes.

---

## 🔢 Useful Built-in Functions

```python
abs(-5)             # 5    — absolute value
round(3.567, 2)     # 3.57 — round to N decimals
min(3, 1, 7)        # 1
max(3, 1, 7)        # 7
sum([1, 2, 3])      # 6
sorted([3,1,2])     # [1, 2, 3]
len("hello")        # 5
```

---

## 🎲 `random` Module

```python
import random

random.randint(1, 10)       # random int between 1 and 10 (inclusive)
random.random()             # random float between 0.0 and 1.0
random.choice(["a","b","c"]) # pick a random element from a list
random.shuffle(my_list)     # shuffle a list in place
```

---

## 🧮 Basic Algorithm Patterns

### Check if a number is prime
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### Find with a flag
```python
def contains_even(numbers):
    found = False
    for n in numbers:
        if n % 2 == 0:
            found = True
            break
    return found
```

### Accumulator pattern
```python
def total_score(scores):
    total = 0
    for s in scores:
        total += s
    return total
```

---

## 🧠 Common Mistakes

| Mistake | Why it breaks | Fix |
|---------|--------------|-----|
| Forgetting `return` | function returns `None` silently | always check what your function should give back |
| Using a variable before assigning it | `NameError` | initialise variables before the loop/condition |
| Infinite recursion | no base case | always define when the recursion stops |
| `random.randint(1,10)` without import | `NameError` | add `import random` at the top |
| Modifying a global inside a function | hard to debug | pass as parameter, return the new value |

---

## ⚡ Quick Reference

```python
import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def guess_game(secret, guess):
    if guess < secret:
        return "Too low"
    elif guess > secret:
        return "Too high"
    else:
        return "Correct!"

secret = random.randint(1, 100)
```
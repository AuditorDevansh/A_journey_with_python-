<div align="center">

```
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
```

# 🐍 Python Fundamentals — The Complete Dev Guide

**Practical-first. Theory when it matters. Built to actually stick.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner%20→%20Intermediate-22c55e?style=for-the-badge)
![Reference](https://img.shields.io/badge/Reference-freeCodeCamp%20Python%20Certification-F1502F?style=for-the-badge&logo=freecodecamp&logoColor=white)
![VisualAlgo](https://img.shields.io/badge/Visualizations-VisualAlgo-6366f1?style=for-the-badge)

> *"Python is not just a language — it's a mindset. Learn it right and everything else clicks faster."*
> — **Dev** | Tech enthusiast<img width="25" height="25" alt="CatComputerGIF" src="https://github.com/user-attachments/assets/c9db1cf8-9499-467d-a498-9d2b4b8a52aa" /> | DSA Grinder ⚔️ | Lifelong Learner 🎯

</div>

---

## 📋 Table of Contents

| # | Section | Jump |
|---|---------|------|
| 01 | What Even Is Python? | [→ Go](#-what-even-is-python) |
| 02 | Variables & Data Types | [→ Go](#-variables--data-types) |
| 03 | Strings — The Full Breakdown | [→ Go](#-strings--the-full-breakdown) |
| 04 | Numbers & Math Operations | [→ Go](#-numbers--math-operations) |
| 05 | Functions | [→ Go](#-functions) |
| 06 | Control Flow — if / elif / else | [→ Go](#-control-flow--if--elif--else) |
| 07 | Loops | [→ Go](#-loops) |
| 08 | Lists | [→ Go](#-lists) |
| 09 | Tuples | [→ Go](#-tuples) |
| 10 | Dictionaries | [→ Go](#-dictionaries) |
| 11 | Sets | [→ Go](#-sets) |
| 12 | Higher-Order Functions | [→ Go](#-higher-order-functions--map-filter-reduce) |
| 13 | OOP — Classes & Objects | [→ Go](#-oop--classes--objects) |
| 14 | Exception Handling | [→ Go](#-exception-handling) |
| 15 | Modules & Standard Library | [→ Go](#-modules--standard-library) |
| 16 | Data Structures & Algorithms | [→ Go](#-data-structures--algorithms) |
| 17 | Dynamic Programming | [→ Go](#-dynamic-programming) |
| 18 | Common Errors & Debugging | [→ Go](#-common-errors--debugging) |
| 19 | References & Resources | [→ Go](#-references--resources) |

---

## 🐍 What Even Is Python?

Python is a **general-purpose, high-level, dynamically typed** programming language. Its syntax reads almost like English — you spend less time fighting the language and more time actually solving problems. That's why it exploded.

```
WHERE PYTHON LIVES:
══════════════════════════════════════════════════════════════
  🔬 Data Science & ML    → NumPy, Pandas, TensorFlow
  🌐 Web Development      → Django, FastAPI, Flask
  🔐 Cybersecurity        → Scripting, Automation, Pentesting
  🤖 Automation           → Selenium, PyAutoGUI
  🍓 Embedded / IoT       → MicroPython, Raspberry Pi
  ☁️  Cloud & DevOps      → AWS Lambda, Boto3, Ansible
══════════════════════════════════════════════════════════════
```

### How Your Code Actually Runs

```
  YOUR CODE (.py file)
          │
          ▼
  ┌───────────────────┐
  │  Python           │  ← Reads your source, checks syntax
  │  Interpreter      │
  └────────┬──────────┘
           │
           ▼
  ┌───────────────────┐
  │  Bytecode (.pyc)  │  ← Converted to intermediate format
  └────────┬──────────┘
           │
           ▼
  ┌───────────────────┐
  │  Python Virtual   │  ← Runs bytecode on your machine
  │  Machine (PVM)    │
  └───────────────────┘
           │
           ▼
         OUTPUT
```

### The REPL — Your Scratchpad

Open terminal → type `python` → hit Enter → you're in.

```
>>> print("Hello, world!")
Hello, world!
>>> 2 + 2
4
>>> type("Dev")
<class 'str'>
```

```
READ  →  you type something
  ↓
EVAL  →  Python interprets it
  ↓
PRINT →  result appears
  ↓
LOOP  →  >>> shows again, ready for next
```

Use the REPL to quickly test ideas, check types, or debug a single expression — don't write full programs here.

---

## 📦 Variables & Data Types

Python is **dynamically typed**. You don't declare a type — Python figures it out from the value you assign.

```python
name    = "Dev"       # str
age     = 21          # int
cgpa    = 7.71        # float
active  = True        # bool
nothing = None        # NoneType
```

No `int x = 10;` nonsense. Just assign and go.

### The Complete Type Map

```
                    ┌─────────────────┐
                    │   DATA TYPES    │
                    └────────┬────────┘
           ┌─────────────────┴─────────────────┐
      ┌────▼────┐                         ┌────▼────┐
      │IMMUTABLE│                         │ MUTABLE │
      │(frozen) │                         │(flexible│
      └────┬────┘                         └────┬────┘
    ┌──────┼───────┐                  ┌────────┼────────┐
    │      │       │                  │        │        │
   int   float   str              list      set      dict
  bool  tuple  None
  range complex
```

**Immutable** = once created in memory, the value cannot change.
**Mutable** = the object can be modified in-place (add, remove, update elements).

### Mutable vs Immutable — What It Actually Means in Memory

This trips up beginners more than anything else. Let's be very clear:

```
IMMUTABLE — variable is just a label pointing to a value
──────────────────────────────────────────────────────────
  x = 10          →  x  ──▶  [10]  (id: 0x1A)
  x = 20          →  x  ──▶  [20]  (id: 0x2B)  ← NEW object
                              [10]  still exists in memory
                                    until garbage collected

  The number 10 never changed. x just points elsewhere now.

MUTABLE — the object itself changes in place
──────────────────────────────────────────────────────────
  my_list = [1, 2, 3]    →  my_list  ──▶  [1, 2, 3]  (id: 0x3C)
  my_list.append(4)      →  my_list  ──▶  [1, 2, 3, 4]  (id: 0x3C)
                                           SAME address, modified

  ⚠️  This is why two variables pointing to the same list
      BOTH see the change — they share the same object.

  a = [1, 2, 3]
  b = a           # b points to the SAME list
  b.append(99)
  print(a)        # [1, 2, 99] ← a changed too! Gotcha.
```

### Type Checking

```python
greeting = "Hello Dev"
age      = 21

print(type(greeting))          # <class 'str'>
print(type(age))               # <class 'int'>
print(isinstance(age, int))    # True
print(isinstance(age, str))    # False  ← clean way to check
```

### Variable Naming Rules

```
✅ VALID                    ❌ INVALID
────────────────────────    ──────────────────────────
my_var     = "ok"           1var      = "nope"  ← starts with number
_private   = "ok"           my-var    = "nope"  ← hyphen not allowed
snake_case = "ok"           class     = "nope"  ← reserved keyword
CONSTANT   = "ok"           my var    = "nope"  ← space not allowed

🏆 Convention: snake_case for variables, UPPER_SNAKE for constants
```

### 🛠 Practice: Type Detective

```python
# Run this and understand every output before moving on
values = [42, 3.14, "hello", True, None, [1,2,3], {"a":1}, (1,2)]

for v in values:
    print(f"{str(v):<15} → type: {type(v).__name__:<10} | mutable: {isinstance(v, (list, dict, set))}")
```

Expected output:
```
42              → type: int        | mutable: False
3.14            → type: float      | mutable: False
hello           → type: str        | mutable: False
True            → type: bool       | mutable: False
None            → type: NoneType   | mutable: False
[1, 2, 3]       → type: list       | mutable: True
{'a': 1}        → type: dict       | mutable: True
(1, 2)          → type: tuple      | mutable: False
```

---

## 🔤 Strings — The Full Breakdown

Strings are **immutable sequences of characters**. Once created, you can't change them — every operation returns a new string.

```python
dev  = 'Devansh'    # single quotes ✅
city = "Meerut"     # double quotes ✅
bio  = """
MCA student.
Salesforce Dev.
Building in public.
"""                  # triple quotes — multiline ✅
```

### String Indexing — Zero-Based, Both Directions

```
  String:  P  y  t  h  o  n
           0  1  2  3  4  5   ← positive (left → right)
          -6 -5 -4 -3 -2 -1   ← negative (right → left)

  s = "Python"
  s[0]    →  'P'
  s[-1]   →  'n'   ← last char without knowing length
  s[2]    →  't'
```

### String Slicing — Extract Any Portion

```
SYNTAX: string[start : stop : step]

  start → where to begin (inclusive)
  stop  → where to end   (exclusive — not included)
  step  → how many to skip (default: 1)

s = "Python is awesome!"

s[0:6]    →  "Python"           ← chars 0,1,2,3,4,5
s[7:]     →  "is awesome!"      ← from 7 to end
s[:6]     →  "Python"           ← from start to 5
s[::2]    →  "Pto saeo!"        ← every other char
s[::-1]   →  "!emosewa si nohtyP"  ← reversed ✅ (interview fav)
s[7:9]    →  "is"
```

### f-Strings — The Modern Way (Use This Always)

```python
name = "Dev"
cgpa = 7.71
uni  = "IGNOU"

# ❌ Old concatenation way (messy):
print("My name is " + name + " CGPA: " + str(cgpa))

# ✅ f-string (clean, readable, fast):
print(f"My name is {name} | CGPA: {cgpa}")
print(f"Studying MCA from {uni.upper()}")   # call methods inside {}
print(f"CGPA rounded: {cgpa:.1f}")          # format numbers inline
print(f"2 + 2 = {2 + 2}")                   # expressions work too
```

Output:
```
My name is Dev | CGPA: 7.71
Studying MCA from IGNOU
CGPA rounded: 7.7
2 + 2 = 4
```

### String Methods Cheat Sheet

```
METHOD            WHAT IT DOES                      EXAMPLE OUTPUT
────────────────────────────────────────────────────────────────────────
.upper()        → All uppercase               "dev"     → "DEV"
.lower()        → All lowercase               "DEV"     → "dev"
.title()        → Capitalize each word        "dev m"   → "Dev M"
.capitalize()   → First char only             "dev m"   → "Dev m"
.strip()        → Remove whitespace (both)    "  hi  "  → "hi"
.lstrip()       → Remove left whitespace      "  hi  "  → "hi  "
.rstrip()       → Remove right whitespace     "  hi  "  → "  hi"
.replace(a,b)   → Replace all a with b        "hi"      → "hello"
.split(sep)     → String → list               "a-b-c"   → ["a","b","c"]
.join(iterable) → List → string               ["a","b"] → "a b"
.find(sub)      → Index of first match        "Dev".find("e") → 1
.count(sub)     → Count occurrences           "aabaa".count("a") → 4
.startswith(s)  → Boolean check at start      "Dev".startswith("D") → True
.endswith(s)    → Boolean check at end        "Dev".endswith("v") → True
.isupper()      → All uppercase?              "DEV".isupper() → True
.islower()      → All lowercase?              "dev".islower() → True
.isdigit()      → All digits?                 "123".isdigit() → True
.isalpha()      → All letters?                "abc".isalpha() → True
```

### ⚠️ Common String Gotchas

```python
# Gotcha 1: strings are immutable — methods return NEW strings
name = "dev"
name.upper()        # does nothing to name
print(name)         # "dev" ← unchanged!
name = name.upper() # ✅ reassign to capture the result
print(name)         # "DEV"

# Gotcha 2: split() without arg splits on ANY whitespace
"  hello   world  ".split()    # ['hello', 'world'] ← clean
"  hello   world  ".split(" ") # ['', '', 'hello', '', '', 'world', '', ''] ← messy

# Gotcha 3: in operator works on substrings
print("is" in "Python is fun")   # True
print("Is" in "Python is fun")   # False ← case sensitive!
```

### 🛠 Practice: String Manipulation

```python
# Build a username generator
full_name  = "  Devansh Mishra  "
university = "IGNOU"
year       = 2024

name_clean = full_name.strip().lower().replace(" ", "_")
username   = f"{name_clean}_{university.lower()}_{str(year)[-2:]}"

print(username)  # devansh_mishra_ignou_24
print(f"Length: {len(username)}")
print(f"Has digits: {any(c.isdigit() for c in username)}")
```

---

## 🔢 Numbers & Math Operations

```python
# Core operators
print(56 + 12)    # 68   → Addition
print(56 - 12)    # 44   → Subtraction
print(56 * 12)    # 672  → Multiplication
print(56 / 12)    # 4.666... → Division  ← ALWAYS returns float
print(56 // 12)   # 4    → Floor Division (round down, int result)
print(56 % 12)    # 8    → Modulo (remainder after division)
print(4 ** 2)     # 16   → Exponentiation
```

### Operator Precedence (PEMDAS in Python)

```
HIGHEST
  │  **          (Exponentiation — right to left)
  │  +x, -x      (Unary plus/minus)
  │  *, /, //, % (Multiplicative)
  │  +, -        (Additive)
LOWEST

Example:
  2 + 3 * 4      →  14   (multiplication first)
  (2 + 3) * 4    →  20   (parentheses win)
  2 ** 3 ** 2    →  512  (right to left: 3**2=9, then 2**9)
```

### Important Number Quirks

```python
# Integer division always rounds DOWN (towards negative infinity)
print(7 // 2)    #  3  (not 3.5)
print(-7 // 2)   # -4  (rounds DOWN, not towards zero!) ← gotcha

# Modulo follows the sign of the DIVISOR
print(7 % 3)     #  1
print(-7 % 3)    #  2  ← not -1! follows divisor's sign

# Float precision — IEEE 754 reality
print(0.1 + 0.2)  # 0.30000000000000004 ← this is normal
print(round(0.1 + 0.2, 2))  # 0.3 ← fix with round()
```

### Type Conversion

```python
int(3.99)      # → 3      (truncates, does NOT round)
int("42")      # → 42     (string → int, must be numeric)
float(10)      # → 10.0
str(42)        # → "42"
bool(0)        # → False
bool("hello")  # → True

round(7.7)     # → 8      (rounds to nearest)
abs(-13)       # → 13     (absolute value)
pow(2, 10)     # → 1024   (2 to the power 10)
```

### Augmented Assignment

```python
x = 10
x += 5     # x = 15   same as x = x + 5
x -= 3     # x = 12
x *= 2     # x = 24
x /= 4     # x = 6.0  ← notice: division gives float
x //= 2    # x = 3.0
x **= 3    # x = 27.0
x %= 5     # x = 2.0
```

### 🛠 Practice: Simple Calculator

```python
def calculator(a, b, op):
    ops = {
        "+":  a + b,
        "-":  a - b,
        "*":  a * b,
        "/":  a / b if b != 0 else "Error: divide by zero",
        "//": a // b if b != 0 else "Error: divide by zero",
        "%":  a % b if b != 0 else "Error: divide by zero",
        "**": a ** b
    }
    return ops.get(op, "Unknown operator")

print(calculator(10, 3, "+"))   # 13
print(calculator(10, 3, "//"))  # 3
print(calculator(10, 0, "/"))   # Error: divide by zero
print(calculator(2, 8, "**"))   # 256
```

---

## ⚙️ Functions

Functions are the backbone of clean code. Write once, reuse everywhere. The moment you find yourself copy-pasting logic — that's your cue to write a function.

```python
# ANATOMY:
#
#  def   → tells Python this is a function definition
#  ↓
def get_sum(num_1, num_2):    # ← parameters (placeholders)
    """Returns the sum of two numbers."""  # ← docstring (document your functions!)
    return num_1 + num_2      # ← return sends value back to caller

result = get_sum(3, 4)        # ← arguments (actual values passed in)
print(result)                 # 7
```

### The Call Stack — What Happens When You Call a Function

```
  main program running...
       │
       │  calls get_sum(3, 4)
       ▼
  ┌────────────────────────┐
  │  STACK FRAME: get_sum  │
  │  num_1 = 3             │  ← local variables live here
  │  num_2 = 4             │
  │  computes: 3 + 4 = 7   │
  │  return 7              │
  └──────────┬─────────────┘
             │  7 returned
             ▼
  main program continues
  result = 7
```

### Parameters — All the Ways to Pass Data

```python
# 1. Positional — order matters
def greet(name, msg):
    print(f"{msg}, {name}!")

greet("Dev", "Hello")          # Hello, Dev!
greet("Hello", "Dev")          # Dev, Hello! ← order matters

# 2. Keyword — name them explicitly, order doesn't matter
greet(msg="Yo", name="Dev")    # Yo, Dev!

# 3. Default — fallback if not provided
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Dev")                   # Hello, Dev!
greet("Dev", "Namaste")        # Namaste, Dev!

# 4. *args — variable number of positional args (tuple)
def total(*nums):
    return sum(nums)

total(1, 2, 3)        # 6
total(10, 20, 30, 40) # 100

# 5. **kwargs — variable number of keyword args (dict)
def show_profile(**info):
    for key, val in info.items():
        print(f"{key}: {val}")

show_profile(name="Dev", cgpa=7.71, uni="IGNOU")
# name: Dev
# cgpa: 7.71
# uni: IGNOU
```

### Scope — Where Variables Live (LEGB Rule)

```
LEGB = Local → Enclosing → Global → Built-in

┌─────────────────────────────────────────────────┐
│  BUILT-IN SCOPE                                 │
│  print, len, type, range, etc. — always there   │
│                                                 │
│  ┌──────────────────────────────────────────┐   │
│  │  GLOBAL SCOPE                            │   │
│  │  tax = 0.18  ← accessible everywhere    │   │
│  │                                          │   │
│  │  ┌────────────────────────────────────┐  │   │
│  │  │  ENCLOSING SCOPE (outer function)  │  │   │
│  │  │  rate = 0.5                        │  │   │
│  │  │  ┌──────────────────────────────┐  │  │   │
│  │  │  │  LOCAL SCOPE (inner func)    │  │  │   │
│  │  │  │  price = 100  ← only here    │  │  │   │
│  │  │  │  can see: price, rate, tax   │  │  │   │
│  │  │  └──────────────────────────────┘  │  │   │
│  │  └────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘

Python looks for a variable in this order: L → E → G → B
If not found anywhere → NameError
```

```python
tax = 0.18   # global

def calculate(price):
    total = price + (price * tax)  # uses global tax ✅
    return total

print(calculate(100))  # 118.0
print(total)           # NameError: total is only local
```

### Lambda — One-Line Anonymous Functions

```python
# Regular function:
def square(x):
    return x * x

# Lambda equivalent:
square = lambda x: x * x     # same thing, one line

# Where lambdas actually shine — as inline arguments:
nums   = [1, 2, 3, 4, 5, 6]
evens  = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4, 6]
double = list(map(lambda x: x * 2, nums))           # [2, 4, 6, 8, 10, 12]

# Sorting with custom key:
students = [("Dev", 7.71), ("Alice", 8.5), ("Bob", 6.9)]
students.sort(key=lambda s: s[1], reverse=True)
# [('Alice', 8.5), ('Dev', 7.71), ('Bob', 6.9)]
```

> 🛑 **Rule:** keep lambdas simple. If you need more than one expression, write a proper `def`.

### 🛠 Practice: Student Grade System

```python
def get_grade(marks):
    """Return letter grade based on marks out of 100."""
    if marks >= 90:   return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    elif marks >= 50: return "D"
    else:             return "F"

def process_results(*scores, student="Unknown"):
    avg   = sum(scores) / len(scores)
    grade = get_grade(avg)
    print(f"Student : {student}")
    print(f"Scores  : {scores}")
    print(f"Average : {avg:.2f}")
    print(f"Grade   : {grade}")

process_results(85, 92, 78, 90, 88, student="Dev")
```

Output:
```
Student : Dev
Scores  : (85, 92, 78, 90, 88)
Average : 86.60
Grade   : A
```

---

## 🔀 Control Flow — if / elif / else

This is how Python makes decisions. Every program you'll ever write depends on this.

```python
age = 16

if age >= 18:
    print("Adult — can vote")
elif age >= 13:
    print("Teenager")         # ← This runs
else:
    print("Child")
```

### The Decision Flow

```
              age = 16
                 │
         ┌───────▼────────┐
         │  age >= 18?    │
         └───┬────────┬───┘
            No        Yes
             │         │
    ┌────────▼────┐   print("Adult")
    │ age >= 13?  │
    └──┬──────┬───┘
      No      Yes
       │        │
  print("Child") print("Teenager")  ← executes
```

### Truthy & Falsy — Python's Hidden Boolean Logic

Everything in Python has a boolean value. You don't always need `== True` or `== False`.

```
FALSY  (behaves like False)    TRUTHY (behaves like True)
─────────────────────────────  ──────────────────────────
False                          True
None                           Any non-zero number
0, 0.0                         Any non-empty string
""   (empty string)            Any non-empty list/dict/set
[]   (empty list)              Any object (by default)
{}   (empty dict)
set()

PRACTICAL USE:
  data = []
  if data:            ← cleaner than: if len(data) > 0
      print("has items")
  else:
      print("empty")  ← prints this
```

### Boolean Operators & Short-Circuiting

```python
# AND — both must be True; stops at first False
is_citizen = True
age = 25
if is_citizen and age >= 18:
    print("Eligible to vote")  # ✅ both True

# OR — at least one True; stops at first True
is_student = True
if age < 18 or is_student:
    print("Eligible for discount")  # ✅ is_student is True

# NOT — flips it
is_admin = False
if not is_admin:
    print("Access Denied")  # ✅

# Short-circuit for safe defaults:
name  = None
label = name or "Anonymous"   # "Anonymous" ← name is falsy
count = 0
total = count or 1            # 1 ← avoid division by zero
```

### Ternary — One-Line Conditions

```python
# Full if-else:
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary (same thing):
status = "adult" if age >= 18 else "minor"
print(status)   # adult

# Nested (keep it readable):
label = "senior" if age >= 60 else ("adult" if age >= 18 else "minor")
```

### 🛠 Practice: Login System

```python
def login(username, password, is_admin=False):
    USERS = {
        "dev":   "pass123",
        "alice": "secret",
    }

    if username not in USERS:
        return "❌ User not found"
    
    if USERS[username] != password:
        return "❌ Wrong password"

    role = "Admin" if is_admin else "User"
    return f"✅ Welcome, {username}! Role: {role}"

print(login("dev", "pass123"))           # ✅ Welcome, dev! Role: User
print(login("dev", "pass123", True))     # ✅ Welcome, dev! Role: Admin
print(login("alice", "wrong"))           # ❌ Wrong password
print(login("ghost", "x"))              # ❌ User not found
```

---

## 🔄 Loops

Loops = automation. Instead of writing the same thing 100 times, you write it once and let the loop do the work.

### for Loop — When You Know What to Iterate

```python
langs = ["Python", "Java", "Rust"]

for lang in langs:
    print(lang)
# Python
# Java
# Rust
```

### range() — Generate Number Sequences

```
range(stop)              → 0 to stop-1
range(start, stop)       → start to stop-1
range(start, stop, step) → custom step

range(5)         →  0, 1, 2, 3, 4
range(1, 6)      →  1, 2, 3, 4, 5
range(0, 11, 2)  →  0, 2, 4, 6, 8, 10
range(10, 0, -2) →  10, 8, 6, 4, 2       ← countdown
```

```python
# Print multiplication table for 5:
for i in range(1, 11):
    print(f"5 × {i:2} = {5*i}")
```

### while Loop — When You Don't Know How Many Times

```python
attempts = 0
MAX = 3
PASSWORD = "python"

while attempts < MAX:
    pwd = input(f"Password (attempt {attempts+1}/{MAX}): ")
    if pwd == PASSWORD:
        print("✅ Access granted!")
        break
    attempts += 1
    print("❌ Wrong. Try again.")
else:
    print("🔒 Locked out after 3 attempts.")
```

### break, continue, else

```
BREAK    → exit loop immediately
CONTINUE → skip this iteration, go to next
ELSE     → runs only if loop completed WITHOUT break

LOOP FLOW:
  ┌──────────────────────────────────────┐
  │  for item in collection:             │
  │      if condition_A:                 │
  │          break       ──────────────▶ exits loop
  │      if condition_B:                 │
  │          continue    ──────┐         │
  │      # normal code         │ back to │
  │                       ─────┘ next   │
  └──────────────────────────────────────┘
  else:  ← runs if no break happened
      print("loop finished cleanly")
```

### enumerate() and zip() — Power Moves

```python
# enumerate() — get index + value together
langs = ["Python", "Java", "Rust"]
for i, lang in enumerate(langs, start=1):
    print(f"{i}. {lang}")
# 1. Python
# 2. Java
# 3. Rust

# zip() — walk multiple lists in sync
names  = ["Dev", "Alice", "Bob"]
scores = [92, 85, 78]
for name, score in zip(names, scores):
    grade = "Pass" if score >= 80 else "Fail"
    print(f"{name}: {score} → {grade}")
# Dev: 92 → Pass
# Alice: 85 → Pass
# Bob: 78 → Fail
```

### List Comprehension — Pythonic Shorthand

```python
# Normal way:
squares = []
for n in range(1, 6):
    squares.append(n ** 2)

# Comprehension:
squares = [n ** 2 for n in range(1, 6)]
# [1, 4, 9, 16, 25]

# With filter condition:
evens = [n for n in range(20) if n % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested — flatten a 2D list:
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat   = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 🛠 Practice: Attendance Tracker

```python
students = ["Dev", "Alice", "Bob", "Carol", "Dan"]
present  = ["Dev", "Bob", "Carol"]

print("📋 Attendance Report")
print("─" * 30)
for i, student in enumerate(students, 1):
    status = "✅ Present" if student in present else "❌ Absent"
    print(f"{i}. {student:<10} {status}")

attendance_pct = (len(present) / len(students)) * 100
print(f"\nAttendance: {len(present)}/{len(students)} ({attendance_pct:.0f}%)")
```

Output:
```
📋 Attendance Report
──────────────────────────────
1. Dev        ✅ Present
2. Alice      ❌ Absent
3. Bob        ✅ Present
4. Carol      ✅ Present
5. Dan        ❌ Absent

Attendance: 3/5 (60%)
```

---

## 📋 Lists

Lists are **ordered, mutable, zero-indexed** collections. The most-used data structure in Python — you'll use them constantly.

```python
cities = ["Meerut", "Agra", "Delhi", "Mumbai"]

cities[0]     # "Meerut"   ← first
cities[-1]    # "Mumbai"   ← last (always, regardless of size)
cities[1:3]   # ["Agra", "Delhi"]  ← slicing
len(cities)   # 4
```

### Memory Layout

```
  Index:    0          1          2          3
         ┌──────────┬──────────┬──────────┬──────────┐
  List:  │ "Meerut" │ "Agra"   │ "Delhi"  │"Mumbai"  │
         └──────────┴──────────┴──────────┴──────────┘
  Neg:      -4         -3         -2         -1
```

### All the Methods You'll Actually Use

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Adding
nums.append(7)          # [3,1,4,1,5,9,2,6,7]   ← add to end, O(1)
nums.insert(0, 99)      # [99,3,1,4,1,5,9,2,6,7] ← insert at index, O(n)
nums.extend([10, 11])   # adds multiple at end (vs append which nests)

# Removing
nums.remove(1)          # removes FIRST occurrence of 1 only
nums.pop()              # removes & returns last → 7
nums.pop(0)             # removes & returns index 0 → 99
del nums[2]             # delete by index, no return

# Searching
nums.index(5)           # → index of 5 (ValueError if not found)
5 in nums               # → True/False
nums.count(1)           # → how many 1s

# Sorting
nums.sort()             # sorts IN PLACE, returns None
nums.sort(reverse=True) # descending
sorted(nums)            # returns NEW sorted list, original untouched

# Other
nums.reverse()          # reverses IN PLACE
nums.copy()             # shallow copy ← use this to avoid shared ref
nums.clear()            # empties list → []
```

### ⚠️ The Copy Trap

```python
# WRONG — both point to same list:
a = [1, 2, 3]
b = a
b.append(4)
print(a)   # [1, 2, 3, 4] ← a changed too! Not what you wanted.

# RIGHT — use .copy() or list()
a = [1, 2, 3]
b = a.copy()   # or: b = list(a)  or: b = a[:]
b.append(4)
print(a)   # [1, 2, 3]   ← safe
print(b)   # [1, 2, 3, 4]
```

### Time Complexities

```
OPERATION             COMPLEXITY   NOTE
──────────────────────────────────────────────────────
Access by index        O(1)        Instant always
Append to end          O(1)*       *O(n) when resizing
Insert at beginning    O(n)        Shifts everything right
Insert in middle       O(n)        Shifts elements after
Delete from end        O(1)        Fast
Delete from middle     O(n)        Shifts elements left
Search (x in list)     O(n)        Scans every element
Sort                   O(n log n)  Timsort (Python built-in)
```

> 🔗 **Visualize array operations:** [VisualAlgo — Array](https://visualgo.net/en/array)

### 🛠 Practice: To-Do List

```python
def todo_app():
    tasks = []

    def add(task):
        tasks.append({"task": task, "done": False})
        print(f"✅ Added: '{task}'")

    def complete(index):
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"✔️  Completed: '{tasks[index]['task']}'")

    def show():
        print("\n📋 TO-DO LIST")
        for i, t in enumerate(tasks):
            mark = "✔" if t["done"] else "○"
            print(f"  {i}. [{mark}] {t['task']}")

    add("Study Python")
    add("Build Salesforce project")
    add("Push to GitHub")
    complete(0)
    show()

todo_app()
```

---

## 📌 Tuples

Tuples are **ordered, immutable** collections. Think of them as "frozen lists" — same indexed access, but you can't modify them after creation.

```python
dev_info = ("Dev", 21, "MCA", "IGNOU")

dev_info[0]    # "Dev"
dev_info[-1]   # "IGNOU"
dev_info[1:3]  # (21, "MCA")

# Attempt to modify → crash:
dev_info[0] = "Devansh"   # TypeError: 'tuple' object does not support item assignment
```

### When to Use Tuple vs List

```
USE TUPLE WHEN:                         USE LIST WHEN:
────────────────────────────────        ────────────────────────────────
Data is fixed, shouldn't change         Data needs to grow/shrink
Return multiple values from func        Shopping cart, dynamic queue
Used as dictionary key (hashable)       Data will be sorted/filtered
Coordinates, RGB values, dates          Any collection you'll mutate
Slightly faster than list               Default for sequences of items
```

### Packing & Unpacking — Python's Secret Weapon

```python
# Packing — multiple values into a tuple:
point = 10, 20, 30     # parentheses optional
print(type(point))     # <class 'tuple'>

# Unpacking — tuple into individual variables:
x, y, z = point
print(x, y, z)         # 10 20 30

# Starred unpacking — catch the rest:
first, *middle, last = (1, 2, 3, 4, 5)
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5

# Functions returning multiple values (it's a tuple!):
def get_stats(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

lo, hi, avg = get_stats([4, 8, 2, 9, 1])
print(lo, hi, avg)  # 1 9 4.8
```

### 🛠 Practice: Coordinate System

```python
def distance(p1, p2):
    """Euclidean distance between two (x, y) points."""
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2) ** 0.5

origin = (0, 0)
point  = (3, 4)
print(f"Distance: {distance(origin, point)}")  # Distance: 5.0

# Swap without temp variable — classic tuple trick:
a, b = 10, 20
a, b = b, a
print(a, b)   # 20 10
```

---

## 🗂️ Dictionaries

Dictionaries store **key-value pairs**. Keys must be unique and immutable; values can be anything. The go-to structure when data has labels/names.

```python
dev = {
    "name"   : "Devansh Mishra",
    "cgpa"   : 7.71,
    "skills" : ["Apex", "LWC", "React"],
    "active" : True
}

dev["name"]              # "Devansh Mishra"
dev["skills"]            # ["Apex", "LWC", "React"]
dev.get("age", "N/A")    # "N/A" ← safe access, no KeyError
dev["city"] = "Meerut"   # add new key
dev["cgpa"] = 7.9        # update existing key
```

### How Hashing Works Under the Hood

```
When you set  dev["name"] = "Dev" :

  "name" → hash() → some integer → index in array
                                        ↓
  Internal array:  [..., "Dev", ..., ...]
                          ↑
                   stored here

When you read  dev["name"] :
  "name" → same hash → same index → retrieve "Dev"

This is why lookups are O(1) — no scanning needed.
Keys must be immutable (str, int, tuple) because their hash must stay constant.
```

### All the Methods You Need

```python
d = {"a": 1, "b": 2, "c": 3}

d.keys()           # dict_keys(['a', 'b', 'c'])
d.values()         # dict_values([1, 2, 3])
d.items()          # dict_items([('a',1), ('b',2), ('c',3)])
d.get("x", 0)      # 0 ← default instead of KeyError
d.update({"d": 4}) # merge another dict in
d.pop("a")         # removes "a", returns 1
d.popitem()        # removes & returns last inserted pair (Python 3.7+)
d.setdefault("e", 0)  # sets "e":0 only if "e" not already in dict
"b" in d           # True ← checks keys, O(1)
```

### Looping Dictionaries

```python
products = {"Laptop": 990, "Phone": 600, "Tablet": 250}

# Keys only (default):
for product in products:
    print(product)

# Values only:
for price in products.values():
    print(price)

# Both at once:
for product, price in products.items():
    tax   = price * 0.18
    total = price + tax
    print(f"{product:<10} ₹{price} + ₹{tax:.0f} GST = ₹{total:.0f}")
```

Output:
```
Laptop     ₹990 + ₹178 GST = ₹1168
Phone      ₹600 + ₹108 GST = ₹708
Tablet     ₹250 + ₹45 GST  = ₹295
```

### Dictionary Comprehension

```python
# Standard:
squared = {}
for n in range(1, 6):
    squared[n] = n ** 2

# Comprehension:
squared = {n: n**2 for n in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With filter:
even_sq = {n: n**2 for n in range(1, 11) if n % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

> 🔗 **Visualize hash maps:** [VisualAlgo — Hash Table](https://visualgo.net/en/hashtable)

### 🛠 Practice: Word Frequency Counter

```python
def word_count(text):
    words  = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

text = "python is great python is easy to learn python is fun"
freq = word_count(text)
for word, count in freq.items():
    bar = "█" * count
    print(f"{word:<10} {bar} ({count})")
```

Output:
```
python     ███ (3)
is         ███ (3)
great      █ (1)
easy       █ (1)
to         █ (1)
learn      █ (1)
fun        █ (1)
```

---

## 🔵 Sets

Sets store **unique, unordered** elements. Two superpowers: instant duplicate removal and mathematical set operations.

```python
# Automatic duplicate removal:
skills = {"Python", "JS", "Python", "Apex", "JS"}
print(skills)   # {'Python', 'JS', 'Apex'} ← duplicates gone

# Set from a list (most common use):
nums    = [1, 2, 2, 3, 3, 3, 4]
unique  = set(nums)
print(unique)   # {1, 2, 3, 4}

# ⚠️  Empty set must use set(), not {}:
empty_set  = set()   # ✅ set
empty_dict = {}      # ❌ this is a dict, not a set!
```

### Set Operations — Where Sets Really Shine

```python
backend  = {"Python", "Java", "Go", "Rust"}
frontend = {"JavaScript", "TypeScript", "Python", "CSS"}

# Union — everything in either:
print(backend | frontend)
# {'Python', 'Java', 'Go', 'Rust', 'JavaScript', 'TypeScript', 'CSS'}

# Intersection — only in both:
print(backend & frontend)
# {'Python'}

# Difference — in backend but NOT frontend:
print(backend - frontend)
# {'Java', 'Go', 'Rust'}

# Symmetric Difference — in either, but NOT both:
print(backend ^ frontend)
# {'Java', 'Go', 'Rust', 'JavaScript', 'TypeScript', 'CSS'}

# Subset / Superset check:
web = {"Python", "JavaScript"}
print(web.issubset(backend | frontend))   # True
```

```
Venn Diagram:

  backend            frontend
  ┌────────────┐   ┌────────────┐
  │ Java  Go   │   │  JS  CSS   │
  │ Rust  ┌────┼───┼────┐ TS    │
  │       │ Py │   │    │       │
  │       └────┼───┼────┘       │
  └────────────┘   └────────────┘
               ↑
          Intersection
```

### 🛠 Practice: Find Common Friends

```python
dev_friends   = {"Alice", "Bob", "Carol", "Dan", "Eve"}
alice_friends = {"Bob", "Charlie", "Dan", "Frank", "Eve"}

common    = dev_friends & alice_friends
only_dev  = dev_friends - alice_friends
only_alice= alice_friends - dev_friends

print(f"Common friends    : {common}")
print(f"Only Dev knows    : {only_dev}")
print(f"Only Alice knows  : {only_alice}")
print(f"Total unique      : {len(dev_friends | alice_friends)} people")
```

---

## 🔁 Higher-Order Functions — map, filter, reduce

These are functions that take **other functions as arguments**. Combined with lambda, they let you process collections in clean one-liners.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### map() — Apply a Function to Every Element

```python
# Transform every element:
squared = list(map(lambda x: x**2, nums))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# With a real function:
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius = [0, 20, 37, 100]
fahrenheit = list(map(celsius_to_fahrenheit, celsius))
# [32.0, 68.0, 98.6, 212.0]
```

### filter() — Keep Elements That Pass a Test

```python
evens  = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4, 6, 8, 10]

words = ["tree", "sky", "mountain", "river", "sun"]
long  = list(filter(lambda w: len(w) > 4, words))
# ['mountain', 'river']
```

### reduce() — Collapse a Collection to a Single Value

```python
from functools import reduce

total   = reduce(lambda acc, x: acc + x, nums)   # 55
product = reduce(lambda acc, x: acc * x, [1,2,3,4,5])  # 120

# How it works step by step for sum:
# Step 1: acc=1,  x=2  → 3
# Step 2: acc=3,  x=3  → 6
# Step 3: acc=6,  x=4  → 10
# Step 4: acc=10, x=5  → 15  ← final result
```

### map vs filter vs list comprehension — When to Use What

```
SITUATION                          PREFERRED
──────────────────────────────────────────────────────
Transform every element            map() or comprehension
Filter elements                    filter() or comprehension
Simple, readable logic             List comprehension
Complex multi-step logic           Regular for loop
Chaining multiple operations       map + filter or generator
Reduce to a single value           reduce()

READABILITY TEST:
  [x**2 for x in nums if x % 2 == 0]   ← clear at a glance ✅
  list(map(lambda x: x**2, filter(lambda x: x%2==0, nums)))  ← harder to read ❌
```

---

## 🏗️ OOP — Classes & Objects

OOP is how you model real-world things in code. A **class** is the blueprint; an **object** is the actual instance built from it.

```
CLASS  →  Blueprint (like a cookie cutter)
OBJECT →  Instance  (like the actual cookie)

  class Laptop:          ← blueprint
      brand = "Generic"

  my_laptop = Laptop()   ← object (instance)
```

### Building a Class — Full Anatomy

```python
class Student:
    # Class attribute — shared by ALL instances
    institution = "IGNOU"

    # Constructor — runs when object is created
    def __init__(self, name, cgpa):
        self.name = name    # instance attribute — unique per object
        self.cgpa = cgpa

    # Instance method
    def get_grade(self):
        if self.cgpa >= 8.0:   return "Distinction"
        elif self.cgpa >= 6.0: return "First Class"
        elif self.cgpa >= 5.0: return "Second Class"
        else:                  return "Pass"

    # String representation — what print() shows
    def __str__(self):
        return f"{self.name} | CGPA: {self.cgpa} | {self.get_grade()}"

# Creating objects:
dev   = Student("Dev", 7.71)
alice = Student("Alice", 8.5)

print(dev)              # Dev | CGPA: 7.71 | First Class
print(alice)            # Alice | CGPA: 8.5 | Distinction
print(Student.institution)  # IGNOU  ← class attribute via class name
print(dev.institution)      # IGNOU  ← also accessible via instance
```

### The 4 Pillars of OOP

```
╔══════════════╦════════════════════════════════════════════════╗
║ PILLAR       ║ WHAT IT MEANS                                  ║
╠══════════════╬════════════════════════════════════════════════╣
║ Encapsulation║ Bundle data + methods. Hide internals.         ║
║              ║ Only expose what users need.                   ║
╠══════════════╬════════════════════════════════════════════════╣
║ Inheritance  ║ Child class gets parent's attributes/methods.  ║
║              ║ Promotes reuse. Add/override as needed.        ║
╠══════════════╬════════════════════════════════════════════════╣
║ Polymorphism ║ Same method name, different behavior per class.║
║              ║ Works via method overriding.                   ║
╠══════════════╬════════════════════════════════════════════════╣
║ Abstraction  ║ Hide complexity. Show only what's needed.      ║
║              ║ Car pedals vs engine internals.                ║
╚══════════════╩════════════════════════════════════════════════╝
```

### Inheritance — Code Reuse in Action

```
        ┌─────────────┐
        │   Person    │  ← Base / Parent class
        │  name, age  │
        │  .greet()   │
        └──────┬──────┘
               │ inherits
       ┌───────┴────────┐
       │                │
┌──────▼──────┐  ┌──────▼──────┐
│   Student   │  │   Teacher   │  ← Child classes
│  .cgpa      │  │  .subject   │
│  .study()   │  │  .teach()   │
│  .greet() ✅│  │  .greet() ✅│  ← inherited
└─────────────┘  └─────────────┘
```

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def greet(self):
        return f"Hi, I'm {self.name}, {self.age} years old."

class Student(Person):
    def __init__(self, name, age, cgpa):
        super().__init__(name, age)   # call parent constructor
        self.cgpa = cgpa

    def study(self):
        return f"{self.name} is studying. CGPA: {self.cgpa}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        return f"{self.name} teaches {self.subject}."

dev     = Student("Dev", 21, 7.71)
prof    = Teacher("Dr. Sharma", 45, "Python")

print(dev.greet())    # Hi, I'm Dev, 21 years old.   ← inherited
print(dev.study())    # Dev is studying. CGPA: 7.71
print(prof.teach())   # Dr. Sharma teaches Python.
```

### Encapsulation — Protecting Data

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner    = owner
        self.__balance = balance   # __ = private (name mangled to _BankAccount__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount}. Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrew ₹{amount}. Balance: ₹{self.__balance}")
        else:
            print("❌ Insufficient balance.")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Dev", 5000)
acc.deposit(2000)       # ✅ Deposited ₹2000. Balance: ₹7000
acc.withdraw(10000)     # ❌ Insufficient balance.
print(acc.__balance)    # AttributeError ← can't access directly
print(acc.get_balance()) # 7000 ← use the public method
```

### Dunder (Magic) Methods

Python calls these automatically behind the scenes. You override them to customize behavior.

```python
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):       # len(cart)
        return len(self.items)

    def __str__(self):       # print(cart)
        return f"Cart({self.items})"

    def __contains__(self, item):   # "item" in cart
        return item in self.items

    def __iter__(self):      # for item in cart
        return iter(self.items)

cart = Cart()
cart.add("Laptop")
cart.add("Keyboard")

print(len(cart))              # 2
print("Laptop" in cart)       # True
print(cart)                   # Cart(['Laptop', 'Keyboard'])
for item in cart:
    print(f"  - {item}")
```

---

## 🛡️ Exception Handling

Errors happen. Good code handles them gracefully instead of crashing with an ugly traceback.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
```

### The Full Structure

```
try:
    ← code that might raise an exception

except SpecificError:
    ← runs if that specific error occurs

except (TypeError, ValueError) as e:
    ← catch multiple errors; use 'e' to inspect the error

else:
    ← runs ONLY if try succeeded (no exception)

finally:
    ← ALWAYS runs — use for cleanup (close files, DB connections)
```

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"❌ Wrong type: {e}")
        return None
    else:
        print(f"✅ Result: {result}")
        return result
    finally:
        print("   (division attempted)")

safe_divide(10, 2)    # ✅ Result: 5.0 / (division attempted)
safe_divide(10, 0)    # ❌ Cannot divide by zero / (division attempted)
safe_divide("a", 2)   # ❌ Wrong type / (division attempted)
```

### Exception Hierarchy — Know What to Catch

```
BaseException
  ├── SystemExit              ← sys.exit() call
  ├── KeyboardInterrupt       ← Ctrl+C
  └── Exception               ← catch all normal errors here
        ├── ValueError        ← bad value (int("abc"))
        ├── TypeError         ← wrong type (1 + "2")
        ├── KeyError          ← dict key not found
        ├── IndexError        ← list index out of range
        ├── AttributeError    ← method/attr doesn't exist
        ├── FileNotFoundError ← file doesn't exist
        ├── ZeroDivisionError ← divided by zero
        └── ImportError       ← module not found
```

### Custom Exceptions

```python
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.message = f"Tried to withdraw ₹{amount} but balance is ₹{balance}"
        super().__init__(self.message)

def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

try:
    new_balance = withdraw(5000, 2000)
except InsufficientFundsError as e:
    print(f"❌ {e}")
```

Output: `❌ Tried to withdraw ₹5000 but balance is ₹2000`

---

## 📦 Modules & Standard Library

A **module** is just a Python file. The **standard library** is Python's built-in collection of modules — no install needed.

### Import Patterns

```python
# Full import — access with module.function()
import math
print(math.sqrt(144))   # 12.0
print(math.pi)          # 3.14159...

# Import with alias — shorter name
import math as m
print(m.floor(3.9))     # 3

# Import specific items — use directly, no prefix
from math import sqrt, pi, factorial
print(sqrt(64))         # 8.0
print(factorial(5))     # 120

# ⚠️  Avoid: from math import *  ← pollutes namespace
```

### The Standard Library Modules You'll Use Most

```
MODULE          USE CASE                       KEY FUNCTIONS
──────────────────────────────────────────────────────────────────
math            Math operations                sqrt, floor, ceil, pi
random          Random numbers & choices       random, randint, choice, shuffle
datetime        Dates, times, formatting       datetime.now(), strftime
os              File system, paths             getcwd, listdir, path.join
sys             System info                    argv, exit, version
json            Read/write JSON                loads, dumps, load, dump
re              Regular expressions            match, search, findall, sub
collections     Specialized containers         Counter, defaultdict, deque
itertools       Efficient iteration            chain, product, combinations
functools       Higher-order functions         reduce, partial, lru_cache
```

### Quick Examples

```python
import random
import datetime
from collections import Counter

# random — pick random items
print(random.randint(1, 100))              # random int 1-100
print(random.choice(["rock","paper","scissors"]))
items = [1,2,3,4,5]
random.shuffle(items)
print(items)                               # shuffled

# datetime — current time
now = datetime.datetime.now()
print(now.strftime("%d %B %Y, %I:%M %p")) # 15 June 2026, 02:30 PM

# Counter — count occurrences in one line
marks = [85, 92, 85, 78, 92, 92, 85, 70]
freq  = Counter(marks)
print(freq)         # Counter({92: 3, 85: 3, 78: 1, 70: 1})
print(freq.most_common(2))  # [(92, 3), (85, 3)]
```

### 🛠 Practice: Mini File Manager

```python
import os
import json

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved to {filename}")

def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ {filename} not found. Starting fresh.")
        return {}

students = {"Dev": 7.71, "Alice": 8.5, "Bob": 6.9}
save_data("students.json", students)

loaded = load_data("students.json")
print(loaded)  # {'Dev': 7.71, 'Alice': 8.5, 'Bob': 6.9}
```

---

## 🧮 Data Structures & Algorithms

### Big O — How Algorithms Scale

Big O is about **growth rate**, not exact speed. It answers: "as input gets bigger, how much slower does this get?"

```
COMPLEXITY   NAME           REAL EXAMPLE
────────────────────────────────────────────────────────────
O(1)         Constant       dict lookup, list access by index
O(log n)     Logarithmic    Binary search (halves each time)
O(n)         Linear         Loop through list once
O(n log n)   Log-linear     Merge sort, Python's sort()
O(n²)        Quadratic      Nested loops (bubble sort)
O(2ⁿ)        Exponential    Naive Fibonacci recursion

n=1000:
  O(1)      → 1 operation
  O(log n)  → ~10 operations
  O(n)      → 1,000 operations
  O(n log n)→ ~10,000 operations
  O(n²)     → 1,000,000 operations   ← gets painful fast
```

### Stacks — LIFO

```
Last In, First Out. Think: undo history, browser back button.

PUSH               POP
  │                 ↑
┌─▼─┐            ┌─┴─┐
│ 3 │ ← TOP      │ 3 │  ← leaves first
├───┤            ├───┤
│ 2 │            │ 2 │
├───┤            ├───┤
│ 1 │            │ 1 │
└───┘            └───┘
```

```python
stack = []
stack.append("action_1")  # push
stack.append("action_2")
stack.append("action_3")

last = stack.pop()         # "action_3" ← LIFO
print(stack)               # ["action_1", "action_2"]

# Real use: undo functionality
undo_stack = []
def do_action(action):
    undo_stack.append(action)
    print(f"Did: {action}")

def undo():
    if undo_stack:
        print(f"Undone: {undo_stack.pop()}")

do_action("type 'Hello'")
do_action("bold text")
undo()   # Undone: bold text
```

> 🔗 [VisualAlgo — Stack](https://visualgo.net/en/list)

### Queues — FIFO

```
First In, First Out. Think: print queue, task scheduler, BFS.

ENQUEUE →  [1][2][3]  → DEQUEUE
 (back)     front ↑
```

```python
from collections import deque   # use deque, not list (O(1) popleft)

queue = deque()
queue.append("task_1")   # enqueue to back
queue.append("task_2")
queue.append("task_3")

next_task = queue.popleft()   # "task_1" ← FIFO
print(queue)                  # deque(['task_2', 'task_3'])
```

> 🔗 [VisualAlgo — Queue](https://visualgo.net/en/list)

### Linked Lists

```
SINGLY — each node points to next only:

 HEAD
 ┌───────┐     ┌───────┐     ┌───────┐
 │data: 1│──▶  │data: 2│──▶  │data: 3│──▶ None
 └───────┘     └───────┘     └───────┘

DOUBLY — each node points both ways:

 HEAD
 ┌───────┐  ◀▶  ┌───────┐  ◀▶  ┌───────┐
 │   1   │      │   2   │      │   3   │──▶ None
 └───────┘      └───────┘      └───────┘
```

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        nodes, curr = [], self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        print(" → ".join(nodes) + " → None")

ll = LinkedList()
ll.append(1); ll.append(2); ll.append(3)
ll.display()   # 1 → 2 → 3 → None
```

```
COMPLEXITY COMPARISON:
                  Array/List   Linked List
──────────────────────────────────────────
Access by index    O(1)         O(n)
Insert at front    O(n)         O(1)
Insert at end      O(1)         O(n)*
Search             O(n)         O(n)
Memory             Contiguous   Non-contiguous (pointers overhead)
```

> 🔗 [VisualAlgo — Linked List](https://visualgo.net/en/list)

### Binary Search

Only works on **sorted arrays**. The idea: compare with middle → eliminate half → repeat.

```
Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        0  1  2  3  4   5   6   7   8   9
Target: 13

Step 1: lo=0, hi=9, mid=4 → arr[4]=9  < 13 → search RIGHT
Step 2: lo=5, hi=9, mid=7 → arr[7]=15 > 13 → search LEFT
Step 3: lo=5, hi=6, mid=5 → arr[5]=11 < 13 → search RIGHT
Step 4: lo=6, hi=6, mid=6 → arr[6]=13 == 13 → FOUND ✅

Each step halves the search space → O(log n)
10 elements → max 4 steps
1,000,000 elements → max 20 steps  ← insane efficiency
```

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid             # found at index mid
        elif arr[mid] < target:
            lo = mid + 1           # target is in right half
        else:
            hi = mid - 1           # target is in left half

    return -1                      # not found

nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(nums, 13))   # 6
print(binary_search(nums, 4))    # -1
```

> 🔗 [VisualAlgo — Binary Search](https://visualgo.net/en/bst)

### Sorting Algorithms

```
ALGORITHM     BEST      AVERAGE    WORST     SPACE   STABLE?
──────────────────────────────────────────────────────────────
Bubble Sort   O(n)      O(n²)      O(n²)     O(1)    Yes
Selection     O(n²)     O(n²)      O(n²)     O(1)    No
Insertion     O(n)      O(n²)      O(n²)     O(1)    Yes
Merge Sort    O(nlogn)  O(nlogn)   O(nlogn)  O(n)    Yes
Quick Sort    O(nlogn)  O(nlogn)   O(n²)     O(logn) No
Heap Sort     O(nlogn)  O(nlogn)   O(nlogn)  O(1)    No
Python sort() O(n)      O(nlogn)   O(nlogn)  O(n)    Yes ← Timsort
```

```
MERGE SORT — Divide & Conquer Visualized:

  [5, 3, 8, 1, 9, 2]          ← original
          │
       DIVIDE
  ┌─────┴──────┐
[5, 3, 8]   [1, 9, 2]         ← split in half
  │               │
[5,3] [8]   [1,9] [2]         ← split again
  │    │      │    │
[5][3][8]   [1][9][2]         ← single elements (base case)
      │             │
    MERGE         MERGE
  [3, 5, 8]    [1, 2, 9]      ← sorted halves
          │
        MERGE
   [1, 2, 3, 5, 8, 9]         ← final ✅
```

> 🔗 [VisualAlgo — Sorting](https://visualgo.net/en/sorting)

### Trees & Graphs

```
BINARY SEARCH TREE (BST):       Rule: left < parent < right

             8
           /   \
          3     10
         / \      \
        1   6      14
           / \    /
          4   7  13

Search 7:
  Start at 8 → 7 < 8 → go left
  At 3 → 7 > 3 → go right
  At 6 → 7 > 6 → go right
  At 7 → FOUND ✅   (O(log n) for balanced tree)
```

```
GRAPH TRAVERSALS:

BFS (Breadth-First)         DFS (Depth-First)
→ Level by level             → Branch fully first
→ Uses QUEUE                 → Uses STACK / recursion
→ Shortest path              → Cycle detection, mazes

  A ─ B ─ D                  A ─ B ─ D
  │   │                      │   │
  C ─ E                      C ─ E

BFS from A: A, B, C, D, E   DFS from A: A, B, D, E, C
```

> 🔗 [VisualAlgo — Graph](https://visualgo.net/en/graphds) | [VisualAlgo — BST](https://visualgo.net/en/bst)

---

## ⚡ Dynamic Programming

DP = **store results of subproblems to avoid recalculating them**. It's the difference between O(2ⁿ) and O(n).

Two conditions for DP to apply:
- **Overlapping subproblems** — same smaller problems appear multiple times
- **Optimal substructure** — best solution built from best sub-solutions

```
NAIVE FIBONACCI — O(2ⁿ):

fib(5)
  ├── fib(4)
  │     ├── fib(3)  ← computed AGAIN
  │     │     ├── fib(2)
  │     │     └── fib(1)
  │     └── fib(2)  ← computed AGAIN
  └── fib(3)  ← computed AGAIN
        ├── fib(2)
        └── fib(1)

For fib(40): 2⁴⁰ = ~1 trillion operations 😱

DP WITH MEMOIZATION — O(n):
fib(5)
  ├── fib(4)
  │     ├── fib(3) → compute & STORE → memo[3] = 2
  │     └── fib(2) → compute & STORE → memo[2] = 1
  └── fib(3) → READ from memo ✅ (instant)

For fib(40): 40 operations 🚀
```

### Memoization — Top-Down (Cache as You Go)

```python
def fib_memo(n, memo={}):
    if n in memo:        # already solved? instant return
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Using functools for cleaner memoization:
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)

print(fib(50))   # 12586269025 (instant)
```

### Tabulation — Bottom-Up (Fill the Table)

```python
def fib_tab(n):
    if n <= 2: return 1
    dp    = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]   # build up from known values
    return dp[n]

# TABLE for fib(8):
#  i │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8
# ───┼───┼───┼───┼───┼───┼───┼───┼───┼───
# dp │ 0 │ 1 │ 1 │ 2 │ 3 │ 5 │ 8 │13 │21

print(fib_tab(8))   # 21
```

### When to Reach for DP

```
SIGNALS THAT DP MIGHT HELP:
─────────────────────────────────────────────────────────
✅ "Minimum/maximum number of steps/coins/moves"
✅ "Count the number of ways to do X"
✅ "Can we achieve X with given constraints"
✅ You see the same recursive call with same args
✅ Naive recursion gives Time Limit Exceeded on LeetCode

COMMON DP PROBLEMS:
  - Fibonacci / Climbing Stairs
  - 0/1 Knapsack
  - Longest Common Subsequence
  - Coin Change
  - Edit Distance
```

---

## 🐛 Common Errors & Debugging

Knowing error types = faster debugging. Here's every error you'll hit as a beginner:

```
ERROR TYPE        CAUSE                           QUICK FIX
─────────────────────────────────────────────────────────────────────
SyntaxError       Code doesn't follow Python      Check brackets, colons,
                  grammar rules                   indentation
NameError         Using a variable before         Define variable first;
                  defining it                     check spelling
TypeError         Wrong type for operation        Check types; use int(),
                  ("hi" + 3)                      str() conversion
IndexError        Index out of list range         Check list length; use
                  (list[10] on len-5 list)        negative index or len()-1
KeyError          Dict key doesn't exist          Use .get(key, default)
                                                  instead of dict[key]
ValueError        Right type, wrong value         Validate input; wrap in
                  (int("abc"))                    try/except
AttributeError    Method doesn't exist on type    Check type with type();
                  ("hello".append("!"))           check Python docs
ZeroDivisionError Dividing by zero                Add "if b != 0" guard
IndentationError  Wrong indentation               Use 4 spaces consistently;
                                                  don't mix tabs & spaces
RecursionError    Infinite recursion              Add base case; check logic
```

### Debugging Techniques

```python
# 1. print() debugging — quick and dirty
def buggy_func(nums):
    total = 0
    for n in nums:
        print(f"  n={n}, total before={total}")   # debug line
        total += n
    print(f"  final total={total}")               # debug line
    return total

# 2. Using assert — catch assumptions early
def get_average(nums):
    assert len(nums) > 0, "List cannot be empty!"  # crashes with message if false
    return sum(nums) / len(nums)

# 3. type() and isinstance() — when you're unsure what you have
data = get_data_from_somewhere()
print(type(data))           # find out what it is
print(isinstance(data, list))  # check before using list methods

# 4. The try/except + print combo — production-safe debug
try:
    result = risky_operation()
except Exception as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
```

---

## 📚 References & Resources

### Primary Reference

> This guide is based on the **freeCodeCamp Python Certification Course** — one of the most thorough free Python resources out there. Everything here maps directly to that curriculum with added practical depth.
>
> 🔗 [freeCodeCamp — Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/)

### Algorithm Visualizations — VisualAlgo

| Topic | Link |
|-------|------|
| Sorting (Bubble, Merge, Quick) | [visualgo.net/en/sorting](https://visualgo.net/en/sorting) |
| Array operations | [visualgo.net/en/array](https://visualgo.net/en/array) |
| Stack, Queue, Linked List | [visualgo.net/en/list](https://visualgo.net/en/list) |
| Binary Search Tree | [visualgo.net/en/bst](https://visualgo.net/en/bst) |
| Hash Table | [visualgo.net/en/hashtable](https://visualgo.net/en/hashtable) |
| Graph traversals (BFS, DFS) | [visualgo.net/en/graphds](https://visualgo.net/en/graphds) |
| Heap / Priority Queue | [visualgo.net/en/heap](https://visualgo.net/en/heap) |

### Further Study

| Resource | What For |
|----------|----------|
| [Python Official Docs](https://docs.python.org/3/) | Authoritative reference |
| [Real Python](https://realpython.com/) | Practical tutorials |
| [LeetCode](https://leetcode.com/) | DSA practice, interviews |
| [Big O Cheat Sheet](https://www.bigocheatsheet.com/) | Complexity quick reference |
| [freeCodeCamp YouTube](https://www.youtube.com/@freecodecamp) | Full video courses |
| [CS50P — Harvard](https://cs50.harvard.edu/python/) | Free Python course with projects |

---

<div align="center">

```
Built with 💙 by Dev (Devansh Mishra)
─────────────────────────────────────────────────────
GitHub   : github.com/auditordevansh
LinkedIn : linkedin.com/in/devanshmishra29
─────────────────────────────────────────────────────
```

*If this helped you — drop a ⭐ on the repo. It means a lot.*
*Found an error or want to add something? Open a PR — contributions welcome.*

</div>

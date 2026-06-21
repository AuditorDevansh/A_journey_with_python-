# Caesar Cipher Tool 🔒

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, robust Python implementation of the classic **Caesar Cipher** algorithm. This tool allows you to securely encrypt and decrypt text messages by shifting letters through the alphabet.

---

## 🚀 Features

- **Case Preservation:** Correctly shifts both lowercase and uppercase characters while maintaining their capitalization.
- **Character Retention:** Leaves spaces, punctuation, numbers, and special characters completely untouched.
- **Input Validation:** Built-in safeguards to ensure shift keys are valid integers within the standard range ($1 \le \text{shift} \le 25$).
- **Clean Architecture:** Divided into distinct helper functions (`encrypt` and `decrypt`) powered by a highly optimized backend using Python's native `str.maketrans()` and `.translate()`.

---

## 🛠️ How It Works

The Caesar Cipher works by shifting each letter in the text by a fixed number of positions down the alphabet. 

For example, with a **shift of 3**:
* `A` becomes `D`
* `B` becomes `E`
* `C` becomes `F`

---

## 💻 Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/AuditorDevansh/A_journey_with_python-.git](https://github.com/AuditorDevansh/A_journey_with_python-.git)
cd A_journey_with_python-/Phase_1/Cryptography

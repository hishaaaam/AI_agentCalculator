# 🤖 AI Stack-Based Calculator

A smart desktop calculator built with **Python + Tkinter** that evaluates mathematical expressions using **core Data Structures concepts**.

Unlike basic calculators that rely on Python’s `eval()`, this project implements a **Stack-based expression engine** with **Infix → Postfix conversion**, making it safer, academic-friendly, and interview-ready.

---

## 🚀 Features

* ✅ Stack-based expression evaluation
* ✅ Infix to Postfix conversion
* ✅ Safe calculation (no `eval()`)
* ✅ Clean chat-style UI using Tkinter
* ✅ Supports brackets and operator precedence
* ✅ Division-by-zero handling
* ✅ Time complexity: **O(n)**

---

## 🧠 Data Structures Used

### 🔹 Array (Python List)

Used for:

* Token storage
* Stack internal storage
* Postfix output list

Example:

```python
self.items = []  # array-based stack
```

---

### 🔹 Stack

Custom stack implementation with:

* `push()`
* `pop()`
* `peek()`
* `is_empty()`

Used in:

* Infix → Postfix conversion
* Postfix evaluation

---

## ⚙️ How It Works

### Step 1: Tokenization

User input:

```
10 + 5 * 3
```

Converted to tokens:

```
['10', '+', '5', '*', '3']
```

---

### Step 2: Infix → Postfix (Stack)

Using operator precedence:

```
10 5 3 * +
```

---

### Step 3: Postfix Evaluation (Stack)

The postfix expression is evaluated using stack push/pop operations to produce the final result.

---

## 🖥️ UI Overview

* Chat-style calculator interface
* Scrollable conversation window
* Input box with Enter key support
* Gradient background

---

## 📦 Requirements

* Python **3.8+**
* Tkinter (comes preinstalled with Python)

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

---

### 2️⃣ Run the application

```bash
python aiagentcalculator.py
```

---

## 🧪 Example Inputs

Try these in the app:

```
10 + 5 * 3
( 8 + 2 ) * 5
100 / 4 + 6
```

---

## 🏗️ Project Structure

```
aiagentcalculator.py
README.md
```

Main components:

* **Stack class** → core data structure
* **ExpressionEvaluator** → conversion + evaluation
* **CalculatorAgent** → user interaction logic
* **Tkinter UI** → frontend

---

## 🎯 Educational Value

This project demonstrates:

* Data Structures in real applications
* Stack-based expression parsing
* Algorithmic thinking
* Safe expression evaluation
* GUI development with Tkinter

Perfect for:

* 🎓 Data Structures course
* 💼 Portfolio projects
* 🧠 Viva demonstrations
* 🏫 Mini projects

---

## 🚀 Future Improvements

* Support scientific functions (sin, cos, sqrt)
* Step-by-step stack visualization
* Button-based calculator layout
* Error highlighting
* Web version (Streamlit)

---

## 👨‍💻 Author

**Hisham Hidayathulla**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub — it helps!

---

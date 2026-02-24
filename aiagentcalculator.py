import tkinter as tk
import re
import math


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0




class ExpressionEvaluator:

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    def tokenize(self, expression):
        """Convert string into tokens (ARRAY usage)"""
        tokens = re.findall(r'\d+\.?\d*|[+\-*/()]', expression)
        return tokens

    def infix_to_postfix(self, tokens):
        output = []
        op_stack = Stack()

        for token in tokens:

            if re.match(r'\d', token):  # number
                output.append(token)

            elif token == '(':
                op_stack.push(token)

            elif token == ')':
                while not op_stack.is_empty() and op_stack.peek() != '(':
                    output.append(op_stack.pop())
                op_stack.pop()  # remove '('

            else:  # operator
                while (
                    not op_stack.is_empty()
                    and op_stack.peek() != '('
                    and self.precedence[token] <= self.precedence[op_stack.peek()]
                ):
                    output.append(op_stack.pop())
                op_stack.push(token)

        while not op_stack.is_empty():
            output.append(op_stack.pop())

        return output

    def evaluate_postfix(self, postfix):
        """Evaluate postfix using STACK"""
        stack = Stack()

        for token in postfix:

            if re.match(r'\d', token):
                stack.push(float(token))

            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.push(a + b)
                elif token == '-':
                    stack.push(a - b)
                elif token == '*':
                    stack.push(a * b)
                elif token == '/':
                    if b == 0:
                        return "Error: Division by zero"
                    stack.push(a / b)

        return stack.pop()

    def evaluate(self, expression):
        tokens = self.tokenize(expression)
        postfix = self.infix_to_postfix(tokens)
        return self.evaluate_postfix(postfix)


# ===================== AI AGENT =====================

class CalculatorAgent:

    def __init__(self):
        self.memory = None
        self.engine = ExpressionEvaluator()

    def run(self, user_input):
        text = user_input.lower()

        # greetings
        if any(greet in text for greet in ["hi", "hello", "hey"]):
            return "Hello 👋 Tell me what you want to calculate!"

        if any(bye in text for bye in ["bye", "exit", "quit"]):
            return "Byeee 👋"

        try:
            result = self.engine.evaluate(text)
            self.memory = result
            return f"The result is {result}"
        except:
            return "Invalid expression 🙂"


# ===================== UI =====================

agent = CalculatorAgent()

root = tk.Tk()
root.title("AI Stack Calculator 🤖")
root.geometry("560x600")
root.resizable(False, False)

# Gradient background
canvas = tk.Canvas(root, width=560, height=600)
canvas.pack(fill="both", expand=True)

for i in range(600):
    r = int(230 - (i / 600) * 40)
    g = int(240 - (i / 600) * 70)
    b = 255
    canvas.create_line(0, i, 560, i, fill=f'#{r:02x}{g:02x}{b:02x}')

container = tk.Frame(root, bg="white")
container.place(relwidth=0.94, relheight=0.94, relx=0.03, rely=0.03)

# Chat area
chat_frame = tk.Frame(container, bg="white")
chat_frame.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_box = tk.Text(
    chat_frame,
    bg="white",
    font=("Segoe UI", 11),
    wrap="word",
    yscrollcommand=scrollbar.set,
    bd=0
)

chat_box.pack(fill="both", expand=True)
scrollbar.config(command=chat_box.yview)

chat_box.insert(
    tk.END,
    "Agent 🤖: Hello! I am your Stack-Based AI Calculator.\n"
    "Try: 10 + 5 * 3 or ( 8 + 2 ) * 5\n\n"
)

# Input bar
input_frame = tk.Frame(container, bg="#f5f7fb", height=70)
input_frame.pack(fill="x")

entry = tk.Entry(input_frame, font=("Segoe UI", 12), bd=0)
entry.pack(side=tk.LEFT, fill="x", expand=True, padx=10, pady=15, ipady=8)


def send_message(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return

    chat_box.insert(tk.END, f"You 🙂: {user_input}\n")
    entry.delete(0, tk.END)

    response = agent.run(user_input)

    chat_box.insert(tk.END, f"Agent 🤖: {response}\n\n")
    chat_box.see(tk.END)


send_btn = tk.Button(
    input_frame,
    text="Send",
    font=("Segoe UI", 11, "bold"),
    bg="#2F80ED",
    fg="white",
    relief="flat",
    padx=20,
    command=send_message
)

send_btn.pack(side=tk.RIGHT, padx=10)

entry.bind("<Return>", send_message)

root.mainloop()
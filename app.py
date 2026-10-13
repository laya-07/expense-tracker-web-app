from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

FILE = "expenses.txt"


def load_expenses():
    expenses = []

    try:
        file = open(FILE, "r")

        for index, line in enumerate(file):

            line = line.strip()

            if not line:
                continue

            date, amount, category = line.split(",")

            expenses.append({
                "id": index,
                "date": date,
                "amount": amount,
                "category": category
            })

        file.close()

    except Exception as e:
        print("ERROR:", e)

    return expenses


def save_expense(amount, category):
    date = datetime.now().strftime("%d-%m-%Y")

    file = open(FILE, "a")
    file.write(f"{date},{amount},{category}\n")
    file.close()

@app.route('/delete/<int:id>')
def delete(id):

    delete_expense(id)

    return home()

def delete_expense(expense_id):

    expenses = load_expenses()

    file = open(FILE, "w")

    for expense in expenses:

        if expense["id"] != expense_id:

            file.write(
                f"{expense['date']},{expense['amount']},{expense['category']}\n"
            )

    file.close()

@app.route('/')
def home():
    expenses = load_expenses()
    total = 0

    for expense in expenses:
        total += int(expense["amount"])

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )


@app.route('/add', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category = request.form['category']

    if category == "Other":
        category = request.form['custom_category']

    save_expense(amount, category)

    return home()


if __name__ == "__main__":
    app.run(debug=True)
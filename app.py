from operator import truediv

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]
    fruits_o_start = [fruit for fruit in fruits if check_o_start(fruit)]
    fruits_more_than_3 = [fruit for fruit in fruits if check_more_than_3(fruit)]

    return render_template("index.html", fruits_o_start=fruits_o_start)

def check_o_start(fruit_info):
    return fruit_info["name"][0].lower() == "o"

def check_more_than_3(fruit_info):
    return fruit_info["quantity"] > 3
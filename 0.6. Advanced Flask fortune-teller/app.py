from flask import Flask, render_template
import random as rand
rand.randint(1,11)
app = Flask(__name__, template_folder = "templates")



@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/fotrune')
def fortune():
    possible_fortunes = ["A beautiful smart  loving person will be coming into your life","A golden egg of opportunity falls into your lap this month",
"A good friendship iS often more important than a passionate romance","A fresh start will put you on your way","A friend iS a present you give yourself","An inch of time is an inch of gold","Believe it can be done","In order to take, one must first give.","It is better to deal with problems before they arise.","Pennies from heaven find their way to your doorstep this year!"]
    selected_fortune = rand.choice(possible_fortunes)
    return render_template("fotrune.html",selected_fortune = selected_fortune)


if __name__ == '__main__':
    app.run(debug = True)
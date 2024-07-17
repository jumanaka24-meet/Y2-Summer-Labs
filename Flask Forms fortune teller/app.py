from flask import Flask, render_template,url_for,redirect,request

import random as rand
rand.randint(1,11)
app = Flask(__name__, template_folder = "templates")





@app.route('/home', methods=['GET', 'POST'])
def home():
    possible_fortunes = [
    "A beautiful smart loving person will be coming into your life",
    "A golden egg of opportunity falls into your lap this month",
    "A fresh start will put you on the way",
    "A good friendship is often more important than a passionate romance",
    "A friend is a present you give yourself",
    "An inch of time is an inch of gold",
    "Believe it can be done",
    "In order to take, one must first give.",
    "It is better to deal with problems before they arise.",
    "Pennies from heaven find their way to your doorstep this year!"
]
    if request.method == 'GET' :
        return render_template('home.html')
    else:
        month = request.form['birth-month']
        if len(month)>11:
            length = possible_fortunes[7]
            print(length)
        else:
            length= possible_fortunes[len(month)]
            print(length)


        return redirect(url_for('fortune',length= length))

@app.route('/fortune/<length>', methods=['GET', 'POST'])
def fortune(length):
    return render_template("fotrune.html",length=length)


if __name__ == '__main__':
    app.run(debug = True)







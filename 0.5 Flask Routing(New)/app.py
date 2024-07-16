from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "<html><p>WELCOME TO THE PHOTO GALLERY</P><a href = \'/food1\'> go to the first food photo</a> <a href = \'/pet2\'> go to the second pet photo</a> <a href = \'/outerspace1\'> go to the first outerspace photo</a> </html><a href = \'/food3\'> go to the third food photo</a>"



@app.route('/food1')
def food1():
    return"<html><h1></h1><img src = 'https://www.summahealth.org/-/media/project/summahealth/website/page-content/flourish/2_18a_fl_fastfood_400x400.webp?la=en&h=400&w=400&hash=145DC0CF6234A159261389F18A36742A.jpg'></img></html><a href = \'/food2\'> go to the second food photo</a><a href = \'/home\'> go to the home page</a>"



@app.route('/food2')
def food2 ():
    return"<html><h1></h1><img src = 'https://www.eatingwell.com/thmb/m5xUzIOmhWSoXZnY-oZcO9SdArQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/article_291139_the-top-10-healthiest-foods-for-kids_-02-4b745e57928c4786a61b47d8ba920058.jpg'></img></html><a href = \'/food3\'> go to the third food photo</a><a href = \'/food1\'> go to the first food photo</a> <a href "


@app.route('/food3')
def food3 ():
    return"<html><h1></h1><img src = 'https://images.immediate.co.uk/production/volatile/sites/30/2013/05/spaghetti-carbonara-382837d.jpg?resize=768,574.jpg'></img></html><a href = \'/home\'> go to the home page</a><a href = \'/food2\'> go to the second food photo</a> "

@app.route('/pet1')
def pet1 ():
    return"<html><h1></h1><img src = 'https://ultra-pet.co.za/wp-content/uploads/2020/08/socialising-800x630.jpg'></img></html><a href = \'/pet2\'> go to the second pet photo</a>"


@app.route('/pet2')
def pet2 ():
    return"<html><h1></h1><img src = 'https://media.cnn.com/api/v1/images/stellar/prod/191006152638-01-pets-and-our-health.jpg?q=w_2000,h_1125,x_0,y_0,c_fill'></img></html><a href = \'/pet1\'> go to the first pet photo</a><a href = \'/pet3\'> go to the third pet photo</a><a href = \'/home\'> go to the home page</a>"



@app.route('/pet3')
def pet3 ():
    return "<html><h1></h1><img src = 'https://www.humanesociety.org/sites/default/files/styles/768x326/public/2023-05/pet-rat-606079.jpg?h=c30eefd5&itok=5UojkYNo.jpg'></img></html><a href = \'/pet2\'> go to the second pet photo</a>"


@app.route('/outerspace1')
def outerspace1():
    return"<html><h1></h1><img src = 'https://www.earth.com/_next/image/?url=https%3A%2F%2Fcff2.earth.com%2Fuploads%2F2022%2F01%2F15092418%2FLife-on-Earth-1400x850.jpg&w=1920&q=75.jpg'></img></html><a href = \'/outerspace2\'> go to the second outerspace photo</a>><a href = \'/outerspace3\'> go to the third outerspace photo</a><a href = \'/home\'> go to the home page</a>"


@app.route('/outerspace2')
def outerspace2():
    return"<html><h1></h1><img src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzKj84btte0OhCtbqzysowKcY2s3RPZcztew&s.jpg'></img></html><a href = \'/outerspace3\'> go to the third outerspace photo</a><a href = \'/outerspace1\'> go to the first outerspace photo</a>"


@app.route('/outerspace3')
def outerspace3():
    return"<html><h1></h1><img src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCIP4Y7Ijxa5hAZ8u2oz2owMn3XTDc2zp6_Q&s.jpg'></img></html><a href = \'/outerspace2\'> go to the second outerspace photo</a><a href = \'/outerspace1\'> go to the first outerspace photo</a>"




    
if __name__ == '__main__':
    app.run(debug=True)


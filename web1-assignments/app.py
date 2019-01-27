from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #neu nguoi dung vao trang chu
def home(): #goi homepage, 'view function'
    return "Hello World, this is ---flask homepage"

@app.route("/c4e25")
def c4e25():
    return "This is C4E25, happy coding!!!"

@app.route("/hi/quan")
def hi_me():
    return "hi quan"

@app.route("/hi/<name>")
def hi(name):
    return "Hi" + name + "Have a good day!!!"

@app.route("/add/<int:x>/<int:y>")
def math(x,y):
    total = x+y
    return str(total) 

@app.route("/simple_html")
def simple_html():
    return "<h3>Simple, indeed!!!</h3>"

@app.route("/html")
def html():
    return render_template("sample.html")

food_list = [
    "Bún đậu",
    "Bún chả",
    "Gà rán",
    "Nem lụi" ,  
]
@app.route("/food/<int:index>") #detail 
def food(index):
    return render_template("food.html", title=food_list[index])

@app.route("/menu")
def menu():
    return render_template("menu.html", food_list=food_list)

detail = {
    'title' : 'Bún chả',
    'image' :'https://img-global.cpcdn.com/005_recipes/da2ad5d76d683cf3/1200x630cq70/photo.jpg'
}
@app.route("/food_detail")
def food_detail():
    return render_template("food_detail.html", detail=detail)
if __name__== "__main__":
    app.run(debug=True)
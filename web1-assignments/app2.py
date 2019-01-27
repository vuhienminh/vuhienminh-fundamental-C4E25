from flask import Flask
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    BMI = (weight*1000)/(height*height)
    return "Your BMI is" , BMI
    if BMI < 16:
        return "Severely underweight"
    elif 16 <= BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI < 25:
        return "Normal"
    elif 25 <= BMI < 30:
        return "Overweight"
    else:
        return "obese"
    

if __name__ == '__main__':
  app.run(debug=True)
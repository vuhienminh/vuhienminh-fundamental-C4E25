from flask import Flask, render_template, redirect
app = Flask(__name__)

information = {
    "Name": "Hiền Minh",
    "Work": "Waitress",
    "School":"University of Adelaide",
    
}
@app.route("/about-me")
def inform():
    return render_template("info.html", information=information )

@app.route("/school")
def school():
    return redirect ("http://techkids.vn", code = 302)
if __name__ == '__main__':
  app.run(debug=True)
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR65'
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)





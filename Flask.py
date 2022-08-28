from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('input.html')

def Gempa():
    import gempaterkini
    return render_template('input.html', gempaterkini=gempaterkini)


if __name__ == '__main__':
    app.run(debug=True)
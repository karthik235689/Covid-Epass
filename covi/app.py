from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/about')
def about():
    pass

@app.route('/login')
def login():
    pass

@app.route('/register')
def register():
    pass










if __name__ == "__main__":
    app.run(debug=True)

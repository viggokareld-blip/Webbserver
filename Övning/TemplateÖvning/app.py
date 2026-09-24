from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    if not request.args.get('name'):
        name = "World"
    else:
        name = request.args.get('name')
    # Render the index.html template with a name variable
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
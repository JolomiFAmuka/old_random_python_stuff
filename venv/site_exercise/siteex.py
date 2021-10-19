from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/register')
def register():
    return render_template ('register.html')

@app.route('/thankspage')
def thankspage():
    first = request.args.get('first')
    last = request.args.get('last')
    namelen = len(first)
    return render_template('thankspage.html', first=first, last=last, namelen=namelen)

if __name__ == '__main__':
    app.run(debug=True)
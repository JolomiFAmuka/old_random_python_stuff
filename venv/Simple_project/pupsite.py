from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def index():
    return render_template ('puphome.html')

@app.route('/puppy/<name>')
def pupuser(name):
    return render_template ('pupuser.html', name=name)

if __name__ == ('__main__'):
    app.run()
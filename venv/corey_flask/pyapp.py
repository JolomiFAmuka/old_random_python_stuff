from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author':'Jolomi Amuka',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'April 20th 2018'
    },
    {
        'author':'Fhima Magdalene',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'April 21st 2018'
    }
]

@app.route('/')
def index():
    return render_template('homepage.html', posts=posts)

@app.route('/about')
def aboutpage():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
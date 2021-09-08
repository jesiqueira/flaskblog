from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'f5f8df9b67db18154630b26a666d0d5f'

posts = [
    {
        'author': 'Jose Edmar de Siqueira',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 04, 2021'
    },
    {
        'author': 'Lucas Siqueira',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 04, 2021'
    }
]


@app.route("/")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, redirect, url_for
from wtforms_fields import *
from models import *
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://noniwoblmkiqub:a8b764046f0c4544a4a508e8e083ac50af75c39eca40e0347795971872e19997@ec2-34-233-186-251.compute-1.amazonaws.com:5432/d2e8snkbaoacm2'
db = SQLAlchemy(app)

# configure login manager
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):

    return User.query.get(int(id))


@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()


    # Update databse if validation success
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Hashed psswd
        hashed_pswd = pbkdf2_sha256.hash(password)

        #
        # # Check username exist
        # user_object = User.query.filter_by(username=username).first()
        # if user_object:
        #     return "Someone else has taken the username!!!"

        user = User(username=username, password=hashed_pswd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)
@app.route("/login", methods=['Get', 'Post'])
def login():

    login_form = LoginForm()


    # Allow login if validation
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat')) 


    return render_template("login.html", form=login_form)

@app.route("/chat", methods=['GET', 'POST'])
@login_required
def chat():
    return "chat with me"
@app.route("/logout", methods=['GET'])
def logout():

    if current_user.is_authenticated:
        logout_user()
        return "Logged out"
    else:
        return "no user"

if __name__ == "__main__":

    app.run(debug = True)

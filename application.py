from flask import Flask, render_template
from wtforms_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://noniwoblmkiqub:a8b764046f0c4544a4a508e8e083ac50af75c39eca40e0347795971872e19997@ec2-34-233-186-251.compute-1.amazonaws.com:5432/d2e8snkbaoacm2'
db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Check username exist
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "Someone else has taken the username!!!"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted the data"

    return render_template("index.html", form=reg_form)


if __name__ == "__main__":

    app.run(debug = True)

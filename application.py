from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aislamml:12345@localhost/aislamml'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':
        email = request.form.get('email')
        comment = request.form.get('comment')

        comm = Comm(email = email, comment = comment)
        db.session.add(comm)
        db.session.commit()
    
    comments= Comm.query.all()
    return render_template('index.html', comm = comments)

if __name__ == '__main__':
    app.run(debug=True)
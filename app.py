from flask import Flask, render_template, url_for, flash, redirect, make_response, request, session
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash as idHash
from config import SECRET_KEY


app = Flask(__name__)
proxied = FlaskBehindProxy(app)  ## add this line
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

product_name = "Hybrid Schedule"

# class food_item(db.Model):
#     __tablename__ = 'food_items'
#     id = db.Column(db.Integer, primary_key=True)
#     uuid = db.Column(db.String(64), nullable=False)
#     purchase_date = db.Column(db.Date(), nullable=False)
#     expiration_date = db.Column(db.Date(), nullable=False)
#     item_name = db.Column(db.String(40), nullable=False)
#     item_category = db.Column(db.String(40), nullable=False)

#     def to_dict(self):
#         return {
#             'id':self.id,
#             'item_name': self.item_name,
#             'item_category': self.item_category,
#             'purchase_date': self.purchase_date.strftime("%m/%d/%Y"),
#             'expiration_date': self.expiration_date.strftime("%m/%d/%Y"),
#         }

# db.create_all()

@app.route("/")
@app.route("/home")
def home():
    return render_template('layout.html', title=f'{product_name}')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
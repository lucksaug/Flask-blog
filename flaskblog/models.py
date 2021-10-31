from datetime import datetime
from flaskblog import db#, login_manager
#from flask_login import UserMixin

'''
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
'''

def insert_user(username, email, password, image_file):
    cur = db.connection.cursor()
    cur.execute("INSERT INTO user(username, email, image_file, password) VALUES(%s, %s, %s, %s);",(username, email, image_file, password))
    db.connection.commit()
    cur.close()
    #def __repr__(self):
    #    return f"User('{self.username}', '{self.email}', '{self.image_file}')"

def select_user(search):
    cur = db.connection.cursor()
    cur.execute(" SELECT %s FROM user;", search)
    rv = cur.fetchall()
    cur.close()
    return rv
    #if key is not rv:
    #    return True
    #else:
    #    return False


#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String(100), nullable=False)
#    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#    content = db.Column(db.Text, nullable=False)
 #   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#    def __repr__(self):
 #       return f"Post('{self.title}', '{self.date_posted}')"
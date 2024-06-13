from flaskr.app import app, db
from flaskr.routes.homepage import homepage
from flaskr.routes.user_management import user_management
from flaskr.routes.link_management import link_management
from flaskr.routes.login import login
from flaskr.routes.register import register
from flaskr.routes.redirect_short_link import redirect_short_link
from flaskr.routes.user import user_blueprint
from flaskr.routes.link import link_blueprint
from flaskr.routes.mail import mail_blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(link_blueprint)
app.register_blueprint(mail_blueprint)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="192.168.1.64")

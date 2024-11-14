from flask import Flask

from app.routs.email_rout import emails_blueprint

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(emails_blueprint, url_prefix="/api")
    app.run(host='localhost', port=5000)

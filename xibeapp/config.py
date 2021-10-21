import os

class Config:
    SECRET_KEY = '4bfb093d4ea4cae9a1889d7e3ddc7414'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'ecec122038a987'
    MAIL_PASSWORD = '8d28cc5a5174f1'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    #MAIL_USERNAME = os.environ.get('EMAIL_USER')
    #MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    #configuração para enviar email pelo gmail
    #app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    #app.config['MAIL_PORT'] = 587
    #app.config['MAIL_USE_TLS'] = True
    #app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    #app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    #app.config['MAIL_USERNAME'] = "moacir.viana@gmail.com"
    #app.config['MAIL_PASSWORD'] = "mmv321@GM"
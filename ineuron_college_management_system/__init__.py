from flask import Flask

flip_app = Flask(__name__)


from ineuron_college_management_system.college_details.views import bp
flip_app.register_blueprint(bp, url_prefix='/college_details')



if __name__ == '__main__':
    flip_app.run(debug=True)


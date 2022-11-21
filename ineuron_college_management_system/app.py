from flask import Flask

college_management = Flask(__name__)

if __name__ == '__main__':
    college_management.run(debug=True)
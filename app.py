from flask import Flask
from flask import request
from user_profile_response import gather_profile_response

app = Flask(__name__)
@app.route('/')
def index():
    return 'Welcome to my app!'


@app.route('/profile', methods=['POST'],)
def profile():
    data = request.get_json()
    return gather_profile_response(name=data['name'], age=data['age'], colour=data['colour'])


if __name__ == '__main__':
    app.run()





































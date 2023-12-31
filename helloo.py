from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/api')
def get_info():

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if track != 'backend':
        return jsonify({'Error': 'invalid track'}), 400

    # getting the current date and time
    current_day = datetime.datetime.now().strftime('%A')

    # Getting the UTC time
    utc_time = datetime.datetime.now().strftime("%Y-%m-&d %H:%M:%S")

    git_file = "https://github.com/Matre5/Task/blob/master/helloo.py"

    git_repo = "https://github.com/Matre5/Task"

    status_code = 200

    result = {
        'slack_name': slack_name,
        'track': track,
        'Day': current_day,
        'UTC': utc_time,
        'git_file' : git_file,
        'git_repo' : git_repo,
        'status_code' : status_code
    }

    # response = jsonify(result)

    # response.headers['Content-type'] = 'application/json'

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)


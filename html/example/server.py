from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    timestamp = request.form.get('timestamp')
    referring_page = request.headers.get('Referer', 'Unknown')  # Get referring page from request headers

    # Log or process analytics data
    print(f"Timestamp: {timestamp}, Referring Page: {referring_page}")

    # Optionally, you can store analytics data in a database or perform other actions

    return 'Analytics data received'

if __name__ == '__main__':
    app.run(host='localhost', port=80)


# install flask --> pip install flask
# run this file --> python3 server.py
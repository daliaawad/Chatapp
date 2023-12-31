import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   #  conn = get_db_connection()
   #  posts = conn.execute('SELECT * FROM logs').fetchall()
   #  conn.close()
    return render_template('index.html')
   # return render_template('index.html', logs=logs)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



"""
from flask import Flask, render_template
from flask_socketio import SocketIO
async_mode = None
app = Flask(__name__)
socket_ = SocketIO(app, async_mode=async_mode)
@app.route('/')
def index():
    return render_template('index.html', sync_mode=socket_.async_mode)


if __name__ == '__main__':
    socket_.run(app, debug=True)
    """

# from flask import Flask, render_template, session, copy_current_request_context
# from flask_socketio import SocketIO, emit, disconnect
# from threading import Lock


# async_mode = None
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socket_ = SocketIO(app, async_mode=async_mode)
# thread = None
# thread_lock = Lock()


# @app.route('/')
# def index():
#    return render_template('index.html', async_mode=socket_.async_mode)


# @socket_.on('my_broadcast_event', namespace='/test')
# def test_broadcast_message(message):
#    session['receive_count'] = session.get('receive_count', 0) + 1
#    emit('my_response',
#       {'data': message['data'], 'count': session['receive_count']},
#       broadcast=True)


# @socket_.on('disconnect_request', namespace='/test')
# def disconnect_request():
#    @copy_current_request_context
#    def can_disconnect():
#       disconnect()

#    session['receive_count'] = session.get('receive_count', 0) + 1
#    emit('my_response',
#       {'data': 'Disconnected!', 'count': session['receive_count']},
#       callback=can_disconnect)


# if __name__ == '__main__':
#     socket_.run(app, debug=True)
    
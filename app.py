from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)


@app.route("/")
def spa():
    return render_template('index.html')

@socketio.on('measurement')
def handle_my_custom_event(args):
    print('received json: ' + str(args))
    socketio.emit('new_measurement',  args)



if __name__ == "__main__":
	socketio.run(app,'localhost')



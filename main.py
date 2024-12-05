import uuid
from flask import  render_template, request, make_response

from app import app

import prompts
import roles
from chat_completion import respond

import db

@app.route('/healthcheck')
def hello_world():  # put application's code here
    return 'Hello World!'

def add_message(chat_id, role, message):
    max_index = db.query('SELECT MAX(MsgIndex) FROM MESSAGES where ChatId = ?', (chat_id,), one=True)[0]

    msg_index = 0

    if max_index is not None:
        msg_index = max_index + 1

    sql_request = f"INSERT INTO MESSAGES VALUES (?, ?, ?, ?)"
    db.execute(sql_request, (chat_id, msg_index, role, message))

def get_chat_messages(chat_id) -> list[dict[str, str]]:
    messages = db.query(f'SELECT * FROM MESSAGES WHERE ChatId = ? ORDER BY MsgIndex', (chat_id,))
    return [{'role':message[2], 'message':message[3]} for message in messages]


def get_chat_id():
    chat_id = uuid.uuid4().hex
    add_message(chat_id, roles.assistant, prompts.agent_first_message)
    return chat_id

def add_system_prompt(message_history):
    prompt = {"role": roles.system, "message": prompts.system_prompt}
    message_history.insert(0, prompt)

    return message_history

@app.route('/')
def index():
    chat_id = request.cookies.get('ChatId')

    if not chat_id:
        chat_id = get_chat_id()

    messages = get_chat_messages(chat_id)
    messages = [(message.get('role'), message.get('message')) for message in messages]

    resp = make_response(render_template('index.html', messages=messages))
    resp.set_cookie('ChatId', chat_id)

    return resp

@app.route('/send', methods=['POST'])
def send():
    chat_id = request.cookies.get('ChatId')
    message = request.form['message']

    if message == "":
        return ""

    add_message(chat_id, roles.user, message)

    return render_template('reply.html', message=message)

@app.route('/reply')
def reply():
    chat_id = request.cookies.get('ChatId')
    messages = get_chat_messages(chat_id)

    messages = add_system_prompt(messages)

    answer = respond(messages)
    add_message(chat_id, roles.assistant, answer)

    return render_template('message.html', username=roles.assistant, message=answer)


@app.route('/reset')
def reset():
    chat_id = request.cookies.get('ChatId')

    db.execute(f'DELETE FROM MESSAGES WHERE ChatId = ?', (chat_id,))
    new_id = get_chat_id()

    messages = get_chat_messages(new_id)
    messages = [(message.get('role'), message.get('message')) for message in messages]

    resp = make_response(render_template('chat_window.html', messages=messages))
    resp.set_cookie('ChatId', new_id)

    return resp

if __name__ == '__main__':
    app.run()

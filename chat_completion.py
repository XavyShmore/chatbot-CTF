from dotenv import load_dotenv
from openai import OpenAI

#The open ai model to use. In my testing gpt-4o-mini is really good for the task and cheap to host
MODEL_TO_USE="gpt-4o-mini"

load_dotenv()
client = OpenAI()

def convert_message_format(message_history):
    return [{"role":message.get('role'), "content": message.get('message')} for message in message_history]

def respond(message_history):
    completion = client.chat.completions.create(
        model=MODEL_TO_USE,
        messages=convert_message_format(message_history),
    )
    response = completion.choices[0].message.content
    return response


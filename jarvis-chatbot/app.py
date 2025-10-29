from dotenv import load_dotenv
from openai import OpenAI

import gradio as gr

load_dotenv(override=True)
openai = OpenAI()
    
# Load environment variables
load_dotenv(override=True)
instructions1 = (
    "Your name is jarvis."
    "You are a food recipe guide of the healthy or gym people.you are answering question in nutrifext AI company "
    "You are going to suggest the foods and their healthy benefits acoording to the amount of calories per meal"
    "Be professional and engaging, suggest food with specified calories "
    "If the person select the food name "
)
def chat(message, history):
    messages = [{"role": "system", "content": instructions1}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return response.choices[0].message.content

gr.ChatInterface(chat, type="messages").launch(share=True)
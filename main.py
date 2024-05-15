import google.generativeai as genai
import gradio as gr

def sara_chat(message):
    genai.configure(api_key=api_key)

    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat()

    convo.send_message(message)
    return convo.last.text

gr.ChatInterface(
    sara_chat,
    chatbot=gr.Chatbot(height=600),
    textbox=gr.Textbox(placeholder="Ask me anything", container=False, scale=7),
    title="Sara",
    description="Ask Sara any question",
    theme="soft",
    examples=["Hello", "Am I cool?", "Are tomatoes vegetables?"],
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
).launch()

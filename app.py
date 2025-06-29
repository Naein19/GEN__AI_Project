# app.py or notebook
import requests
from PIL import Image
from io import BytesIO
import gradio as gr

try:
    from config import HUGGINGFACE_TOKEN
except ImportError:
    HUGGINGFACE_TOKEN = "hf_token_placeholder"  # Default or warning

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

def generate_image(prompt):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        return f"Error {response.status_code}: {response.text}"

with gr.Blocks() as demo:
    gr.Markdown("# ✨ Generative AI Image Creator")
    gr.Markdown("Enter a prompt to generate an image using AI.")

    prompt_box = gr.Textbox(label="🧘 Enter your prompt here:")
    image_output = gr.Image(label="🖼️ Generated Image")
    generate_btn = gr.Button("✨ Generate Image")

    generate_btn.click(fn=generate_image, inputs=prompt_box, outputs=image_output)

demo.launch()

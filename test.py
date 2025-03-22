import gradio as gr

print("Starting the Gradio app...")

def greet(name):
    return f"Hello, {name}!"

interface = gr.Interface(fn=greet, inputs="text", outputs="text")
interface.launch()

print("Gradio app is running.")



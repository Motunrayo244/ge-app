import gradio as gr
import requests
import re

# Define the function to call the API
def query_vllm(prompt, use_cache=True, temperature=1.5, min_p=0.1):
    api_url = "https://m5ypgg3uebl8r4hj.us-east-1.aws.endpoints.huggingface.cloud/v1/chat/completions" # "http://172.17.0.2:8000/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Accept" : "application/json"}
    payload = {
        "model": "tgi",  
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512,
        "use_cache": use_cache,
        "temperature": temperature,
        "min_p": min_p,
    }
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response_data = response.json()
        if "choices" in response_data:
            raw_output = response_data["choices"][0]["message"]["content"]
            # Parse output into Expectations and Recommendations/Instructions
            cleaned_output =  raw_output.strip() #re.sub(r'[^a-zA-Z0-9\s.,:;!?()\-\'"\n=_$#%&@*]+', '', raw_output).strip()
            
            # Identify Recommendations if present
            if "#replace" in cleaned_output:
                parts = cleaned_output.split("#replace", 1)
                expectations = parts[0].strip()
                recommendation = f"Replace {parts[1].strip()}"
            else:
                expectations = cleaned_output
                recommendation = "No specific recommendations."
            
            return f"Expectation:\n{expectations}\n\nRecommendation/Instruction:\n{recommendation}"
        else:
            return f"Error: {response_data.get('message', 'Unknown error')}"
    except Exception as e:
        return f"Error: {e}"

# Create a Gradio interface
interface = gr.Interface(
    fn=query_vllm,
    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Checkbox(label="Use Cache", value=True),
        gr.Slider(label="Temperature", minimum=0.1, maximum=2.0, step=0.1, value=1.5),
        gr.Slider(label="Min P", minimum=0.0, maximum=1.0, step=0.1, value=0.1),
    ],
    outputs="text",
    title="Chat with Your Model",
    description="Enter your prompt and get Great Expectation rules with optional recommendations.",
)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch(share=True)

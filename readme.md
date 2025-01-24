# Run Server

```vllm serve "Motunrayo1960422/text-to-GreatExpectation-llama-finetuned-v1" --max_model_len 56000 --gpu_memory_utilization 0.95```

# Run App
- ```docker build -t ge-app:latest```
- ```docker run -p 7860:7860 gradio-app:latest```

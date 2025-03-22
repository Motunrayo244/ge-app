# Great Expectation App

This project contains a Gradio-based application for running a text-to-GreatExpectation model.

## Run Server

To serve the model using `vllm`, run the following command on your device:

Minimum Requirement for Server:
- Nvidia GPU
- 24GB RAM
- 6 vCPU
- 30GB Storage

```sh
vllm serve "Motunrayo1960422/text-to-GreatExpectation-llama-finetuned-v1" --max_model_len 56000 --gpu_memory_utilization 0.95


# Run Server

```vllm serve "Motunrayo1960422/text-to-GreatExpectation-llama-finetuned-v1" --max_model_len 56000 --gpu_memory_utilization 0.95```


# Run App
- ```docker build -t ge-app:latest```
- ```docker run -p 7860:7860 gradio-app:latest```


# Base image with vLLM and CUDA support
FROM vllm/vllm-openai:latest

# Set the working directory inside the container
WORKDIR /app

# Expose the required port for the API
EXPOSE 8000

# Set environment variables for vLLM
ENV HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}

# Command to start the vLLM API server
CMD ["vllm", "serve", "--model", "Motunrayo1960422/unsloth-Llama-3.2-3B-bnb-4bit-text-Great-Expectation-16bit"]

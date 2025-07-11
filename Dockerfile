FROM ollama/ollama

# Copy model into the container if needed
# COPY ./ollama_models /root/.ollama/models

EXPOSE 11434
CMD ["ollama", "serve"]

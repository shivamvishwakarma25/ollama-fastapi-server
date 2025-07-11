from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    prompt = body.get("prompt")

    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True
    )
    return {"response": result.stdout}

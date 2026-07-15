from ollama import chat


class OllamaService:
    def __init__(self, model="qwen3:8b"):
        self.model = model

    def generate(self, messages):
        response = chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]
from ollama import chat


class Brain:
    def __init__(self, model="qwen3:8b"):
        self.model = model

    def ask(self, message: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]
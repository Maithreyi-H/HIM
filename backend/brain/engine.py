from personality.loader import CharacterLoader
from prompts.builder import PromptBuilder
from services.ollama_service import OllamaService


class Brain:
    def __init__(self):
        self.character = CharacterLoader("jungkook")
        self.builder = PromptBuilder()
        self.llm = OllamaService()

    def ask(self, user_message: str) -> str:
        messages = self.builder.build(
            self.character,
            user_message
        )

        return self.llm.generate(messages)
from personality.loader import CharacterLoader
from prompts.builder import PromptBuilder
from services.ollama_service import OllamaService
from memory.conversation import ConversationMemory


class Brain:

    def __init__(self):

        self.character = CharacterLoader("jungkook")

        self.builder = PromptBuilder()

        self.memory = ConversationMemory()

        self.llm = OllamaService()

    def ask(self, user_message):

        self.memory.add_user_message(user_message)

        messages = self.builder.build(
            self.character,
            self.memory
        )

        reply = self.llm.generate(messages)

        self.memory.add_assistant_message(reply)

        return reply
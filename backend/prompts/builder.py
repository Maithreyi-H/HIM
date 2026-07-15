class PromptBuilder:

    def build(self, character, conversation):

        messages = [
            {
                "role": "system",
                "content": character.get_prompt()
            }
        ]

        messages.extend(conversation.get_messages())

        return messages
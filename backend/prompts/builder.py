class PromptBuilder:

    def build(self, character, user_message):

        messages = [
            {
                "role": "system",
                "content": character.get_prompt()
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        return messages
import json
from pathlib import Path


class CharacterLoader:
    def __init__(self, character_name):
        self.character_name = character_name

        base_path = (
            Path(__file__).parent.parent
            / "characters"
            / character_name
        )

        profile_path = base_path / "profile.json"
        prompt_path = base_path / "system_prompt.txt"

        with open(profile_path, "r", encoding="utf-8") as file:
            self.profile = json.load(file)

        with open(prompt_path, "r", encoding="utf-8") as file:
            self.system_prompt = file.read()

    def get_name(self):
        return self.profile["name"]

    def get_prompt(self):
        return self.system_prompt

    def get_profile(self):
        return self.profile
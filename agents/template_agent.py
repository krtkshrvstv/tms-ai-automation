class TemplateAgent:
    def __init__(self, name: str):
        self.name = name

    def think(self, context: str):
        print(f"[{self.name}] Thinking about: {context}")
class Player:
    def __init__(self, skills: dict[str, int], health):
        self.skills: dict[str, int] = skills
        self.health: int = health

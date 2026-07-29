class HomeCleaningRobot:
    def __init__(self, start_position=0):
        self.position = start_position
        self.cleaned_positions = []

    def perceive(self, environment):
        return environment.is_dirty(self.position)

    def decide(self, is_dirty):
        if is_dirty:
            return "Clean"
        else:
            return "Move Forward"

    def act(self, decision, environment):
        if decision == "Clean":
            print(f"Robot at {self.position}: Cleaning dirty spot.")
            environment.clean(self.position)
            self.cleaned_positions.append(self.position)
        elif decision == "Move Forward":
            print(f"Robot at {self.position}: Spot is clean. Moving forward.")
            self.position += 1

class Environment:
    def __init__(self, dirty_positions):
        self.dirty_positions = set(dirty_positions)

    def is_dirty(self, position):
        return position in self.dirty_positions

    def clean(self, position):
        if position in self.dirty_positions:
            self.dirty_positions.remove(position)

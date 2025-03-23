class StoryProgress:
    """Helper class to track story generation progress"""
    def __init__(self):
        self.percent = 0
        self.status = "Initializing..."

    def update(self, percent, status):
        self.percent = percent
        self.status = status
        return self.percent, self.status 
class GameStats:
    """Track stats for Alien Invasion."""

    def __init__(self, ai_game):
        """Initiailize Statistics"""
        self.settings = ai_game.settings
        self.reset_status()
    
    def reset_status(self):
        """Initialize stats that can change during the game."""
        self.ship_left = self.settings.ship_limit
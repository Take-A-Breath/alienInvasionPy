import sys
import pygame
from settings import Settings

class AlienInvasion
    """Overall clas to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        
        # Set the background color
        self.bg_color = (230, 230, 230)

        def run_game(self):
            """Start the main loop for the game."""
            while True:
                self._check_events()
                self._update_screen()
                        
        def _check_events(self):
            """Respond to keypresses and mouse events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
                self.ship.blitme()

                # Make the most recently drawn screen visible
                pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai. = AlienInvasion()
    ai.run_game()
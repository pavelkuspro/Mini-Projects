import pygame
from screens.menu import MenuScreen
from screens.user_select import UserSelectScreen
from screens.mission1 import Mission1Screen
from db.database import init_db

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders Skeleton")
        self.clock = pygame.time.Clock()
        self.running = True

        # ----- NOVÉ -----
        init_db()  # inicializace databáze
        self.current_user = None  # místo, kam uložíme aktuálního hráče

        self.state = "menu"        # aktuální obrazovka
        self.screens = {
            "menu": MenuScreen(self),
            "user_select": UserSelectScreen(self),
            "mission1": Mission1Screen(self)
        }

    def run(self):
        while self.running:
            screen_obj = self.screens[self.state]

            screen_obj.handle_events()
            screen_obj.update()
            screen_obj.render(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    Game().run()

import pygame
from screens.menu import MenuScreen
from screens.user_select import UserSelectScreen
from screens.mission1 import Mission1Screen
from db.database import init_db

class Game:
    def __init__(self):
        """
        Konstruktor, který se zavolá vždy.
        Nastaví základní atributy hry a jednu metodu, která provede spuštění hry.
        """
        # ----- inicializace hry -----
        pygame.init()   # inicializace modulárních podsystémů knihovny pygame
        self.screen = pygame.display.set_mode((800, 600))   # velikost screenu hry
        pygame.display.set_caption("Space Invaders Skeleton")   # popisek okna hry
        self.clock = pygame.time.Clock()    # vytvoření objektu, kterým budeme udávat rychlost hru (FPS)
        self.running = True     # atribut, který dokud bude True, tak hra poběží

        # ----- vytvoření databáze a aktuálně sledovaného uživatele -----
        init_db()  # inicializace databáze
        self.current_user = None  # místo, kam uložíme aktuálního hráče

        # ----- aktuální stav, na jaké "obrazovce" zrovna jsme -----
        self.state = "menu"        # aktuální obrazovka, začínáme v menu
        self.screens = {           # všechny obrazovky, mezi kterými budeme přepínat, reprezentované objekty
            "menu": MenuScreen(self),   # obrazovka menu
            "user_select": UserSelectScreen(self),  # obrazovka zadání aktuálního uživatele
            "mission1": Mission1Screen(self)    # obrazovka Mise 1
        }

    def run(self):
        while self.running:     # dokud je runniny = True, poběží nekonečná smyčka
            screen_obj = self.screens[self.state]   # aktuální obrazovka - jeden z objektů: Menu, Výběr hráče, Mise 1

            screen_obj.handle_events()  # koukáme po událostech
            screen_obj.update() # herní logika - jak se hra mění
            screen_obj.render(self.screen) # vykreslování na aktuální obrazovku (vlastně jen do skryté vrstvy)

            pygame.display.flip()   # vymění skrytou vrstvu za viditelnou
            self.clock.tick(60)     # max 60 FPS

        pygame.quit()   # ukončení hry, pokud running = False

if __name__ == "__main__":  # provede se jen, pokud bude modul spuštěný napřímo
    Game().run()            # vytvoření instance hry a zavolání metody run pro spuštění hry, začínáme v menu

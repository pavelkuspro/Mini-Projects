import pygame
from db.database import get_user, create_user

class UserSelectScreen:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 50)
        self.username = ""

        # tlačítko potvrzení
        self.confirm_button = pygame.Rect(100, 350, 200, 60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            # klávesnice
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.username = self.username[:-1]
                elif event.key == pygame.K_RETURN:
                    self.confirm()
                else:
                    if len(self.username) < 12:
                        self.username += event.unicode

            # myš
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.confirm_button.collidepoint(event.pos):
                    self.confirm()

    def confirm(self):
        name = self.username.strip()
        if name == "":
            return

        # Zkusíme najít uživatele v databázi
        user = get_user(name)

        if user is None:
            # pokud neexistuje → založíme ho
            create_user(name)

        self.game.current_user = name
        self.game.state = "mission1"

    def update(self):
        pass

    def render(self, screen):
        screen.fill((30, 30, 60))

        # text
        prompt_text = self.font.render("Zadej jméno hráče:", True, (255, 255, 255))
        name_text = self.font.render(self.username, True, (255, 255, 0))

        screen.blit(prompt_text, (100, 200))
        screen.blit(name_text, (100, 270))

        # tlačítko potvrzení
        pygame.draw.rect(screen, (70, 200, 70), self.confirm_button)
        confirm_text = self.font.render("Potvrdit", True, (255, 255, 255))
        screen.blit(confirm_text, (self.confirm_button.x + 20, self.confirm_button.y + 10))

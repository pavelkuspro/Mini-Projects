import pygame
from db.database import get_user, get_top_players

class MenuScreen:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 60)

        self.leader_font = pygame.font.Font(None, 36)  # font pro jména a skóre
        self.leader_title_font = pygame.font.Font(None, 48)  # font pro 'TOP 5 hráčů'

        # Tlačítka definujeme jako rect (x, y, šířka, výška)
        self.buttons = {
            "start": pygame.Rect(100, 125, 200, 60),
            "exit": pygame.Rect(100, 200, 200, 60)
        }

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # souřadnice kliknutí
                if self.buttons["start"].collidepoint(mouse_pos):
                    self.game.state = "user_select"
                elif self.buttons["exit"].collidepoint(mouse_pos):
                    self.game.running = False

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))

        # Vykreslíme nadpis
        title = self.font.render("SPACE INVADERS", True, (255, 255, 255))
        screen.blit(title, (60, 35))

        # Vykreslíme tlačítka jako barevné obdélníky + text
        pygame.draw.rect(screen, (70, 70, 200), self.buttons["start"])  # modré tlačítko
        pygame.draw.rect(screen, (200, 70, 70), self.buttons["exit"])   # červené tlačítko

        # Text na tlačítkách
        start_text = self.font.render("Start", True, (255, 255, 255))
        exit_text = self.font.render("Exit", True, (255, 255, 255))

        # Text vycentrovaný do tlačítka
        screen.blit(start_text, (self.buttons["start"].x + 50, self.buttons["start"].y + 10))
        screen.blit(exit_text, (self.buttons["exit"].x + 60, self.buttons["exit"].y + 10))

        # --- NOVÉ: highscore hráče ---
        if self.game.current_user:
            user = get_user(self.game.current_user)
            if user:
                highscore = user[2]  # podle struktury db: (id, username, highscore)
                score_text = self.font.render(f"Highscore: {highscore}", True, (255, 255, 0))
                screen.blit(score_text, (200, 400))

        # ----- LEADERBOARD -----
        top_players = get_top_players()

        leader_title = self.leader_title_font.render("TOP 3 hráčů:", True, (255, 255, 0))
        screen.blit(leader_title, (400, 100))

        y_offset = 150
        for i, (username, score) in enumerate(top_players, start=1):
            line = self.leader_font.render(f"{i}. {username} — {score}", True, (200, 200, 200))
            screen.blit(line, (400, y_offset))
            y_offset += 40


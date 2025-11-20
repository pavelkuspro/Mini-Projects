import pygame
import random
from db.database import update_score

class Mission1Screen:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont(None, 36)

        # hráč
        self.player = pygame.Rect(400, 550, 50, 20)
        self.player_speed = 5

        # střely
        self.bullets = []
        self.bullet_speed = 7

        # nepřítel - KE SMAZANI
        #self.enemy = pygame.Rect(random.randint(0, 750), 0, 40, 40)
        #self.enemy_speed = 3

        # více nepřátel
        self.enemies = []
        self.enemy_speed = 1

        for _ in range(7):
            x_coord = random.randint(0, 750)
            y_coord = random.randint(-200, -40)
            self.enemies.append(pygame.Rect(x_coord, y_coord, 40, 40))

        # skóre
        self.score = 0

        self.game_over = False

    def reset_game(self):
        # hráč
        self.player = pygame.Rect(400, 550, 50, 20)
        self.player_speed = 5

        # střely
        self.bullets = []
        self.bullet_speed = 7

        # nepřítel - KE SMAZANI
        # self.enemy = pygame.Rect(random.randint(0, 750), 0, 40, 40)
        # self.enemy_speed = 3

        # více nepřátel
        self.enemies = []
        self.enemy_speed = 1

        for _ in range(7):
            x_coord = random.randint(0, 750)
            y_coord = random.randint(-200, -40)
            self.enemies.append(pygame.Rect(x_coord, y_coord, 40, 40))

        # skóre
        self.score = 0

        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN:
                # střelba
                if event.key == pygame.K_SPACE and not self.game_over:
                    bullet = pygame.Rect(self.player.centerx - 2, self.player.top - 10, 4, 10)
                    self.bullets.append(bullet)

                # návrat do menu po Game Over
                if self.game_over and event.key == pygame.K_RETURN:
                    self.game.state = "menu"
                    # přidáno
                    self.reset_game()

    def update(self):
        if self.game_over:
            return

        keys = pygame.key.get_pressed()

        # pohyb hráče
        if keys[pygame.K_LEFT] and self.player.left > 0:
            self.player.x -= self.player_speed
        if keys[pygame.K_RIGHT] and self.player.right < 800:
            self.player.x += self.player_speed

        for bullet in self.bullets[:]:
            bullet.y -= self.bullet_speed

            if bullet.y < 0:
                self.bullets.remove(bullet)
                continue

            for enemy in self.enemies:
                if bullet.colliderect(enemy):
                    self.score += 1
                    self.bullets.remove(bullet)

                    # respawn nepřítele
                    enemy.y = random.randint(-300, -40)
                    enemy.x = random.randint(0, 760)

                    break

            # střela trefila nepřítele
            #if bullet.colliderect(self.enemy):
                #    self.bullets.remove(bullet)
                #    self.score += 1
                #    self.spawn_enemy()

        # pohyb nepřítele
        #self.enemy.y += self.enemy_speed

        # nepřítel doletěl dolů → game over
        #if self.enemy.bottom > 600:
            #    self.game_over = True
                #    if self.game.current_user:
                #       update_score(self.game.current_user, self.score)

        # pohyb nepřátel
        for enemy in self.enemies:
            enemy.y += self.enemy_speed

            # pokud spadne mimo obraz → poslat zpět nahoru a dát nový random x
            if enemy.y > 600 or self.player.colliderect(enemy):
                self.game_over = True
                if self.game.current_user:
                    update_score(self.game.current_user, self.score)

    # TENTO SMAZAT
    #def spawn_enemy(self):
        #    """Vytvoří nového nepřítele po zničení."""
        #    self.enemy.x = random.randint(0, 760)
        #    self.enemy.y = 0

    def render(self, screen):
        screen.fill((0, 0, 0))

        # hráč
        pygame.draw.rect(screen, (255, 255, 255), self.player)

        # střely
        for bullet in self.bullets:
            pygame.draw.rect(screen, (0, 255, 0), bullet)

        # nepřítel
        #pygame.draw.rect(screen, (255, 0, 0), self.enemy)
        for enemy in self.enemies:
            pygame.draw.rect(self.game.screen, (255, 0, 0), enemy)

        # skóre
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # game over text
        if self.game_over:
            msg = self.font.render("GAME OVER - Press ENTER", True, (255, 255, 0))
            screen.blit(msg, (200, 300))

import pygame
from setting import Config, sounds
from screens.chess import Chess
import ui

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.hard = ui.Button(screen, Config.width//2, Config.height//2, 200, 80, "Hard")
        self.medium = ui.Button(screen, Config.width//2, Config.height//2 + 100, 200, 80, "Medium")
        self.easy = ui.Button(screen, Config.width//2, Config.height//2 + 200, 200, 80, "Easy")
        self.exit = ui.Button(screen, Config.width//2, Config.height//2 + 300, 200, 80, "Exit")
        self.background = pygame.image.load("./assets/images/background1.jpg")
        self.background = pygame.transform.smoothscale(self.background, Config.resolution)
        self.title = ui.TextUI(self.screen, "CHESS", Config.width//1.2, Config.height//6, 140, (255, 255, 255))
        self.title.centered = True
        self.running = True
        self.clock = pygame.time.Clock()
        self.chess = Chess(screen)

    def DrawButtons(self):
        self.hard.Draw()
        self.medium.Draw()
        self.easy.Draw()
        self.exit.Draw()
        self.title.Draw()

    def HandleClick(self):
        mouse_position = pygame.mouse.get_pos()
        if self.hard.get_rect().collidepoint(mouse_position):
            self.chess.gameOver = False
            self.hard.tempcolor = (255, 255, 180)
            print("Hard")
            self.chess.playHard()
        elif self.medium.get_rect().collidepoint(mouse_position):
            self.chess.gameOver = False
            self.medium.tempcolor = (255, 255, 180)
            print("Medium")
            self.chess.playMedium()
        elif self.easy.get_rect().collidepoint(mouse_position):
            self.chess.gameOver = False
            self.easy.tempcolor = (255, 255, 180)
            print("Easy")
            self.chess.playEasy()
        elif self.exit.get_rect().collidepoint(mouse_position):
            self.exit.tempcolor = (255, 255, 180)
            self.running = False

    def GetFrameRate(self):
        return self.clock.get_fps()

    def Run(self):
        while self.running:
            self.clock.tick(Config.fps)
            # update caption and frame rate
            pygame.display.set_caption("Chess " + str(int(self.GetFrameRate())))
            # display background image
            self.screen.blit(self.background, (0, 0))
            # handle Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    # left mouse click
                    if event.button == 1:
                        self.HandleClick()

            self.DrawButtons()
            # update screen
            pygame.display.update()

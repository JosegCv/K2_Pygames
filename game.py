import pygame

class Bolas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Bolas")

        self.player = Ball(400,300, 30)
        self.metronomo = pygame.time.Clock()


    def main_loop(self):
        game_over = False
        dy = 10 
        
        while game_over == False:
            self.metronomo.tick(60)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True


            self.screen.fill((0, 255, 0))

            pygame.draw.circle(self.screen, (255,255,255), (self.player.x, self.player.y), self.player.radio)
            self.player.draw(self.screen)

            
            self.player.y += dy

            if self.player.y == 600 - self.player.radio:
                dy = -dy 


            pygame.display.flip()


class Ball:
    def __init__(self, x , y, radio, color =(255,255,255)):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radio)


if __name__ == "__main__":

    bola = Bolas()
    bola.main_loop()

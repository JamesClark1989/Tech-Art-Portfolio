import pygame, sys
from city import City
from settings import *

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Python Weather App")
        self.clock = pygame.time.Clock()

        # Australia background
        path = "australia.png"
        self.australia_bg = pygame.image.load(path).convert()
        SCALE_SIZE = (WINDOW_WIDTH,WINDOW_HEIGHT-150)
        self.australia_bg = pygame.transform.scale(self.australia_bg, SCALE_SIZE)


        self.city_group = pygame.sprite.Group()

        # Initial Loading Screen
        self.font = pygame.font.SysFont('Arial', 32)
        self.display_surface.fill((0,0,0))
        loading_text = self.font.render("Fetching Weather Info from API", True, (255,255,255))
        text_rect = loading_text.get_rect(center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        self.display_surface.blit(loading_text, text_rect)
        pygame.display.update()


        # groups
        self.setup()

    def setup(self):

        cities_loaded = 1
        # Import cities
        for city in cities:
            
            # Loading Text
            self.display_surface.fill((0,0,0))
            loading_text = self.font.render("Fetching Weather Info from API", True, (255,255,255))
            text_rect = loading_text.get_rect(center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
            self.display_surface.blit(loading_text, text_rect)
            cities_loaded_text = self.font.render(f"{cities_loaded}/{len(cities)}", True, (255,255,255))
            cities_load_rect = cities_loaded_text.get_rect(center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 40))
            self.display_surface.blit(cities_loaded_text, cities_load_rect)
            pygame.display.update()

            pos = cities[city]["pos"]
            city_name = cities[city]["name"]
            address = cities[city]["address"]
            City(pos, self.city_group, city_name, address,self.display_surface)

            cities_loaded += 1


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.display_surface.fill((0,0,0))
            self.display_surface.blit(self.australia_bg, (0,0))

            self.city_group.update(dt)

            is_mouse_over = False
            for city in self.city_group:
                if city.mouse_over == True:
                    is_mouse_over = True

            if not is_mouse_over:
                # Blit Help Text
                help_text = self.font.render("Place mouse over the capital cities to see weather details", True, (255,255,255))
                help_text_rect = help_text.get_rect(center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 270))
                self.display_surface.blit(help_text, help_text_rect)

            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()

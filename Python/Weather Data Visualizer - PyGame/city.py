import pygame, requests

class City(pygame.sprite.Sprite):

    def __init__(self, pos, groups, name, address, display_surface):
        super().__init__(groups)

        self.pos = pos
        self.address = address
        self.name = name
        self.display_surface = display_surface

        self.width_x = 30
        self.width_y = 30

        self.mouse_over = False

        self.font = pygame.font.SysFont('Arial', 32)

        self.setup()


    def setup(self):
        data = requests.get(self.address)
        self.json_data = data.json()
        
        # Weather data
        # Temperature
        self.temperature = self.json_data['current_weather']['temperature']
        # Windspeed
        self.windspeed = self.json_data['current_weather']['windspeed']
        # Rain fall summary
        self.rainfall = self.json_data['daily']['showers_sum'][0]

    

    def show_data(self):
        # Blit city name
        self.text = self.font.render(self.name.upper(), True, (255,255,255))
        self.display_surface.blit(self.text, (20, 560))

        # Blit temperature
        self.text = self.font.render(f"Temperature: {str(self.temperature)}°c", True, (255,255,255))
        self.display_surface.blit(self.text, (20, 600))

        # Blit Windspeed
        self.text = self.font.render(f"Windspeed: {str(self.windspeed)} km'h", True, (255,255,255))
        self.display_surface.blit(self.text, (20, 640))

        # Blit rainfall
        self.text = self.font.render(f"Rainfall: {str(self.rainfall)} mm", True, (255,255,255))
        self.display_surface.blit(self.text, (350, 600))


    def interact(self):
        x = self.pos[0]
        y = self.pos[1]
        mouse_pos = pygame.mouse.get_pos()
        if (mouse_pos[0] > x and mouse_pos[0] < x + self.width_x) and (mouse_pos[1] > y and mouse_pos[1] < y + self.width_y):
            self.show_data()
            self.mouse_over = True
        else:
            self.mouse_over = False

    def draw(self):
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.rect(self.display_surface, (0,255,0), pygame.Rect(x,y, self.width_x, self.width_y))

    def update(self,dt):
        self.draw()
        self.interact()

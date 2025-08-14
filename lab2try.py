import pygame
import math
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transformations with Buttons")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)
ORANGE = (255, 165, 0)
ACTIVE_COLOR = (255, 255, 200)
CANCEL_COLOR = (255, 100, 100)
ERROR_COLOR = (255, 50, 50)

# Fonts
FONT = pygame.font.SysFont(None, 24)

# Shape: Triangle points (centered)
shape_points = [(300, 300), (350, 200), (400, 300)]
original_points = shape_points.copy()

# Shape history for undo functionality
history = []

# Input box state variables
input_active = False
input_text = ''
input_prompt = ''
transformation_to_apply = None
error_message = ""

# Button class
class Button:
    def __init__(self, x, y, w, h, text, button_type="normal"):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = GRAY
        self.hover_color = LIGHT_BLUE
        self.active_color = GREEN if text != "Back" else ORANGE
        self.is_last_pressed = False
        
        if button_type == "cancel":
            self.color = CANCEL_COLOR
            self.hover_color = (255, 150, 150)
            self.active_color = (255, 50, 50)

    def draw(self, win):
        if self.is_last_pressed:
            color = self.active_color
        elif self.is_hovered:
            color = self.hover_color
        else:
            color = self.color

        pygame.draw.rect(win, color, self.rect, 0)
        pygame.draw.rect(win, BLACK, self.rect, 2)

        text_surface = FONT.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        win.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    @property
    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def set_last_pressed(self, is_last):
        self.is_last_pressed = is_last

# InputBox class
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.text = text
        self.active = False
        self.text_surface = FONT.render(self.text, True, BLACK)

    def handle_event(self, event):
        global input_text, input_active, transformation_to_apply, error_message
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            error_message = ""
            if event.key == pygame.K_RETURN:
                apply_transformation_with_input()
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
            self.text_surface = FONT.render(input_text, True, BLACK)

    def draw(self, screen):
        color = ACTIVE_COLOR if self.active else self.color
        pygame.draw.rect(screen, color, self.rect, 0)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

        text_rect = self.text_surface.get_rect(midleft=(self.rect.x + 5, self.rect.centery))
        screen.blit(self.text_surface, text_rect)

    def get_value(self):
        return self.text

# Transformation functions
def translate(points, tx, ty):
    return [(x + tx, y + ty) for x, y in points]

def scale(points, sx, sy):
    cx, cy = center(points)
    return [((x - cx) * sx + cx, (y - cy) * sy + cy) for x, y in points]

def rotate(points, angle):
    cx, cy = center(points)
    rad = math.radians(angle)
    return [
        (cx + (x - cx) * math.cos(rad) - (y - cy) * math.sin(rad),
         cy + (x - cx) * math.sin(rad) + (y - cy) * math.cos(rad))
        for x, y in points
    ]

def reflect_x(points):
    cx, cy = center(points)
    return [(x, 2*cy - y) for x, y in points]

def reflect_y(points):
    cx, cy = center(points)
    return [(2*cx - x, y) for x, y in points]

def shear(points, shx, shy):
    cx, cy = center(points)
    return [((x - cx) + shx * (y - cy) + cx,
             (y - cy) + shy * (x - cx) + cy) for x, y in points]

def center(points):
    xs, ys = zip(*points)
    return sum(xs)/len(xs), sum(ys)/len(ys)

def apply_transformation_with_input():
    global shape_points, transformation_to_apply, history, input_text, input_active, error_message

    old_shape = shape_points.copy()

    if transformation_to_apply and input_text:
        try:
            params = [float(p) for p in input_text.split(',')]
            history.append(shape_points.copy())

            if transformation_to_apply == "Translate":
                shape_points = translate(shape_points, params[0], params[1])
            elif transformation_to_apply == "Scale":
                shape_points = scale(shape_points, params[0], params[1])
            elif transformation_to_apply == "Rotate":
                shape_points = rotate(shape_points, params[0])
            elif transformation_to_apply == "Shear":
                shape_points = shear(shape_points, params[0], params[1])

            # Reset input state on valid input
            input_active = False
            input_text = ''
            error_message = ""
            
            for i in range(10):
                progress = i / 10
                intermediate = [
                    (x1 + (x2 - x1) * progress,
                     y1 + (y2 - y1) * progress)
                    for (x1, y1), (x2, y2) in zip(old_shape, shape_points)
                ]
                draw(intermediate)
                pygame.time.delay(50)

        except (ValueError, IndexError):
            # Keep the input box active and display an error message
            error_message = f"Invalid input. Please enter valid numbers for {transformation_to_apply}."
            input_text = ''
            print(error_message) # Still prints to console for debugging
            
def cancel_input_mode():
    global input_active, input_text, transformation_to_apply, input_prompt, error_message
    input_active = False
    input_text = ''
    transformation_to_apply = None
    input_prompt = ''
    error_message = ""
    for btn in buttons:
        btn.set_last_pressed(False)

def draw(points):
    screen.fill(WHITE)

    for i in range(0, WIDTH, 50):
        pygame.draw.line(screen, (220, 220, 220), (i, 0), (i, HEIGHT))
    for i in range(0, HEIGHT, 50):
        pygame.draw.line(screen, (220, 220, 220), (0, i), (WIDTH, i))

    pygame.draw.line(screen, (150, 150, 150), (WIDTH//2, 0), (WIDTH//2, HEIGHT), 2)
    pygame.draw.line(screen, (150, 150, 150), (0, HEIGHT//2), (WIDTH, HEIGHT//2), 2)

    pygame.draw.polygon(screen, (100, 150, 255), original_points)
    pygame.draw.polygon(screen, BLUE, original_points, 3)

    pygame.draw.polygon(screen, (255, 150, 150), points)
    pygame.draw.polygon(screen, RED, points, 3)
    
    font = pygame.font.SysFont(None, 24)
    info_text = f"Original (Blue) | Transformed (Red)"
    text_surface = font.render(info_text, True, BLACK)
    screen.blit(text_surface, (10, 10))
    
    # Draw error message if one exists
    if error_message:
        error_surface = FONT.render(error_message, True, ERROR_COLOR)
        screen.blit(error_surface, (10, 100))

    if input_active:
        prompt_surface = FONT.render(input_prompt, True, BLACK)
        screen.blit(prompt_surface, (10, 40))
        input_box.draw(screen)
        cancel_button.draw(screen)
    
    for btn in buttons:
        btn.draw(screen)

    pygame.display.update()

# Button labels and positions
button_width = 80
button_height = 30
button_y = HEIGHT - button_height - 10
button_spacing = 5
button_labels = ["Translate", "Scale", "Rotate", "Reflect X", "Reflect Y", "Shear", "Reset", "Back"]

total_width = len(button_labels) * button_width + (len(button_labels) - 1) * button_spacing
start_x = (WIDTH - total_width) // 2

buttons = [
    Button(start_x + i * (button_width + button_spacing), button_y, button_width, button_height, text)
    for i, text in enumerate(button_labels)
]

input_box = InputBox(10, 70, WIDTH - 120, 32)
cancel_button = Button(WIDTH - 100, 70, 90, 32, "Cancel", button_type="cancel")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if input_active:
            input_box.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN and cancel_button.is_clicked(event.pos):
                cancel_input_mode()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not input_active:
            error_message = ""
            pos = pygame.mouse.get_pos()
            for btn in buttons:
                if btn.is_clicked(pos):
                    for button in buttons:
                        button.set_last_pressed(False)
                    
                    old_shape = shape_points.copy()

                    if btn.text in ["Translate", "Scale", "Rotate", "Shear"]:
                        input_active = True
                        input_text = ''
                        transformation_to_apply = btn.text
                        btn.set_last_pressed(True)
                        if btn.text == "Translate":
                            input_prompt = "Enter tx,ty (e.g., 50,30):"
                        elif btn.text == "Scale":
                            input_prompt = "Enter sx,sy (e.g., 1.5,1.2):"
                        elif btn.text == "Rotate":
                            input_prompt = "Enter angle (e.g., 45):"
                        elif btn.text == "Shear":
                            input_prompt = "Enter shx,shy (e.g., 0.3,0.2):"

                    elif btn.text == "Reset":
                        shape_points = original_points.copy()
                        history.clear()
                        for button in buttons:
                            button.set_last_pressed(False)
                        
                    elif btn.text in ["Reflect X", "Reflect Y"]:
                        history.append(shape_points.copy())
                        if btn.text == "Reflect X":
                            shape_points = reflect_x(shape_points)
                        else:
                            shape_points = reflect_y(shape_points)
                        btn.set_last_pressed(True)
                        
                        for i in range(10):
                            progress = i / 10
                            intermediate = [
                                (x1 + (x2 - x1) * progress,
                                 y1 + (y2 - y1) * progress)
                                for (x1, y1), (x2, y2) in zip(old_shape, shape_points)
                            ]
                            draw(intermediate)
                            pygame.time.delay(50)
                            
                    elif btn.text == "Back":
                        if history:
                            old_shape = shape_points.copy()
                            shape_points = history.pop()
                            btn.set_last_pressed(True)

                            for i in range(10):
                                progress = i / 10
                                intermediate = [
                                    (x1 + (x2 - x1) * (1 - progress),
                                     y1 + (y2 - y1) * (1 - progress))
                                    for (x1, y1), (x2, y2) in zip(shape_points, old_shape)
                                ]
                                draw(intermediate)
                                pygame.time.delay(50)

    draw(shape_points)
    clock.tick(60)

pygame.quit()
sys.exit()
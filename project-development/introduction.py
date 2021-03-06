"""General information on your module and what it does."""
import coda_kids as coda

#load sprites constants
IMAGE_BUTTON = coda.Image("button.png")
IMAGE_SNAKE_1 = coda.Image("Snake_1.png")
IMAGE_SNAKE_2 = coda.Image("Snake_2.png")
IMAGE_SNAKE_3 = coda.Image("Snake_3.png")
IMAGE_SNAKE_4 = coda.Image("Snake_4.png")
IMAGE_SNAKE_5 = coda.Image("Snake_5.png")

SHEET = coda.SpriteSheet("tileset.png", (32, 32))
ANIMATION = coda.Animator(SHEET, 5)
OBJ = coda.Object(ANIMATION)

OBJ.scale *= 1
#test stuff

SOUND_CHARACTER = [
    [
        coda.Sound("Select_1.wav"),
        coda.Sound("Select_2.wav")
    ],
    [
        coda.Sound("Select_1.wav"),
        coda.Sound("Select_2.wav")
    ],
    [
        coda.Sound("Select_1.wav"),
        coda.Sound("Select_2.wav")
    ],
    [
        coda.Sound("Select_1.wav"),
        coda.Sound("Select_2.wav")
    ],
    [
        coda.Sound("Select_1.wav"),
        coda.Sound("Select_2.wav")
    ]
]

# text constants
TEXT_1 = "I am snake 1!"
TEXT_2 = "I am snake 2!"
TEXT_3 = "I am snake 3!"
TEXT_4 = "I am snake 4!"
TEXT_5 = "I am snake 5!"

class Data:
    """place changable state variables here."""
    info = coda.TextObject(coda.color.WHITE, 64, "")
    button = coda.Object(IMAGE_BUTTON)
    snake = coda.Object(IMAGE_SNAKE_1)
    selection = 1

MY = Data()

def play_sound(character):
    """plays a sound associated with a character."""
    sound = coda.utilities.rand(1, 2)
    SOUND_CHARACTER[character-1][sound-1].play()

def initialize(window):
    """Initializes the Introduction class."""
    MY.button.location = window / 2
    MY.info.location = (window.x / 2, 128)
    MY.info.centered = True
    MY.snake.location = (window.x / 2, 64)
    OBJ.location = window / 2

def update(delta_time):
    """Update method for Intro state."""
    print(delta_time)
    for event in coda.event.listing():
        if coda.event.quit_game(event):
            coda.stop()
        elif coda.event.mouse_l_button_down(event):
            if MY.button.collides_with_point(coda.event.mouse_position()):
                MY.selection += 1
                if MY.selection > 5:
                    MY.selection = 1
                play_sound(MY.selection)
    
    if OBJ.collides_with_point(coda.event.mouse_position()):
        coda.actions.add(OBJ, "scale", 4, 0.2)
    else:
        coda.actions.add(OBJ, "scale", 1, 0.2)

    OBJ.update(delta_time)
    

def draw(screen):
    """Draws the state to the given screen."""
    if MY.selection == 1:
        MY.snake.sprite = IMAGE_SNAKE_1
        MY.info.text = TEXT_1
    elif MY.selection == 2:
        MY.snake.sprite = IMAGE_SNAKE_2
        MY.info.text = TEXT_2
    elif MY.selection == 3:
        MY.snake.sprite = IMAGE_SNAKE_3
        MY.info.text = TEXT_3
    elif MY.selection == 4:
        MY.snake.sprite = IMAGE_SNAKE_4
        MY.info.text = TEXT_4
    elif MY.selection == 5:
        MY.snake.sprite = IMAGE_SNAKE_5
        MY.info.text = TEXT_5
    #MY.snake.draw(screen)
    #MY.info.draw(screen)
    #MY.button.draw(screen)
    OBJ.draw(screen)

def cleanup():
    """Cleans up the Intro State."""

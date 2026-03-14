# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'Level1Bg5' : 5,
    'Level1Bg6' : 6,
    'Player1'   : 3,
    'Player2'   : 3,
    'Enemy1'    : 2,
    'Enemy2'    : 1,
}

ENTITY_HEALTH = {
    'Level1Bg0' : 9999,
    'Level1Bg1' : 9999,
    'Level1Bg2' : 9999,
    'Level1Bg3' : 9999,
    'Level1Bg4' : 9999,
    'Level1Bg5' : 9999,
    'Level1Bg6' : 9999,
    'Level2Bg0': 9999,
    'Level2Bg1': 9999,
    'Level2Bg2': 9999,
    'Level2Bg3': 9999,
    'Level2Bg4': 9999,
    'Player1'  : 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}


# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000


# W
WIN_WIDTH = 576
WIN_HEIGHT = 324



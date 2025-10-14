# --- Screen and Game Settings ---
WIDTH = 960
HEIGHT = 720
FPS = 60

# --- Colors ---
BG_COLOR = (10, 10, 10)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

# --- Player Settings ---
PLAYER_SIZE = 24
PLAYER_ACCEL = 0.26
PLAYER_FRICTION = 0.98
PLAYER_TURN_SPEED = 0.085

# --- Bullet Settings ---
BULLET_SPEED = 8
MAX_BULLETS = 5

# --- Invincibility ---
INVINCIBILITY_FRAMES = 90  # About 1.5 seconds at 60 FPS

# --- Asteroid Settings ---
ASTEROID_MIN_RADIUS = 22
ASTEROID_MAX_RADIUS = 45
ASTEROID_MIN_SPEED = 0.7
ASTEROID_MAX_SPEED = 2.4
ASTEROID_VERTICES = (8, 16)

# --- Particle Effects ---
PARTICLE_LIFESPAN = (25, 50)  # min, max frames

# --- Leaderboard ---
LEADERBOARD_FILE = "leaderboard.txt"
LEADERBOARD_LIMIT = 8

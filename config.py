import arcade

# map configuration
# Set how many rows and columns we will have
ROW_COUNT = 40
COLUMN_COUNT = 40
BIOME_STEP = 5

# display configuration
# cell and boarder
CELL_WIDTH = 20
CELL_HEIGHT = 20
BOARDER_WIDTH = 2

# sidebar
DEFAULT_FONT_SIZE=20
SIDEBAR_WIDTH = 200
SIDEBAR_TEXT_X_MARGIN=10
SIDEBAR_TEXT_Y_MARGIN=10+DEFAULT_FONT_SIZE

# Do the math to figure out our screen dimensions
GRID_WIDTH = (CELL_WIDTH + BOARDER_WIDTH) * COLUMN_COUNT + BOARDER_WIDTH
GRID_HEIGHT = (CELL_HEIGHT + BOARDER_WIDTH) * ROW_COUNT + BOARDER_WIDTH
SCREEN_WIDTH = GRID_WIDTH + SIDEBAR_WIDTH
SCREEN_HEIGHT = GRID_WIDTH

HEIGHT_COLOR = [
    arcade.color.BLACK,
    arcade.color.GREEN,
    arcade.color.YELLOW_GREEN,
    arcade.color.YELLOW,
    arcade.color.ORANGE,
    arcade.color.RED,
]

# map configuration
# Set how many rows and columns we will have
ROW_COUNT = 40
COLUMN_COUNT = 40
BIOME_STEP = 5

# display configuration
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
BOARDER = 2

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + BOARDER) * COLUMN_COUNT + BOARDER
SCREEN_HEIGHT = (HEIGHT + BOARDER) * ROW_COUNT + BOARDER

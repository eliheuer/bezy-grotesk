import math
import argparse
import drawBot as db
import pytweening as pt
from fontTools.ttLib import TTFont
from datetime import datetime


# Width, Height, Margin, Unit, Frames
W, H, M, U, F = 1080*2, 1080*2, 120, 60, 50
CURRENT_DATE = datetime.now()
FORMATTED_DATE = CURRENT_DATE.strftime("%d-%m-%Y")


# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()


# FontTools docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
# ttFont = TTFont(MAIN_FONT_PATH)


# Draws a grid
def grid():
    db.stroke(1, 1, 1, 0.2)
    db.strokeWidth(1)

    # Calculate increments
    increment_x, increment_y = U, U

    # Draw the border rectangle
    db.rect(M, M, W - (M * 2), H - (M * 2))

    # Calculate how many lines will fit within the margins
    x_lines_count = int((W - 2 * M) / increment_x)
    y_lines_count = int((H - 2 * M) / increment_y)

    # Draw vertical grid lines
    for i in range(x_lines_count + 1):
        x_pos = M + (i * increment_x)
        db.line((x_pos, M), (x_pos, H - M))

    # Draw horizontal grid lines
    for i in range(y_lines_count + 1):
        y_pos = M + (i * increment_y)
        db.line((M, y_pos), (W - M, y_pos))

    # Draw center lines
    db.line((W / 2, 0), (W / 2, H))
    db.line((0, H / 2), (W, H / 2))


# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# For looping animations
def sin_loop(x):
    # Scale the input to the range [0, 2π] and shift by -π/2
    scaled_input = 2 * math.pi * (x % 1) - (math.pi / 2)
    # Calculate the sine of the scaled input
    return (math.sin(scaled_input) + 1) / 2


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    db.newPage(W, H)
    db.fill(0.05)
    db.fill(0)
    db.rect(-2, -2, W + 2, H + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# DRAW THE GRAPHICS -------------------------------------------
GRID_VIEW = True
GRID_VIEW = False
draw_background()
MAIN_FONT_PATH = "fonts/BezyGrotesk-Regular.ttf"
db.openTypeFeatures(dlig=False)
db.font(MAIN_FONT_PATH)
db.stroke(None)

db.image("images/alpha/ai-art/earth-001.png", (U*1.25, U*6.0), alpha=1.0)

db.fill(0.8)
db.fontSize(128*3.7)
db.tracking(-16)
# MAIN TEXT ----------------------------------------------------
db.text("believe in", (M-(U*(0.3)), M+(U*(26))), align="left")
db.text("som\uF004ing", (M-(U*(0.3)), M+(U*(19.75))), align="left")


#db.fill(0.4)
db.fontSize(96-16)
db.tracking(None)
# AUXILARY TEXT -------------------------------------------------
#db.text(("\uE004 Font.Garden"),         (M+(U*(0)),  M+(U*(31))), align="left")
db.text(("World Computer"),         (M+(U*(0)),  M+(U*(0))), align="left")
#db.text("Bezy Grotesk Regular Alpha",    (M+(U*(0)),  M+(U*(0))),  align="left")

#db.text("SIL Open Font License", (M+(U*(32)), M+(U*(31))), align="right")
db.text("0xd4e56740f876aef8c",     (M+(U*(32)), M+(U*(0))),  align="right")


# SAVE THE IMAGE ----------------------------------------------
db.saveImage(args.output)
print("DrawBot: Done\n")


# SCRATCH PAD -------------------------------------------------
#db.lineHeight(FONT_SIZE*1.1)
#db.tracking(-1)
#db.textBox("أشهد يا إلهي بأنك خلقتني لعرفانك وعبادتك "*19,
#   (M+(M*0), M+(M*1.5), W-(M*2), H-(M*5)), align="right")



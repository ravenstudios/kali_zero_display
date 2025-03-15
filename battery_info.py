import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from PIL import Image, ImageDraw, ImageFont

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Read from A0 (use A1, A2, A3 for other channels)
chan = AnalogIn(ads, ADS.P0)







WIDTH = 128
HEIGHT = 64

def get_battery_info():
    return f"{chan.voltage:.2f}V"

def draw():
    # Clear the screen


    # Create a blank image for drawing
    image = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)

    # Load a bigger font
    # font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Change path if needed
    font = ImageFont.truetype("vcr.ttf", 24)  # Adjust font size

    # Display text with the larger font
    draw.text((5, 5), "Batt:", font=font, fill=255)
    draw.text((5, 25), get_battery_info(), font=font, fill=255)


    # Send image to OLED

    rotated_image = image.rotate(180, expand=True)  # You can change 90 to 180, 270, etc.

    # Resize the rotated image to fit the display dimensions (128x64)
    resized_image = rotated_image.resize((WIDTH, HEIGHT))

    # Send resized image to OLED
    return resized_image

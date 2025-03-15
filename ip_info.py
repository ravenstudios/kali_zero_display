import socket
from PIL import Image, ImageDraw, ImageFont

WIDTH = 128
HEIGHT = 64


def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except Exception:
        ip_address = "No IP"
    return ip_address


def get_host_name():
    return socket.gethostname()


def draw():
    # Clear the screen


    # Create a blank image for drawing
    image = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)

    # Load a bigger font
    # font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Change path if needed
    font = ImageFont.truetype("vcr.ttf", 16)  # Adjust font size

    # Display text with the larger font
    draw.text((5, 5), get_ip_address(), font=font, fill=255)
    draw.text((5, 16 + 5), "Host:", font=font, fill=255)
    draw.text((5, 32 + 5), get_host_name(), font=font, fill=255)

    # Send image to OLED

    rotated_image = image.rotate(180, expand=True)  # You can change 90 to 180, 270, etc.

    # Resize the rotated image to fit the display dimensions (128x64)
    resized_image = rotated_image.resize((WIDTH, HEIGHT))

    # Send resized image to OLED
    return resized_image

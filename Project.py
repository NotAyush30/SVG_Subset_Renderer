import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

tree = ET.parse("Demo.svg")
root = tree.getroot()

svg_width = int(root.get("width"))
svg_height = int(root.get("height"))

img = Image.new("RGB", (svg_width, svg_height), (255, 255, 255))

draw = ImageDraw.Draw(img)


def get_color(color):
    # If color is not given
    if color is None:
        return None

    if color.startswith("rgb"):
        color = color.replace("rgb(", "")
        color = color.replace(")", "")

        values = color.split(",")

        red = int(values[0])
        green = int(values[1])
        blue = int(values[2])

        return (red, green, blue)

    return color


for element in root:

    if element.tag == "rect":
        x = float(element.get("x"))
        y = float(element.get("y"))

        width = float(element.get("width"))
        height = float(element.get("height"))

        fill = get_color(element.get("fill"))
        stroke = get_color(element.get("stroke"))

        stroke_width = int(element.get("stroke-width", 1))

        # top-left = (x, y)
        # bottom-right = (x + width, y + height)

        draw.rectangle(
            ((x, y), (x + width, y + height)),
            fill=fill,
            outline=stroke,
            width=stroke_width,
        )


    elif element.tag == "circle":
        cx = float(element.get("cx"))
        cy = float(element.get("cy"))

        r = float(element.get("r"))

        fill = get_color(element.get("fill"))
        stroke = get_color(element.get("stroke"))

        stroke_width = int(element.get("stroke-width", 1))

        # cx = center x
        # cy = center y
        # r  = radius

        topleft = (cx - r, cy - r)
        bottomright = (cx + r, cy + r)

        draw.ellipse(
            (topleft, bottomright),
            fill=fill,
            outline=stroke,
            width=stroke_width,
        )


    elif element.tag == "ellipse":
        cx = float(element.get("cx"))
        cy = float(element.get("cy"))

        rx = float(element.get("rx"))
        ry = float(element.get("ry"))

        fill = get_color(element.get("fill"))
        stroke = get_color(element.get("stroke"))

        stroke_width = int(element.get("stroke-width", 1))

        topleft = (cx - rx, cy - ry)
        bottomright = (cx + rx, cy + ry)

        draw.ellipse(
            (topleft, bottomright),
            fill=fill,
            outline=stroke,
            width=stroke_width,
        )


    elif element.tag == "line":
        x1 = float(element.get("x1"))
        y1 = float(element.get("y1"))

        x2 = float(element.get("x2"))
        y2 = float(element.get("y2"))

        stroke = get_color(element.get("stroke"))

        stroke_width = int(element.get("stroke-width", 1))

        draw.line(
            ((x1, y1), (x2, y2)),
            fill=stroke,
            width=stroke_width,
        )


    elif element.tag == "text":
        x = float(element.get("x"))
        y = float(element.get("y"))

        font_size = int(element.get("font-size"))

        fill = get_color(element.get("fill"))

        text = element.text.strip()

        font = ImageFont.truetype("arial.ttf", font_size)

        draw.text(
            (x, y),
            text,
            font=font,
            fill=fill,
        )


img.save("Output.png")


img.show()

print("SVG successfully rendered to Output.png")

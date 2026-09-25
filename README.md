# SVG Subset Renderer

A lightweight vector graphics renderer built in Python that parses a simplified SVG file using xml.etree.ElementTree and rasterizes supported SVG elements using Pillow.

Currently supported:
rect, circle, ellipse, line, text, fill, stroke, stroke-width, named colors, HEX colors, and RGB colors.

Pipeline:
SVG → XML Parsing → Attribute Extraction → Pillow Rendering → PNG

Tech:
Python, Pillow, ElementTree

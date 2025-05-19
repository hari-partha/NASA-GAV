import pandas as pd
import json
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageOps import scale
import math
from itertools import groupby
import numpy as np
from statistics import mean

class BackgroundTemplate:
    '''
    Description: Background Template helps to define box methods to create the graphical abstract template 
    which will house all the necessary information needed for the graphical abstract visualizer
    '''
    def __init__(self, image_size, background_color='white'):
        self.image = Image.new('RGB', image_size, color=background_color)
        self.draw = ImageDraw.Draw(self.image)
        self.boxes = []

    def add_box(self, top_left, bottom_right, outline_color='black', fill_color=None, text=None, text_color='black'):
        box = {'top_left': top_left, 'bottom_right': bottom_right, 'outline_color': outline_color, 'fill_color': fill_color, 'text': text, 'text_color': text_color}
        self.boxes.append(box)

    def draw_boxes(self):
        for box in self.boxes:
            self.draw.rectangle([box['top_left'], box['bottom_right']], outline=box['outline_color'], fill=box['fill_color'])
            if box['text']:
                self._draw_centered_text(box['text'], box['top_left'], box['bottom_right'], box['text_color'])

    def _draw_centered_text(self, text, top_left, bottom_right, text_color, font = None):
        if font == None:
            font_path = "./fonts/Aptos-Bold.ttf"
            font_size = 16
            font = ImageFont.truetype(font_path, font_size)
        bbox = self.draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        box_width = bottom_right[0] - top_left[0]
        box_height = bottom_right[1] - top_left[1]
        x = top_left[0] + (box_width - text_width) / 2
        y = top_left[1] + (box_height - text_height) / 2
        self.draw.text((x, y), text, fill=text_color, font=font)


    def get_image(self):
        return self.image

    def paste(self, icon, icon_position, icon_type):
        self.image.paste(icon, icon_position, icon_type)

    def add_enclosed_boxes(self, enclosing_box_top_left, enclosing_box_bottom_right, num_inner_boxes, spacing, colors, texts):
        # Define the enclosing box
        self.add_box(enclosing_box_top_left, enclosing_box_bottom_right, outline_color='black', fill_color=None)
        
        # Calculate inner box dimensions and spacing
        enclosing_width = enclosing_box_bottom_right[0] - enclosing_box_top_left[0]
        enclosing_height = enclosing_box_bottom_right[1] - enclosing_box_top_left[1]
        box_width = enclosing_width - 2 * spacing
        box_height = (enclosing_height - (num_inner_boxes + 1) * spacing) // num_inner_boxes
        
        # Add inner boxes
        for i in range(num_inner_boxes):
            top_left = (enclosing_box_top_left[0] + spacing, enclosing_box_top_left[1] + spacing + i * (box_height + spacing))
            bottom_right = (top_left[0] + box_width, top_left[1] + box_height)
            self.add_box(top_left, bottom_right, outline_color='black', fill_color=colors[i % len(colors)], text=texts[i], text_color='white')
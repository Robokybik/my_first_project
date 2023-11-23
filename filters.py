from PIL import Image
from math import exp, e
import random

class Filter:
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        raise NotImplementedError()

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = img.getpixel((i, j))
                new_colors = self.apply_to_pixel(r, g, b)
                img.putpixel((i, j), new_colors)

        return img


class BreakingBadFilter(Filter):
    def apply_to_pixel(self, r, g, b):
        r = int(exp(r / 40) / e * 40)
        g = int(exp(g / 40) / e * 40)
        b = 10
        return r, g, b

class TheMatrixFilter(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        g = int(exp(r / 60) / e * 60)
        return r, g, b


class BarbieFilter(Filter):
    def apply_to_pixel(self, r, g, b):
        r = min(255, r + 100)
        g = max(0, g - 50)
        b = max(0, b - 50)
        return r, g, b

class BladeRunnerFilter(Filter):
    def apply_to_pixel(self, r, g, b):
        r = int(r * 0.9)
        g = int(g * 0.9)
        b = 150
        return r, g, b

class OppenheimerFilter(Filter):
    def apply_to_pixel(self, r, g, b):
        r = 255 if r > 128 else 0
        g = 255 if g > 128 else 0
        b = 255 if b > 128 else 0
        return r, g, b

class HorrorArgFilter(Filter):
    def __init__(self, noise_strength: float = 100):
        self.noise_strength = noise_strength

    def apply_to_pixel(self, r, g, b):
        r = min(255, r + 100)
        g = max(0, g - 100)
        b = max(0, b - 100)
        noise = [random.gauss(0, self.noise_strength) for _ in range(3)]
        new_colors = [int(round(c + n)) for c, n in zip((r, g, b), noise)]
        return tuple(new_colors)

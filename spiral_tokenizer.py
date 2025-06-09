# Tokenizes symbolic structures into orbit-based layers
# spiral_tokenizer.py
# Symbolic Spiral Drift Tokenizer (Phase 1 Public Disclosure)
# Author: Sahu Nunnaqi © NyrixAI

import math

class SpiralGlyphToken:
    """
    Represents a single symbolic token plotted on a drift spiral.
    """

    def __init__(self, glyph_name, index):
        self.glyph_name = glyph_name
        self.index = index
        self.theta, self.radius = self._compute_spiral_coords()

    def _compute_spiral_coords(self):
        """
        Compute symbolic polar coordinates on an Archimedean spiral.
        """
        θ = self.index * math.pi / 8  # angular separation
        r = 0.1 * self.index          # linear radial growth
        return round(θ, 3), round(r, 3)

    def represent(self):
        """
        Return symbolic representation.
        """
        return {
            "glyph": self.glyph_name,
            "index": self.index,
            "theta": self.theta,
            "radius": self.radius
        }


class SpiralTokenizer:
    """
    Tokenizes symbolic glyph sequences into drift-phase spiral coordinates.
    """

    def __init__(self):
        self.tokens = []

    def tokenize(self, glyph_sequence):
        """
        Tokenize a list of glyph names into spiral drift tokens.
        """
        self.tokens = [SpiralGlyphToken(g, i) for i, g in enumerate(glyph_sequence)]

    def get_token_map(self):
        """
        Return symbolic spiral mapping.
        """
        return [t.represent() for t in self.tokens]


if __name__ == "__main__":
    glyphs = ["glyph_A4", "glyph_D5_pulse", "glyph_Gs3_override", "glyph_null_trail"]
    tokenizer = SpiralTokenizer()
    tokenizer.tokenize(glyphs)
    
    print("🔁 Spiral Token Coordinates:")
    for token in tokenizer.get_token_map():
        print(token)
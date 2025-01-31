from typing import Optional

class HuffmanNode:
    def __init__(self,
                 freq: int,
                 char: Optional[str] = None,
                 left: Optional["HuffmanNode"] = None,
                 right: Optional["HuffmanNode"] = None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right


    def __lt__ (self, other: "HuffmanNode"):
        return self.freq < other.freq



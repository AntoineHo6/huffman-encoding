from huffmanNode import HuffmanNode
import heapq
from bitarray import bitarray
import sys


def buildHuffmanTree(freqTable: dict[str, int]) -> HuffmanNode:
    # min heap
    priorityQ = []

    for char, freq in freqTable.items():
        heapq.heappush(priorityQ, HuffmanNode(freq, char))

    while len(priorityQ) > 1:
        left = heapq.heappop(priorityQ)
        right = heapq.heappop(priorityQ)

        merged = HuffmanNode(left.freq + right.freq, char=None, left=left, right=right)

        heapq.heappush(priorityQ, merged)

    return priorityQ[0]


def buildHuffmanCodes(node: HuffmanNode, currentCode="", huffmanCodes={}):
    if node is None:
        return

    # is leaf node
    if node.char is not None:
        huffmanCodes[node.char] = currentCode
        return

    buildHuffmanCodes(node.left, currentCode + "0", huffmanCodes)
    buildHuffmanCodes(node.right, currentCode + "1", huffmanCodes)

    return huffmanCodes


def convertInputToHuffmanCodes(input: str, codes: dict[str, int]) -> bytes:
    encodedInput: list[str] = []
    for char in input:
        encodedInput.append(str(codes.get(char)))

    bitArr = bitarray("".join(encodedInput))

    return bitArr.tobytes()


if __name__ == '__main__':
    text = input("Enter some text to compress: ")

    freqTable = {}

    for char in text:
        if char in freqTable:
            freqTable[char] += 1
        else:
            freqTable[char] = 1

    huffmanTree: HuffmanNode = buildHuffmanTree(freqTable)

    codes = buildHuffmanCodes(huffmanTree)

    compressedResult = convertInputToHuffmanCodes(text, codes)

    print("Size in bytes BEFORE compression: {}".format(sys.getsizeof(text)))
    print("Size in bytes AFTER compression: {}".format(sys.getsizeof(compressedResult)))
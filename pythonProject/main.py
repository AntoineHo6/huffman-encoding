from queue import PriorityQueue

from huffmanNode import HuffmanNode
import heapq

if __name__ == '__main__':
    text = input("Enter some text to compress: ")

    freqTable = {}

    for char in text:
        if char in freqTable:
            freqTable[char] += 1
        else:
            freqTable[char] = 1


def buildHuffmanTree(freqTable: dict[str, int]) -> HuffmanNode:
    priorityQ = []

    for char, freq in freqTable.items():
        heapq.heappush(priorityQ, HuffmanNode(freq, char))

    while len(priorityQ) > 1:
        left = heapq.heappop(priorityQ)
        right = heapq.heappop(priorityQ)

        merged = HuffmanNode(left.freq + right.freq)

        heapq.heappush(priorityQ, merged)

    return priorityQ[0]



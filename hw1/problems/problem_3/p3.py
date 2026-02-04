import heapq
from collections import Counter

# A Node class is useful for building the Huffman tree.
class Node:
    def __init__(self, symbol, freq, left=None, right=None):
        """Initializes a Node for the Huffman tree."""
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        """Overloads the less-than operator to allow Node objects to be compared in a min-heap."""
        return self.freq < other.freq

def run_length_encode(data_block):
    """
    Performs Run-Length Encoding on a single block of quantized DCT coefficients.

    Args:
        data_block (list[int]): A list of 64 integers representing one block that has been
                                quantized and zig-zag scanned.

    Returns:
        list[tuple]: A list of RLE symbols. Each symbol is either ('EOB',)
                     or (num_zeros, value).
    """
    # <<< YOUR IMPLEMENTATION HERE >>>
    #
    # Example: [52, -7, 0, 0, 3, 0, -2, 0, ..., 0] -> [(0, 52), (0, -7), (2, 3), (1, -2), ('EOB',)]
    #
    # Hint: Iterate through the block. If you see a zero, increment a counter.
    # If you see a non-zero value, create a symbol with the current zero count
    # and the value, then reset the counter. Don't forget the EOB symbol
    # when you reach the end of the non-zero coefficients.
    zero_counter = 0
    rle_list = []
    list_length = len(data_block)

    for index, i in enumerate(data_block):
        if i == 0:
            zero_counter+=1
        else:
            rle_list.append((zero_counter,i))
            zero_counter = 0
        if index == list_length - 1:
            rle_list.append(('EOB',))

    return rle_list


def huffman_compress(all_rle_symbols):
    """
    Generates Huffman codes and encodes a stream of RLE symbols.

    Args:
        all_rle_symbols (list[tuple]): A list of all RLE symbols from an entire image.

    Returns:
        tuple[dict, str]: A tuple containing:
            - A dictionary mapping each unique RLE symbol to its Huffman code (binary string).
            - The fully encoded data as a single binary string.
    """
    if not all_rle_symbols:
        return {}, ""

    # 1. Calculate frequency of each RLE symbol. `collections.Counter` is useful.
    ctr = Counter(all_rle_symbols)

    # 2. Build the Huffman tree using a priority queue. `heapq` is recommended.
    #    - Create a leaf Node for each symbol and add it to the heap.
    #    - While the heap has more than one node, pop the two lowest frequency nodes,
    #      merge them into a new internal node, and push it back onto the heap.
    heap = []
    heapq.heapify(heap)
    for i in set(all_rle_symbols):
        heapq.heappush(heap, Node(i, ctr[i]))

    while len(heap) > 1:
        low1 = heapq.heappop(heap)
        low2 = heapq.heappop(heap)
        heapq.heappush(heap, Node(None, low1.freq + low2.freq, low1, low2))

    # 3. Traverse the tree to generate Huffman codes. A recursive helper function is a good approach.
    def traverse_tree(root, code, map):
        if root.symbol:
            map[root.symbol] = ''.join(code)
        else:
            code.append('0')
            traverse_tree(root.left,code,map)
            code.pop()
            code.append('1')
            traverse_tree(root.right,code,map)
            code.pop()


    # 4. Encode the `all_rle_symbols` list into a single bitstring using your generated codes.
    root_node = heapq.heappop(heap)
    huffman_codes = {}
    traverse_tree(root_node,[],huffman_codes)

    if root_node.left == None and root_node.right == None:
        huffman_codes[root_node.symbol] = ''.join('0')

    encoded_data = ""
    for i in all_rle_symbols:
        encoded_data += huffman_codes[i] 
    
    return huffman_codes, encoded_data

print(run_length_encode([]))
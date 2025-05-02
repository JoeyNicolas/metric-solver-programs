def hamming_distance(s1, s2):
    """
    Calculate the Hamming distance between two strings.
    
    The Hamming distance is defined as the number of positions at which
    the corresponding symbols in two strings differ.
    
    Note: If strings have different lengths, we can either:
    1. Only compare up to the length of the shorter string
    2. Consider the difference in length as additional edits
    
    This implementation uses option 2, which is a modified Hamming distance.
    """
    # If strings have different lengths, count the length difference as edits
    if len(s1) != len(s2):
        # Calculate the common length to compare
        min_len = min(len(s1), len(s2))
        # Add the length difference to the distance
        length_diff = abs(len(s1) - len(s2))
    else:
        min_len = len(s1)
        length_diff = 0
    
    # Count positions where characters differ
    distance = sum(s1[i] != s2[i] for i in range(min_len))
    
    # Add the length difference to get the total distance
    return distance + length_diff

# Word pairs to analyze
word_pairs = [
    ("haus", "maus"),
    ("tier", "stier"),
    ("abfliegen", "abfedern")
]

# Calculate and display the Hamming distance for each pair
print("Hamming Edit Distance Results:")
print("-" * 40)
for pair in word_pairs:
    word1, word2 = pair
    distance = hamming_distance(word1, word2)
    print(f"• {word1} - {word2}: {distance}")
    
    # Additional detailed explanation
    if len(word1) != len(word2):
        print(f"  (Different lengths: {len(word1)} vs {len(word2)})")
    
    # Show character-by-character comparison
    comparison = []
    min_len = min(len(word1), len(word2))
    for i in range(min_len):
        if word1[i] == word2[i]:
            comparison.append(" ")  # Same character
        else:
            comparison.append("^")  # Different character
    
    print(f"  {word1}")
    print(f"  {word2}")
    print(f"  {''.join(comparison)}")
    
    if len(word1) != len(word2):
        # Show the extra characters
        if len(word1) > len(word2):
            print(f"  Plus {len(word1) - len(word2)} extra character(s) in first word")
        else:
            print(f"  Plus {len(word2) - len(word1)} extra character(s) in second word")
    
    print()
def longest_common_subsequence(s1, s2):
    """
    Find the longest common subsequence of two strings.
    
    A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
    For example, "abc", "abg", "bdf", "aeg", "acefg", .. are subsequences of "abcdefg".
    
    Returns:
        tuple: (LCS length, LCS string, LCS distance)
        LCS distance = len(s1) + len(s2) - 2 * LCS_length
    """
    # Create a table to store lengths of LCS for all subproblems
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Reverse the LCS list to get the correct order
    lcs = ''.join(reversed(lcs))
    
    # Calculate LCS distance
    lcs_length = dp[m][n]
    lcs_distance = len(s1) + len(s2) - 2 * lcs_length
    
    return lcs_length, lcs, lcs_distance

def find_all_subsequences(s):
    """
    Find all possible subsequences of a string.
    Warning: This grows exponentially with string length!
    """
    n = len(s)
    # 2^n combinations (including empty string)
    subsequences = []
    
    # Generate all subsequences using binary representation
    for i in range(1, 1 << n):
        subsequence = ''.join(s[j] for j in range(n) if (i & (1 << j)))
        subsequences.append(subsequence)
    
    return sorted(subsequences, key=len)

# Word pairs to analyze
word_pairs = [
    ("trier", "stier"),
    ("halt", "fault"),
    ("ab", "ba")
]

# Calculate and display the LCS distance for each pair
print("Längste-Gemeinsame-Teilsequenz-Distanz:")
print("-" * 50)

for pair in word_pairs:
    word1, word2 = pair
    lcs_length, lcs, lcs_distance = longest_common_subsequence(word1, word2)
    
    # Find all subsequences (limited to reasonable size strings)
    if len(word1) <= 8 and len(word2) <= 8:
        subseq1 = find_all_subsequences(word1)
        subseq2 = find_all_subsequences(word2)
    else:
        subseq1 = ["Too many to display"]
        subseq2 = ["Too many to display"]
    
    # Display results
    print(f"• {word1} - {word2}:")
    print(f"  LCS: '{lcs}' (Länge: {lcs_length})")
    print(f"  LCS-Distanz: {lcs_distance}")
    
    print(f"  Alle Teilsequenzen von '{word1}':")
    # Print subsequences in groups of 8 per line
    for i in range(0, len(subseq1), 8):
        print(f"    {', '.join(repr(s) for s in subseq1[i:i+8])}")
    
    print(f"  Alle Teilsequenzen von '{word2}':")
    for i in range(0, len(subseq2), 8):
        print(f"    {', '.join(repr(s) for s in subseq2[i:i+8])}")
    
    print()
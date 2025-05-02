def levenshtein_distance(s1, s2, show_table=True):
    """
    Calculate the Levenshtein edit distance between two strings.
    
    The Levenshtein distance is the minimum number of single-character edits
    (insertions, deletions or substitutions) required to change one string into the other.
    
    Parameters:
    s1 (str): First string
    s2 (str): Second string
    show_table (bool): If True, print the dynamic programming table
    
    Returns:
    int: The Levenshtein distance between s1 and s2
    """
    # Create a table to store results of subproblems
    # Size of the table is (len(s1)+1) x (len(s2)+1)
    rows = len(s1) + 1
    cols = len(s2) + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Initialize the first row and column
    for i in range(rows):
        dp[i][0] = i  # Cost of transforming s1[:i] to empty string
    
    for j in range(cols):
        dp[0][j] = j  # Cost of transforming empty string to s2[:j]
    
    # Fill the dp table
    for i in range(1, rows):
        for j in range(1, cols):
            # If characters match, no additional cost
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Take the minimum of:
                # 1. Replace: dp[i-1][j-1] + 1
                # 2. Insert: dp[i][j-1] + 1
                # 3. Delete: dp[i-1][j] + 1
                dp[i][j] = min(dp[i-1][j-1] + 1,  # Replace
                               dp[i][j-1] + 1,    # Insert
                               dp[i-1][j] + 1)    # Delete
    
    # Display the table if requested
    if show_table:
        # Print table header with better formatting
        print(f"\nLevenshtein distance table for '{s1}' and '{s2}':")
        print()
        
        # Create the top row with column indices and second string characters
        header = "     |"
        for j in range(cols):
            if j == 0:
                header += "   |"
            else:
                header += f" {s2[j-1]} |"
        print(header)
        
        # Print a separator line
        separator = "-----+" + "---+" * cols
        print(separator)
        
        # Print the table rows with row indices and first string characters
        for i in range(rows):
            row = ""
            if i == 0:
                row += "     |"
            else:
                row += f"  {s1[i-1]}  |"
                
            for j in range(cols):
                # Highlight matches with a different format
                if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
                    row += f" {dp[i][j]}*|"
                else:
                    row += f" {dp[i][j]} |"
            print(row)
            print(separator)
        
        # Add a legend for the highlighted cells
        print("\n* Matching characters (no substitution cost)")
        print()
    
    # Return the final distance
    return dp[rows-1][cols-1]

# Word pairs to analyze
word_pairs = [
    ("frisch", "licht"),
    ("suchleiste", "schalter")
]

# Calculate and display the Levenshtein distance for each pair
print("Levenshtein Edit Distance Results:")
print("=" * 50)
for pair in word_pairs:
    word1, word2 = pair
    print(f"• {word1} - {word2}:")
    distance = levenshtein_distance(word1, word2)
    print(f"  Levenshtein distance: {distance}")
    print("-" * 50)
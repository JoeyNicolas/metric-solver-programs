#!/usr/bin/env python3      
"""
Basic Python script template
"""

import os
import sys

text_x = "maus"
text_y = "haus"


def main():
    """Main function of the script."""
    print("Hello, World!")
    cost = 0
    for i in range(len(text_x)):
        for j in range(len(text_y)):
            # if text_x[i] == text_y[j]:
            #     print(text_x[i], "==", text_y[j], end=" ")
            #     cost += 0
            #     print(cost, end=" ")
            # elif text_x[i-1] != text_y[j]:
            #     cost += 1
            #     print(cost, end=" ")
            helper_function(i,j)
        print()
    print("--------------")        
    # Your code goes here
    for i in range(len(text_x)):
        for j in range(len(text_y)):
            print(matrix[i][j], end=" ")
        print()
    
matrix = [[0 for i in range(len(text_x)+1)] for j in range(len(text_y)+1)] # matrix x*y 

def helper_function(i, j):
    """Helper function for the main function."""
    # minimal_cost= 0
    minimal_cost= min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])
    print("return of min: ", minimal_cost)
    # check top left corner cost if characters are the same called match
    if text_x[i] == text_y[j]:
        # if i > 0 and j > 0:
            # minimal_cost = matrix[i-1][j-1]
        # minimal_cost += 0
        matrix[i][j] = minimal_cost
        
    # check top cost if characters are different called insert
    else:
        # if i > 0 :
            # minimal_cost = matrix[i-1][j]
        matrix[i][j] = minimal_cost + 1
        
    # check left cost if characters are different called delete
        # if j > 0:
            # minimal_cost = matrix[i][j-1]
        matrix[i][j] = minimal_cost + 1
    #if first row && no match
        # if i==0:
            # matrix[i][j] = minimal_cost + 1
        
    # print(minimal_cost, end=" ")    
    # return the minimum cost
    
if __name__ == "__main__":
    main()
    
    #
    #   [0],[1]
    #   -----
    #   [1],[o]
    #
    #
    #
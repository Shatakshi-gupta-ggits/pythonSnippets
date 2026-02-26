# # Python Loops with Patterns - Beginner's Guide

# ## What is a Loop?
# A loop is used to repeat a block of code multiple times. Think of it like telling Python "do this thing X times" or "keep doing this until something changes".

# ## Types of Loops in Python

# ### 1. **For Loop** - Used when you know how many times to repeat
# ### 2. **While Loop** - Used when you repeat until a condition is met

# ## Pattern 1: Square Pattern

# *****
# *****
# *****
# *****
# *****
# ```


# # Square pattern of 5x5 stars
# for i in range(5):          # Outer loop for rows (runs 5 times)
#     for j in range(5):       # Inner loop for columns (runs 5 times)
#         print("*", end="")   # Print star without new line
#     print()                  # Print new line after each row
# ```

# **Explanation:**
# - `range(5)` creates numbers 0,1,2,3,4 (5 times)
# - Outer loop runs 5 times for 5 rows
# - Inner loop runs 5 times for 5 stars in each row
# - `end=""` keeps printing on the same line
# - Empty `print()` moves to next line

# ---

# ## Pattern 2: Right Triangle
# ```
# *
# **
# ***
# ****
# *****
# ```

# **Solution:**
# ```python
# # Right triangle pattern
# rows = 5
# for i in range(1, rows + 1):     # i goes from 1 to 5
#     for j in range(i):            # j runs i times
#         print("*", end="")
#     print()
# ```

# **Explanation:**
# - `i` increases each time: 1, then 2, then 3, etc.
# - When `i=1`, inner loop runs 1 time → prints 1 star
# - When `i=2`, inner loop runs 2 times → prints 2 stars
# - And so on...

# ---

# ## Pattern 3: Inverted Triangle
# ```
# *****
# ****
# ***
# **
# *
# ```

# **Solution:**
# ```python
# # Inverted triangle pattern
# rows = 5
# for i in range(rows, 0, -1):     # i goes from 5 down to 1
#     for j in range(i):            # j runs i times
#         print("*", end="")
#     print()
# ```

# **Explanation:**
# - `range(rows, 0, -1)` counts backwards: 5,4,3,2,1
# - When `i=5`, print 5 stars
# - When `i=4`, print 4 stars
# - Stars decrease each row

# ---

# ## Pattern 4: Pyramid
# ```
#     *
#    ***
#   *****
#  *******
# *********
# ```

# **Solution:**
# ```python
# # Pyramid pattern
# rows = 5
# for i in range(1, rows + 1):
#     # Print spaces (decreases as i increases)
#     for j in range(rows - i):
#         print(" ", end="")
    
#     # Print stars (increases as i increases)
#     for k in range(2 * i - 1):
#         print("*", end="")
    
#     print()  # Move to next line
# ```

# **Explanation:**
# - Spaces = `rows - i` (5-1=4 spaces first row, 5-2=3 spaces second row)
# - Stars = `2*i - 1` (1,3,5,7,9 stars)
# - First loop prints spaces to center the pyramid
# - Second loop prints the stars

# ---

# ## Pattern 5: Diamond
# ```
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# ```

# **Solution:**
# ```python
# # Diamond pattern
# rows = 5

# # Top half (including middle)
# for i in range(1, rows + 1):
#     # Spaces
#     for j in range(rows - i):
#         print(" ", end="")
#     # Stars
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

# # Bottom half
# for i in range(rows - 1, 0, -1):
#     # Spaces
#     for j in range(rows - i):
#         print(" ", end="")
#     # Stars
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()
# ```

# ---

# ## Pattern 6: Number Pattern
# ```
# 1
# 12
# 123
# 1234
# 12345
# ```

# **Solution:**
# ```python
# # Number pattern
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
# ```

# **Explanation:**
# - Instead of `*`, we print `j` which changes each time
# - `j` goes from 1 to i, creating increasing numbers

# ---

# ## Pattern 7: Alphabet Pattern
# ```
# A
# BB
# CCC
# DDDD
# EEEEE
# ```

# **Solution:**
# ```python
# # Alphabet pattern
# rows = 5
# for i in range(rows):
#     for j in range(i + 1):
#         # chr(65) = 'A', chr(66) = 'B', etc.
#         print(chr(65 + i), end="")
#     print()
# ```

# ---

# ## Quick Tips for Beginners:

# 1. **Start Small**: Try with 3 rows first, then increase
# 2. **Use Print Statements**: Add `print(f"i={i}, j={j}")` inside loops to see what's happening
# 3. **Naming**: Use meaningful variable names:
#    - `i` = rows (outer loop)
#    - `j` = columns (inner loop)
# 4. **Remember**: 
#    - Outer loop = rows
#    - Inner loop = columns/stars in each row

# ## Practice Exercise:
# Try to create this pattern:
# ```
# 1
# 22
# 333
# 4444
# 55555
# ```

# **Solution:**
# ```python
# for i in range(1, 6):
#     for j in range(i):
#         print(i, end="")
#     print()
# ```

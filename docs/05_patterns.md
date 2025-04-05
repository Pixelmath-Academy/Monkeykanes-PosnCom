# Python Pattern Printing

This section covers various pattern printing examples in Python.

## Contents

1. [Right Triangle Patterns](#right-triangle-patterns)
2. [Pyramid Patterns](#pyramid-patterns)
3. [Number Patterns](#number-patterns)
4. [Diamond Patterns](#diamond-patterns)
5. [Special Patterns](#special-patterns)

## Right Triangle Patterns

File: `05_patterns/01_right_triangle.py`

Basic right triangle patterns using loops.

### Examples:
```python
# Right triangle with stars
*
**
***
****
*****

# Inverted right triangle
*****
****
***
**
*

# Right triangle with spaces
    *
   **
  ***
 ****
*****

# Right triangle with spaces (inverted)
*****
 ****
  ***
   **
    *
```

## Pyramid Patterns

File: `05_patterns/02_pyramid.py`

Pyramid patterns using nested loops.

### Examples:
```python
# Basic pyramid
    *
   ***
  *****
 *******
*********

# Inverted pyramid
*********
 *******
  *****
   ***
    *

# Number pyramid
    1
   2 3
  4 5 6
 7 8 9 10
11 12 13 14 15
```

## Number Patterns

File: `05_patterns/03_number_patterns.py`

Patterns using numbers and mathematical sequences.

### Examples:
```python
# Number triangle
1
12
123
1234
12345

# Number pyramid
    1
   121
  12321
 1234321
123454321

# Pascal's triangle
1
11
121
1331
14641
```

## Diamond Patterns

File: `05_patterns/04_diamond.py`

Diamond-shaped patterns using loops.

### Examples:
```python
# Basic diamond
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

# Diamond with spaces
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
```

## Special Patterns

File: `05_patterns/05_special_patterns.py`

Special patterns like hollow squares and alternating patterns.

### Examples:
```python
# Hollow square
*****
*   *
*   *
*   *
*****

# Cross pattern
*   *
 * * 
  *  
 * * 
*   *

# Checkerboard pattern
* * * * *
 * * * * *
* * * * *
 * * * * *
* * * * *
```

### Pattern Printing Tips:
1. Use nested loops for complex patterns
2. Consider using string multiplication for repeated characters
3. Use end="" in print() for same-line printing
4. Break down complex patterns into simpler parts
5. Use mathematical formulas for number patterns 
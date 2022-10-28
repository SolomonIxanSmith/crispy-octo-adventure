# GOAL

Write a program with two functions **initMaze**() and **printMaze**().  The prototypes for these two functions are shown below:

``` 
 def initMaze( myMaze, gapSize ) # initialize outer and inner walls of the maze based on the numpy array and gap size given
 def printMaze( myMaze ) # print the maze
```

Note that these functions expect to be passed a previously declared 2D numpy array of characters (str type)  with a user-specified square number of rows and columns;   (Your functions should assess the dimension of the 2D array using the shape attribute (a tuple) of the numpy array argument passed to the function).  

You will use these functions to programmatically initialize and then print a 2D numpy array of characters that represents a Maze. 


# Details
Your Maze will have an inner and outer wall as shown in the Example output below, where the inner wall is separated from the outer wall by a user-specified gap size.

Your maze must be comprised of an **OUTER** wall on all four sides, where walls are represented by a star character: *.

You must also create an **INNER** wall for the maze ( comprised of plus +  characters) where each of its wall are placed at a user-specified gap size (in characters) from the outer wall.  The gap specified must be a positive value, where a 0 means there is no gap between the inner and outer wall; a gap size of 1 leaves a clear space of size 1 between the inner and outer wall, etc.  Your program should produce an inner all for gap sizes 0, 1, 2,  and 3.  Gap sizes >3 should produce no inner wall.

# Steps in Main
1. Prompt the user for the dimension size and for the gap size in the main section
2. Create the numpy array of the proper dimensions
3. Pass the array and gap size to your initMaze() function, which will assign either a * (star), + (plus), or blank to each location in the numpy array
4. Pass the numpy array to printMaze() function, which will print it row by row (with no extra spaces between array character - let your "square maze" be printed in its natural "rectangular" appearance in the console for this assignment)

# EXAMPLES

Example 1: 10x10 outer wall and inner wall with user-specified gap == 2 (2 character spaces between the inner and outer walls, left, right, top, and bottom)

```
**********
*        *
*        *
*  ++++  *
*  +  +  *
*  +  +  *
*  ++++  *
*        *
*        *
**********
```

_note: the maze above IS a 10x10 square, even though it is appears rectangular when printed_

Example 2: 10x10 outer wall and inner wall with user-specified gap == 0 (zero space between inner and outer walls)

```
**********
*++++++++*
*+      +*
*+      +*
*+      +*
*+      +*
*+      +*
*+      +*
*++++++++*
**********
```

_note: the maze above IS a 10x10 square, even though it is appears rectangular when printed_

Example 3: 10x10 outer wall and inner wall with user-specified gap == 10 (no inner wall)

```
**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
```
_note: the maze above IS a 10x10 square, even though it is appears rectangular when printed_



Example 4: 15x15 outer wall and inner wall with user-specified gap == 3 (3 character gap between inner and outer wall on all sides)

```
***************
*             *
*             *
*             *
*   +++++++   *
*   +     +   *
*   +     +   *
*   +     +   *
*   +     +   *
*   +     +   *
*   +++++++   *
*             *
*             *
*             *
***************
```
# REQUIREMENTS

- You must programmatically generate the inner wall using loops and if-else statements, likely utilizing compound logical if-conditionals (with parenthesis and combinations of "and" and "or" ).
- Your program should work for inner walls with a gap of 0, 1, 2, or 3.
- Gap sizes >3 should produce no inner wall.
- Your inner wall must use a plus + character and your outer wall must use a star * character
- You should not add any extra spaces in your output to make your maze appear perfect square when printed (for this assignment)

# RESTRICTIONS

- You are not allowed to store pre-made solutions to the maze in your "initMaze() function.  You must generate your solutions programmatically.
- You must produce a "clear gap" between the outer and inner walls at all times.

# HINTS

- Initialize a simple maze first, with only the outer wall, using the star * character 
- Once you have the outer wall looking correct, work on the inner wall based on the gap parameter, using the plus + character
- Due to screen display attributes, your printed Maze will not be square even though it will have the same number of rows and columns (see example above)


# SCORING out of 100 points

- +15 points : function definitions match prototypes provided
- +15 points: initMaze() correctly initializes walls of the 2D array to the *
- +15 points: initMaze() correctly initializes interior of 2D array to blank (where there is no inner wall)
- +15 points: initMaze() does not create an inner wall if the gap size is > 3
- +15 points: initMaze() correctly initializes inner wall of 2D array to + for gap sizes 0, 1, 2, and 3
- +25 points: printMaze() correctly prints the  maze of the user-specified dimension

# Testing
- To run all tests, in the Shell (next to the Console button in repl), type: python -m unittest testMe.py
- All tests should pass, resulting in an "OK" at the end of your test output
- If any tests fail you will see "FAILED (failures=#)"  where # indicates the number of tests which failed


# Submission
- After testing, submit a link to your repl on canvas for this specific assignent


# Concepts Covered
- 2D numpy arrays
- assigning characters to 2D array positions
- passing arrays to functions as arguments
- defining and calling functions
- coding 2D initialization logic


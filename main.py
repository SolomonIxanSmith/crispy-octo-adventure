import numpy
#import random

def printMaze( myMaze ) :  
  for row in range(0,myMaze.shape[0]):    
    for col in range(0,myMaze.shape[1]):
      print(myMaze[row][col],end="")
    print()
# end function


# TODO STEP 4B: define your initMaze() function here
def initMaze( myMaze, gap) :  
  rowMaxIndex=myMaze.shape[0]-1
  colMaxIndex=myMaze.shape[1]-1
  gap+=1 #add 1 to gap to account for the encircling walls
  
  for row in range(0,rowMaxIndex+1): 
    for col in range(0,colMaxIndex+1):
      if(row%(rowMaxIndex)==0 or col%(colMaxIndex)==0):
        myMaze[row][col]="*"
      elif((row == gap or row == rowMaxIndex-gap) and (col >= gap and col <= colMaxIndex-gap)):
        myMaze[row][col]="+"
      elif((col == gap or col == colMaxIndex-gap) and (row >= gap and row <= rowMaxIndex-gap)):
        myMaze[row][col]="+"
      else:
        myMaze[row][col]=" "
    # end function

  
# --------------- main section --------------------
if __name__ == "__main__":
  rows=int(input("Number of Rows:\n"))
  columns = int(input("Number of Columns:\n"))
  #columns = rows
  gapSize=int(input("Size of gap between inner and outer walls:\n"))
  strArray=numpy.full((rows,columns),"",dtype=str)# 
  initMaze(strArray,gapSize)
  printMaze(strArray)
  #print(rows, columns, gapSize)



import unittest
#import main
import os

# to run tests, in the Shell, type: python -m unittest testMe.py

# NOTE: Please do not remove this file from your repl
# it is required to perform testing on your submission
import sys
from contextlib import contextmanager
from contextlib import redirect_stdout
from io import StringIO 

inputStrings = [
("10\n4\n", 
"**********\n\
*        *\n\
*        *\n\
*        *\n\
*        *\n\
*        *\n\
*        *\n\
*        *\n\
*        *\n\
**********"), 

("10\n3\n", 
"**********\n\
*        *\n\
*        *\n\
*        *\n\
*   ++   *\n\
*   ++   *\n\
*        *\n\
*        *\n\
*        *\n\
**********"), 

("10\n2\n", 
"**********\n\
*        *\n\
*        *\n\
*  ++++  *\n\
*  +  +  *\n\
*  +  +  *\n\
*  ++++  *\n\
*        *\n\
*        *\n\
**********"), 

("10\n1\n", 
"**********\n\
*        *\n\
* ++++++ *\n\
* +    + *\n\
* +    + *\n\
* +    + *\n\
* +    + *\n\
* ++++++ *\n\
*        *\n\
**********"), 

("10\n0\n", 
"**********\n\
*++++++++*\n\
*+      +*\n\
*+      +*\n\
*+      +*\n\
*+      +*\n\
*+      +*\n\
*+      +*\n\
*++++++++*\n\
**********"),

("30\n3\n", 
"******************************\n\
*                            *\n\
*                            *\n\
*                            *\n\
*   ++++++++++++++++++++++   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   +                    +   *\n\
*   ++++++++++++++++++++++   *\n\
*                            *\n\
*                            *\n\
*                            *\n\
******************************")

]

@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig

class TestMe( unittest.TestCase ):

  def test_all(self):
    self.maxDiff = None # enables us to see full diff if output is wrong
    for testNum in range(0, len(inputStrings), 1): # run tests 0 through len()
      inputString = inputStrings[testNum][0] # get the full input string for this test, delineated with returns
      print("\nStarting test #", testNum)
      print( "Testing game with input string:", inputString.replace("\n", " ") )
      outFileName = "testingOutputTemp.txt"
      #print( "\n:Redirecting all output into the file", outFileName)
      self.maxDiff = None # enables us to see full diff if output is wrong
      if os.path.exists(outFileName): # if we have an old file
        os.remove(outFileName) # remove any old versions of this file
      with open(outFileName, "w") as outFile: # now open the file for writing 
        with redirect_stdout(outFile): # redirect all output to this temp file
          with replace_stdin(StringIO(inputString)): # here we take over the usual stdin and force our own input "rock"
            #main.dungeonEscape() # writes output to "testingOutputTemp.txt" instead of stdout
            with open("main.py") as mainFile: # open main as an input file so we can execute it directly
              exec(mainFile.read()) # read the entire content of main and execute the string (file will close after with scope)

        
      try:
        #print("    opening test file....")
        inFile = open(outFileName) # try to open the file
      except:
        self.assertEqual( True, False, msg = "    Error: could not open interim output file " + outFileName )
        
      outputString = inFile.read() # read in the output from main
      inFile.close()
      #print("    checking test file output=\n", outputString)
      #print("    searching for the word", inputStrings[testNum][1] )
      pos = outputString.find(inputStrings[testNum][1])

      if (pos < 0 ):
        print("    *** Error: test#", testNum, "does not appear to match the following test maze string:\n", inputStrings[testNum][1] )
        print("    *** Please review the file", outFileName, "in your repl, for output from your program for the input string shown above" )
        self.assertEqual(True, False, msg="(Abort)"  ) # stops here if assert fails
      print("test", testNum, "is ok")


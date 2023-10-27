''' 
Each of the test file in each of the folder will check if your implementation
for the function defined in the 'name_of_the_exercise.py' file is correct.

This file will tests if you have implemented the function return_magic_number()
correctly (it should return the number 42).

Just run the file and see if it passes the test.

If it does, well done, go to the next exercise folder and repeat the process.

    Ran 1 test in 0.000s
    OK

If it doesn't, go back to the 'name_of_the_exercise.py' file and try again.

    Ran 1 test in 0.001s
    FAILED (failures=1)

P.S. If you're stuck, you can always use Google to help you out, but try not to use ChatGPT.

Good luck and have fun!
'''


# import unittest means that we are importing a module called unittest
# that allows you to write tests for your code (here I use it to test your code)
import unittest

# I then import the function that you need to implement to this test file
# so that I can test it
from start_here import return_magic_number


# TestReturnMagicNumber is the name of the class that will contain the tests
# This class inherits from unittest.TestCase so that it can use the functions
# defined in the unittest module
class TestReturnMagicNumber(unittest.TestCase):
    # test_return_magic_number is the function that will test your implementation
    def test_return_magic_number(self):
        # self.assertEqual is a function from the unittest module
        # that will check if the first argument is equal to the second argument.
        # In this case, it will check if the return_magic_number() function
        # returns the number 42.
        self.assertEqual(return_magic_number(), 42)


# This is a special line that tells Python to run
if __name__ == '__main__':
    unittest.main()

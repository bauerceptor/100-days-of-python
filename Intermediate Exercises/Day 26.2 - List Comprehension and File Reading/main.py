with open('./file1.txt') as file1:
  list1 = file1.readlines()

with open('./file2.txt') as file2:
  list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

#First *fork* your copy. 
#Copy Paste your code above this line 👆
#Then click "Run" to execute the tests

print(result)






















































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇
with open('file1.txt', 'w') as file:
  file.write('1\n2\n3\n4\n5\n6\n7\n8\n')

with open('file2.txt', 'w') as file:
  file.write('1\n20\n3\n49\n5\n67\n7\n86\n')

with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:40]
    for x in f2:
      file.write("    " + x)

import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):

  def run_test(self, expected_print): 
    with patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      self.assertEqual(fake_out.getvalue(), expected_print) 

  # Original file1 and file2 print
  # def test_1(self):
  #   self.run_test(expected_print="[3, 6, 5, 33, 12, 7, 42, 13]\n")

  def test_1(self):
    self.run_test(expected_print="[1, 3, 5, 7]\n")


print('\n\n\n.\n.\n.')
print('Checking if what you printed is a list containing the numbers present in both files for a different file contents ...')
print('Running some tests on your code:')
print('.\n.\n.\n.')
unittest.main(verbosity=1, exit=False)

# Restoring original values
with open('file1.txt', 'w') as file:
  file.write('3\n6\n5\n8\n33\n12\n7\n4\n72\n2\n42\n13\n')

with open('file2.txt', 'w') as file:
  file.write('3\n6\n13\n5\n7\n89\n12\n3\n33\n34\n1\n344\n42\n')

os.remove('testing_copy.py')
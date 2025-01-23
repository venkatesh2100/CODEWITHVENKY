from squareNum import square



def test_square():
  assert square(2)==4
  assert square(3)==9
  assert square(0)==0
  # def main():
#   test_square()


# Test by manul try except block
# def test_square():
#   try:
#     assert square(2)==4
#   except AssertionError:
#     print("Status Error of 2")
#   try:
#     assert square(3)==9
#   except AssertionError:
#     print("Error of 3")


#   try:
#     assert square(0)==0
#   except AssertionError:
#     print("Status Error")

  # if square(2)!=4:
  #   print("Error Occured")
  # if square(3)!=9:
  #   print("Error Occured")
  # else:
  #   print("code run 200 ook")


# if __name__=="__main__":
#   main()
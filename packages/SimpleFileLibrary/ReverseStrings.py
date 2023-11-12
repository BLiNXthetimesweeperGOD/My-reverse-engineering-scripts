#A bunch of functions for flipping/reversing stuff
def reverse_string(input_string):
  # initialize an empty string to store the reversed string
  reversed_string = ""
  # loop through the input string from the last character to the first
  for i in range(len(input_string) - 1, -1, -1):
    # append each character to the reversed string
    reversed_string += input_string[i]
  # return the reversed string
  return reversed_string

def reverse_byte_string(input_byte_string):
  # convert the byte string to a list of integers
  input_list = list(input_byte_string)
  # reverse the list using slicing
  reversed_list = input_list[::-1]
  # convert the reversed list back to a byte string
  reversed_byte_string = bytes(reversed_list)
  # return the reversed byte string
  return reversed_byte_string

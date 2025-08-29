#!/usr/bin/env python3
import hashlib
import os
import sys


def file_hash(complete_file_path):
  """Return the hash of the file at complete_file_path"""
  # Hint: Use os.path.exists() to check if the file exists
  does_path_exist = os.path.exists(complete_file_path)
  # Hint: If the file does not exist, return "FILE NOT FOUND"
  if does_path_exist == False:
    return "FILE NOT FOUND"
  # Hint: Use open() to open the file
  file_handle = open(complete_file_path, "rb")
  # Hint: Use read() to read the contents of the file as bytes
  contents = file_handle.read()
  # Hint: Use hashlib.md5() to get the hash of the file
  hash_of_file = hashlib.md5(contents).hexdigest()
  # Hint: Use hexdigest() to get the hex representation of the hash
  file_handle.close()

  return hash_of_file


def main(hash, search_path):
  """Search for files in search_path that match hash"""
  # Hint: Use os.listdir() to get a list of files in search_path
  file_list = os.listdir(search_path)
  # Hint: Use a for loop to iterate over the files
  for file_name in file_list:
    # Hint: Use os.path.join() to join the search_path and the file name
    full_file_path = os.path.join(search_path, file_name)
    # Hint: Use file_hash() to get the hash of the file
    compare_hash = file_hash(full_file_path)
    # Hint: Use an if statement to check if the hash matches
    if compare_hash == hash:
      return file_name
  # Hint: If no file matches, return "NO MATCH FOUND"
  return "NO MATCH FOUND"


# Do not edit below this line
if __name__ == "__main__":
  result = main(sys.argv[1], sys.argv[2])
  print(result)

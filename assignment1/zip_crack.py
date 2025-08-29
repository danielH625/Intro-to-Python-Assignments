#!/usr/bin/env python3
import pathlib
import subprocess
import sys
from os import path


def attempt_password(path_to_zip_file, password_attempt):
  """Given a path to a zip file and a password attempt, return True if the password attempt is correct, False otherwise"""
  zip_path = pathlib.Path(path_to_zip_file)
  if not zip_path.exists():
    return False
  result = subprocess.run(["unzip", "-P", password_attempt, path_to_zip_file],
                          capture_output=True,
                          input=b"y\n")
  if result.returncode == 0:
    return True
  return False


def main(path_to_zip_file):
  first_phone_num = '1800555'

  for i in range(10000):
    password = f"{i:04}"
    full_password = first_phone_num + password

    pass_crack = attempt_password(path_to_zip_file, full_password)

    if pass_crack == True:
      return full_password
    elif pass_crack == False and i == 9999:
      return "PASSWORD NOT FOUND"
    else:
      continue


# Do not edit below this line
if __name__ == "__main__":
  zip_path = sys.argv[1]
  result = main(zip_path)
  print(result)

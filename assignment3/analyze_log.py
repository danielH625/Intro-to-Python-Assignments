#!/usr/bin/env python3
import os
import sys


def get_ip_from_line(line):
  """Given a single line of a log file, return the IP address"""
  # The input line will contain a line from a log file.
  # The line will be a string.
  string_line = str(line)
  # Every IP address will start with the octet "10." or "192."
  if "10." or "192." in string_line:
    # The IP address may be followed by a colon and a port number
    if "10." in string_line:
      start_index = string_line.find("10.")
    else:
      start_index = string_line.find("192.")
    end_index = string_line.find(":")
    ip_address = string_line[start_index:end_index]
  # If there is no IP address in the line, return an empty string
  else:
    return ''
  # You must find and return the IP address as a string
  return ip_address


def log_to_dict(path_to_log_file):
  """Given a path to a log file, return a dictionary of IP addresses and the number of times they IP was on a line that contained "LOGIN FAILED". """
  counter_dict = {}
  # Hint: Use open() to open the file
  file_handle = open(path_to_log_file, "rt")
  # Hint: Read the contents of the file using the readlines() function
  all_lines = file_handle.readlines()
  file_handle.close()
  # Hint: Use a for loop to iterate over the lines in the file
  for line in all_lines:
    # Hint: If the log file does not contain "LOGIN FAILED" then do not process the line any further
    if "LOGIN FAILED" in line:
      # Hint: Use get_ip_from_line() to get the IP address from the line
      ip_address = get_ip_from_line(line)
      if "10." or "192." in ip_address:
        # Hint: Use a dictionary to count the number of times each IP address appears
        if ip_address in counter_dict:
          counter_dict[ip_address] += 1
        else:
          counter_dict[ip_address] = 1
  # Hint: For example, after you have seen "10.1.1.1" twice and "192.168.1.1" once it might look like this:
  # {"10.1.1.1":2, "192.168.1.1":1}
      else:
        pass
    else:
      pass
  return counter_dict


def main(path_to_log_file, threshold):
  """Open the log file and analyze the log"""
  # Hint: Confirm that the log file in path_to_log_file exists
  path_exists = os.path.exists(path_to_log_file)
  if path_exists == True:
    # Hint: Call log_to_dict() to get a dictionary of IP addresses and the number of times they appear in the log file
    ip_dict = log_to_dict(path_to_log_file)
    # Hint: Process the dictionary to find the IP address that appears the most times
    targeted_ips = []
    for each_key, each_value in ip_dict.items():
      if each_value >= threshold:
        targeted_ips.append(each_key)
    if len(targeted_ips) == 0:
      return "NO IP FOUND"
  # Hint: If no IP address appears more than once, return "NO IP FOUND"
  else:
    return "FILE NOT FOUND"
    # Hint: Return a sorted list of all IP addresses that appears threshold or more times in the log
  return sorted(targeted_ips)


# Do not edit below this line
if __name__ == "__main__":
  file_path = sys.argv[1]
  threshold = int(sys.argv[2])
  result = main(file_path, threshold)
  print(f"The following IP Addresses were found more than {threshold} time.")
  if result == "NO IP FOUND":
    print(result)
  else:
    for each_ip in result:
      print(each_ip)

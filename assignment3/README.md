# Assignment 3 - Log Analyzer

## Situation Brief

After analyzing the same log file every day looking for signs of attackers you realize the truth, that manually analyzing log files is time consuming and are less accurate then that writing a tool to do it manually. To that end you are writing a tool to analyze the authentication logs of a server that is running on your internal network. 

## Tool Requirements

You must develop a tool called "analyze_log.py". It will take the following two command line arguments:

 - PATH: The first command line argument is the path to the log file you are going to analyze.
 - THRESHOLD: The second command line argument is an integer. 


If an IP Address appear on a line in the log in argument PATH along with the string "LOGIN FAILED" then you will count count it.  Any IP Address that appears in the log file more than the integer THRESHOLD you will print.


## Implementation Details

You must develop each of the following functions.  Your code will be tested by calling these individual functions by name.

### Function 1 - get_ip_from_line

This function will have following function definition:

```def get_ip_from_line(line):```

The function `get_ip_from_line` is designed to extract the IP address from a single line of a log file. It takes a string, `line`, as input and aims to identify and return the IP address present in that line. If no IP address is present it returns an empty string.

To accomplish this task using only the "in" operator, ".find()" or ".index()" and string slicing, you can follow a step-by-step approach:

For the given line, check if it contains an IP address that starts with either "10." or "192." by using the "in" operator. If the line does not contain such an IP address return an empty string.

You can use the location of the string "10." or "192." as the beginning of the IP Address.
You can use the location of the ":" between the IP Address and port number to identify the location of the end of the IP Address.

Slice the IP Address using the beginning and the end identified as described above.

The line "LOGIN FAILED 192.168.1.1:5000" should return "192.168.1.1"  
The line "10/01/2000 08:10:12.12345 HOST LOGIN FAILED FROM 192.168.1.1:12355"  should return "192.168.1.1"


### Function 2 - log_to_dict

This function will have the following definition:

```def log_to_dict(path_to_log_file):```


The function `log_to_dict()` will read the specified log file and return a dictionary containing counts of IP Addresses with failed logins.

This function will open the specified file and process it line by line. If a line does not contain "LOGIN FAILED" then the line is ignored. If a line does contain "LOGIN FAILED" then it should be passed the line to `get_ip_from_line()` to extract the IP Address. If the function returns an empty string value it can be ignored. However, if it returns an IP Address then it should update (or create) a count in a dictionary.

The format of the dictionary returned by this function should be as follows:

{ "IP ADDRESS 1" : occurrences of ip address 1, "IP ADDRESS 2": occurrences of ip address 2}

It should have one entry for every IP Address in the log that appears on a line containing LOGIN FAILED.  The value should be now many entries in the log contain that IP Address.   For example a file containing:

"LOGIN FAILED 10.1.1.1:12345
LOGIN FAILED 10.1.1.1:12346
LOGIN FAILED 192.168.1.1:1234"

Would return a dictionary containing:  {"10.1.1.1":2, "192.168.1.1":1}

### Function 3 - main

This function will have the following definition:

```def main(path_to_log_file, threshold):```

This function confirms that the file "path_to_log_file" exists if it doesn't it returns the string "FILE NOT FOUND". If the file exists it is passed to `log_to_dict()`. It will then process the dictionary and build a list of any IP Addresses that have a count of "threshold" or more. Then it will sort that list of IP Addresses by simply passing it to `sorted()` and return the sorted list.


### Other Details:

The provided template "analyze_log.py" will contain the following code. You should not make any changes to the code.

```
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
```

## Testing your code

A folder called test_files is in this folder.  You can use it to test your program.  Here are some example runs and the results you should expect to get back. The "$" (dollar sign) in the example below represent a bash terminal prompt. If you are going to run these command from colab you would put an "!" (exclamation point) before the command you want to execute.

```
$ python /content/drive/MyDrive/assignment3/analyze_log.py /content/drive/MyDrive/assignment3/sample_log.txt 30
The following IP Addresses were found more than 30 time.
192.168.5.50


$ python /content/drive/MyDrive/assignment3/analyze_log.py /content/drive/MyDrive/assignment3/sample_log.txt 25
The following IP Addresses were found more than 25 time.
10.9.5.42
192.168.5.50

$ python /content/drive/MyDrive/assignment3/analyze_log.py /content/drive/MyDrive/assignment3/sample_log.txt 20
The following IP Addresses were found more than 20 time.
10.9.5.2
192.168.5.53
10.9.5.42
192.168.5.50
192.168.5.54

$ python /content/drive/MyDrive/assignment3/analyze_log.py /content/drive/MyDrive/assignment3/sample_log.txt 50
The following IP Addresses were found more than 50 time.
NO IP FOUND

```

Remember you can execute your program in colab by running ```!/usr/bin/python3 <path to script>```  You path to script will almost certainly begin with `/content/drive/MyDrive/` and will continue from there to point to the location of your script.


## Submitting your answer.

After you have confirmed your code is working properly you will submit your code to the server. To submit your code use the pywars client's .solution method and upload your code to the server.  The solution method accepts one argument.  That argument is the full path to your code. Your path may vary depending upon where you have saved your files, but if you saved it to the same file given to you as a template then the correct path would be:

```d.solution("content/drive/MyDrive/assignment3/analyze_log.py")```  

The server will analyze your code and provide feedback. Fix any error and resubmit your code until it scores your answer as "Correct!".

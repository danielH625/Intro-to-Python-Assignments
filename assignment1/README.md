# Assignment 1 - Zip Password Cracker


## Situation Brief

After your companies head sales person left his position you discover that he used password protected zip files to store all the company spreadsheets containing critical contacts information and account numbers. You have been told by one of his co-workers that his password was the digits of a phone number, but you don't know what phone number. It could be any digit valid phone number in the format 1800555xxxx where xxxx is any digit between 0 and 9. You have been asked to write a tool to determine the password.

## Tool Requirements

You must develop a tool called "zip_crack.py". It will take one argument which will be the complete path to a password protected zip file. To determine the correct password you can repeatedly execute the "unzip" command which is in the same directory as this file and pass password attempts. 

## Implementation Details

 A function to determine if a password is correct or not is provided to you. When you call the provided function you will pass the path to the zip file and a password guess. It will return True if the password successfully extracted the zip contents and False if it did not.

This is the function that is provided to you.

```attempt_password( path_to_zip_file, password_attempt )```

Here is an example of calling the function with the password "18005550001"

```attempt_password( "/content/drive/MyDrive/assignment3/test_zip.zip", "18005550001" )```

If that is the correct password it will return True, if not it will return False.

### Function Main

You must develop a function called main().  It definition is as follows:

```def main(path_to_zip_file):```

This function must build a string containing a possible password guess. It will call `attempt_password()` to see if the password is correct. If the password is correct it will return the password. If it is not correct then it will continue trying another password repeating the process until it has tried every possible password or found the correct one. If it tries every possible password and does not identify the password it must return "PASSWORD NOT FOUND".


### Other Details:

The provided template "zip_crack.py" will contain the following code. You should not make any changes to the code.

```
# Do not edit below this line
if __name__ == "__main__":
    zip_path = sys.argv[1]    
    result = main(zip_path)
    print(result)
```


## Testing your code

A folder called test_files is in this folder.  You can use it to test your program.  Here are some example runs and the results you should expect to get back. The "$" (dollar sign) in the example below represent a bash terminal prompt. If you are going to run these command from colab you would put an "!" (exclamation point) before the command you want to execute.

```
$ python3 /content/drive/MyDrive/assignment1/zip_crack ./to_student/sample_zip1.zip 
Cracking ./to_student/sample_zip1.zip...
18005550001
$ python3 /content/drive/MyDrive/assignment1/zip_crack ./to_student/sample_zip2.zip 
Cracking ./to_student/sample_zip2.zip...
18005550100


$ python3 /content/drive/MyDrive/assignment1/zip_crack ./to_student/sample_zip3.zip 
Cracking ./to_student/sample_zip3.zip...
18005559999

$ python3 /content/drive/MyDrive/assignment1/zip_crack ./to_student/sample_zip4.zip 
Cracking ./to_student/sample_zip4.zip...
PASSWORD NOT FOUND


```

Remember you can execute your program in colab by running ```!/usr/bin/python3 <path to script>```  You path to script will almost certainly begin with `/content/drive/MyDrive/` and will continue from there to point to the location of your script.


## Submitting your answer.

After you have confirmed your code is working properly you will submit your code to the server. To submit your code use the pywars client's .solution method and upload your code to the server.  The solution method accepts one argument.  That argument is the full path to your code. Your path may vary depending upon where you have saved your files, but if you saved it to the same file given to you as a template then the correct path would be:

```d.solution("content/drive/MyDrive/assignment1/zip_crack.py")```  

The server will analyze your code and provide feedback. Fix any error and resubmit your code until it scores your answer as "Correct!".

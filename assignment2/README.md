# Assignment 2 - Forensics Investigation

## Situation Brief

Your organization maintains highly valued intellectual property. Over the last few months company leaders have grown suspicious that someone is collecting and celling intellectual property to your competitors. You have been asked to write a tool to search drives and identify the presence of specific intellectual property.

## Tool Requirements

You must develop a tool called "hash_search.py". The file that will contain your code has already been created in this folder. The tool must accept exactly two command line arguments.

 - HASH: The first command line argument is an MD5 Hash of a file you want to search for.

 - PATH: The second command line argument is the directory you must search.


Your tool will read the command line arguments that are passed to it and stored in the variable sys.argv. The MD5sum will be in sys.argv[1].  It will be referred to as "HASH" in this document. The path to search will be in sys.argv[2] and will be referred to as "PATH" in this document. You must open every file in PATH and calculate its MD5 ".hexdigest()" on the contents of the file using the "hashlib" module. The .hexdigest() method returns a string you will compare that to the HASH in the first command line argument. When you find whose calculated MD5 hexdigest that matches the HASH from the command line you will print the name of the file.

## Implementation Details

### Function 1 - file_hash
Your program must have a function named "file_hash".  Here is a definition statement for it.

```def file_hash(complete_file_path):```

This function must first check to see if the specified file exists.  If it does not exist the function must return the string "FILE NOT FOUND". If the file does exist it will open the file, and read its contents as bytes(). Do not read the files as text. It will then calculate its MD5 hexdigest() and return that value.  For example:

Here is an example of calling it and passing it paths to files that exist.

```file_hash("/etc/passwd")```  Returns a hex digest such as ```452304487baa4448a5e01a003bc67c52```
```file_hash("file_in_current_dir.txt")```  Returns a hex digest such as ```0202d1417d51f728e4695548fe420d38```

Here is an example of calling it and passing it a path to a file that does not exist:

```file_hash("/path/to/non-existent-file")``` return the string ```FILE NOT FOUND```


### function 2 - main

Your program must have a function named "main".  Here is a definition statement for it.

```def main(target_hash, search_path):```

This function will open every file that is stored in search_path. The search_path will be a complete absolute path to a directory. You will not search in any subdirectories. Instead use `os.listdir()` to retrieve a list of all of the files in that directory. Use a for loop to go through every file in that list of files. Combine the original search_path with individual file names using `os.path.join()`. Then pass the completed file path to the file_hash() function you have written above. If the hash returned by file_hash() matches the target_hash then it should return ONLY the file name (not the complete path) of the file that matched. If none of the files in the search_path match the target_hash then it should return the string "NO MATCH FOUND". 

### Other details:

The provided hash_search.py template file will already contain the following lines of code:

```
if __name__ == "__main__":
    result = main(sys.argv[1], sys.argv[2])
    print(result)
```

They read the command line arguments passed to your program, call the main function and print the value returned from it. This will enable you to test your two functions with the files I am providing you to confirm they are functioning properly before submitting your answer. These lines of code should not be removed or altered. These lines are the only lines you are not permitted to change. You can import additional modules as needed. 


## Testing your code

A folder called test_files is in this folder.  You can use it to test your program.  Here are some example runs and the results you should expect to get back. The "$" (dollar sign) in the example below represent a bash terminal prompt. If you are going to run these command from colab you would put an "!" (exclamation point) before the command you want to execute.

```
$ python3 /content/drive/MyDrive/assignment2/hash_search.py 210ba7944eb8ac397e52f39ca01bf30c /content/drive/MyDrive/assignment2/test_files
file-4hjWlQB9hS

$ python3 /content/drive/MyDrive/assignment2/hash_search.py 115ccaabb485916436b8b7b8845f0ed3  ./content/drive/MyDrive/assignment2/test_files
file-gO61SH5VLf

$ python3 /content/drive/MyDrive/assignment2/hash_search.py 20db6066bc80fbda6b529ee818f92367  /content/drive/MyDrive/assignment2/test_files
file-iEZ5CFRKYh

$ python3 /content/drive/MyDrive/assignment2/hash_search.py 8cbb158f175f073e52f35709efca6ba2  /content/drive/MyDrive/assignment2/test_files
file-q1OmXr979k
```

Remember you can execute your program in colab by running ```!/usr/bin/python3 <path to script>```  You path to script will almost certainly begin with `/content/drive/MyDrive/` and will continue from there to point to the location of your script.


## Submitting your answer.

After you have confirmed your code is working properly you will submit your code to the server. To submit your code use the pywars client's .solution method and upload your code to the server.  The solution method accepts one argument.  That argument is the full path to your code. Your path may vary depending upon where you have saved your files, but if you saved it to the same file given to you as a template then the correct path would be:

```d.solution("content/drive/MyDrive/assignment2/hash_search.py")```  

The server will analyze your code and provide feedback. Fix any error and resubmit your code until it scores your answer as "Correct!".

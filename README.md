### pygrep
A python program intended to work exactly like the grep linux command, or at least like the basic functionality of it.

## Functionality
This program is intended to find a string in a larger text. An example is finding something specific in a 1000 line long log file.

By default, the program takes input from a different program using a pipe `|`, and takes an argument for the string you are searching for. Example usage: `program-that-outputs-a-bunch-of-text | ./pygrep hello` 
The result will be every line with the string "hello" in the text to be printed on the screen.

Additionally, adding the `-t` argument, with a value of 3 for example, will print the next 3 lines after each occurance of the string. This is useful if you want to get more context around each found line.

Instead of taking input from standard input, and printing the result to the screen, pygrep can also read and write to files. `./pygrep -i input-file -o output-file hello` would take text from `input-file`, find every occurance of "hello", and then appends the result to `output-file`

When writing to a file, the program will create the file if it doesn't exist. If it does exist, it will append to the end of the file.

Other minor options are:
- `-C`: makes searching case sensitive.
- `-c`: disables color (automatically disabled when writing to a file).
- `-l`: prints line numbers before each resulting line.

## Error handling

I have tried my best to account for pretty much any error that can happen.

# Argument parsing

The program will ignore the error and keep running if: 
- The user inputs an unrecognized argument
- The user inputs unrecognized text when the search string is already specified.

The program will abort if:
- The user doesn't input a string to search for.
- The `-t` argument is used without a quantity of lines given, or an invalid quantity of lines is given (ie a value below 0, or a string instead of an int.)

# File related errors

The program will notify the user and abort if: 
- The input file / directory doesn't exist.
- The input file is not readable / permission issue.
- The output file destination directory doesn't exist.
- Whe output file isn't writable.
- Some other issue with output file, like an i/o error

## Why would you use this?

Grep is used commonly in linux environments, where something as basic as a text editor with a search function might be unavailable, or complicated to use (looking at you vim). This program allows you to quickly search through log files or command output to find if something happened or not. For example, you might want to know what graphics card is in a linux system, so you would run `lspci`, a command that lists all PCI devices in the machine, and then search for `VGA`, which is how a graphics card device is denoted. Using pygrep, you would do that like this: `lspci | pygrep VGA`. Another example is looking through the system log, to see if, for example, the wifi driver threw some errors.

Another reason to use this is that it can be inegrated into scripts. A search function within a text editor cannot be used in a diffrerent program, while grep can be run from within any script.
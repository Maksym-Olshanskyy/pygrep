## pygrep
A python program intended to work exactly like the grep linux command, or at least like the basic functionality of it.

# Functionality
This program is intended to find a string in a larger text. An example is finding something specific in a 1000 line long log file.

By default, the program takes input from a different program using a pipe `|`, and takes an argument for the string you are searching for. Example usage: `program-that-outputs-a-bunch-of-text | ./pygrep hello` The result will be every line with the string "hello" in the text to be printed on the screen.

Additionally, adding the `-t` argument, with a value of 3 for example, will print the next 3 lines after each occurance of the string.

Instead of taking input from standard input, and printing the result to the screen, pygrep can read and write to files. `./pygrep -i input-file -o output-file hello` would take text from `input-file`, find every occurance of `hello`, and then outputs the result to `output-file`

Other minor options are:
    `-C`: makes searching case sensitive.
    `-c`: disables color (automatically disabled when writing to a file).
    `-l`: prints line numbers before each resulting line.

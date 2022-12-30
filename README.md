# Console

## Summary

- Description
- How to use the program
- Credits

### Description

This program is an implementation of a "console" made with Python.
It contains some function to easily add a log system in your project.
With this program you are able to save and retrieve text line.

### How to use the program

The first thing to do is to create a "Console".
You can do that by initializing an instance of the "Console" class.

**Note:** You have to give a name to your console.
```python
import Console

my_console = Console.Console(name="MyCons")
```
This will result in the creation of 2 files in the same directory as the program :
- "MYCONS_session.txt"
- "MYCONS_always.txt"

The logs will be saved in those file.

**Note:** The "_always.txt" file keep all the logs since the creation of the console.
The goal of the "_session.txt" is to be cleared when needed then register the log of a session.
Even though the "_always" file can also be cleared following your needs.


Once you have created the console, you can start registering logs in it :
```python
my_console.log("This is my first log!")
```
This code will write the line "This is my first log!" in both file.


Now that you have registered log, you may want to retrieve them. You can do that this way:
```python
my_console.get_log("session", number_of_line=5)
```
This will return a list of the 5 lasts line of the "_session.txt" file.
The `get_log(cache, number_of_line)` function takes 3 different values for `cache` (string):
- `"session"`: Retrieve the log of the "_session.txt" file.
- `"always"`: Retrieve the log of the "_always.txt" file.
- `"both"`: Retrieve the log of both file.

The `number_of_line` (positive integer) argument correspond to the number of line that you want to retrieve from your logs file.
It can also take the value `"all"` to retrieve all the log file at once.

**Note:** If you choose the `"both"` option, the function will return a list of 2 lists,
the first one corresponding to the "_session.txt" and the second to "_always.txt".

The program also contains function to clear a log file :
```python
my_console.clear_log("session")
```
The `clear_log(cache)` function can take 3 different values for `cache` (string):
- `"session"`: Clear the log of the "_session.txt" file.
- `"always"`: Clear the log of the "_always.txt" file.
- `"both"`: Clear the log of both file.


### Credits

This program has been made by the following person/ group :
- GabHas : [GitHub](https://github.com/TheRealGabHas/) - [Website](https://gabhas.fr/)
- Photon Creation : [GitHub](https://github.com/Photon-Creation/)
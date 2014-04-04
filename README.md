##pyInteractiveTesting

When testing a Python script that requires user input from the command-line:
```python
name = input("Enter your name: ")
```
it is a pain manually typing those commands in all the time. So why not automate it? 

Why not send the console output to a file to view later? Why not execute the script multiple times with a set of given outputs? Why not take a group of scripts and run all of them with these inputs and have all of the outputs be sent to the output file?

The test script also includes built in method to call functions with arguments in automation multiple times as well.

###Install:  
```
git clone git@github.com:levibostian/pyInteractiveTesting.git
cd pyInteractiveTesting
mkdir assignments
```

###Execute:
To execute this program, you will need to configure these steps:  
* Put all Python scripts you want to exeucte into the ```assignments/``` directory.  
* Edit the input.txt file. On each line, type the text to send to a given input statement. For each separate group of inputs, enter an empty line. 
Example contents of input.txt:  
```
# tester input.txt
# lines beginning with # are comments.
# Enter one value per line per input() statement to send to script.
# Separate sets of input statements with a blank line.
# function calls are in format => :funcName(arg1, arg2) and must be separated by new lines.
5
try this text!
65.7

now try this set of inputs
000
-1

:fibonacci(100)
```
The above file will run each Python script in the ```assignments/``` directory three times. Once with inputs: 5, "try this text!", and 65.7. The second time with the inputs: "now try this et of inputs", 000, -1. And the third time it will call the function, fibonacci with argument 100.

* Now, simply run the script!  
```
python3 grader.py
```
Once execution is complete, the program will generate ```output.txt``` containing the command-line output a user would have seen if they ran the program manually. 

###Notes:
pyInteractiveTesting only works on Linux machines as it depends on the pexpect Python library.

If the output file ends up having infinite loops inside of it, opening up the output file may be very slow. To help conquer this issue, use the removeInfiniteLoops.py utility file:
```python
python3 removeInfiniteLoops.py
```
The program will prompt for the text to search for in the output.txt file that is the infinite loop text. output.txt will be edited to fix the infinite loop issue.

Lastly, this code is pretty hacky so be warned. It was meant to be a quick and dirty tester so it was created quick and dirty.

###License:

    The MIT License (MIT)
    
    Copyright (c) 2014 Levi Bostian
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.


PEXPECT LICENSE

    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt

    Copyright (c) 2012, Noah Spurrier <noah@noah.org>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
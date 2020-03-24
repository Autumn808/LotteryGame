# LotteryGame
This is a Python program that produces 3 or 4 pick random lottery numbers on a sentinel loop by until the user quits the program. 
Week 2 Deliverables

Overview: In this week, you have studied additional Python language syntax including selection statements, control statements and functions The Lab for this week demonstrates your knowledge of this additional Python functionality.

Be sure to develop and test your Python code in the AWS Cloud9 IDE provided for the class. Also, only use the functionality and Python concepts covered so far in the readings and examples. For example, we have not covered arrays, file I/O, sequences or sets. The good news is since you have been programming for a few semesters now, learning Python will go quick and we will be developing advanced code fairly quickly.

You should continue to use the PEP Python Style guide mentioned in the book and found here:

https://www.python.org/dev/peps/pep-0008/

Some examples of Python Coding Style best practices include:







Limit all lines to a maximum of 79 characters.

Imports are always put at the top of the file, just after any module comments and before module globals and constants.

Use 4 spaces for indentation.

Submission requirements for this project include 3 files. (Zipping them into one file is acceptable and encouraged):







Python Pick-3, Pick-4 lottery Application Code

Python Math Function Data Generator Application Code

Word, Excel or PDF file containing your test and plot results

Python Applications for Lab1: (total 100 points):

This lab consists of two parts.

The first exercise (40 points) allows the user to use a menu to select and then generate pick-3 or pick-4 lottery number generator. Once the user makes their choice, the lottery number will be generated and displayed for the user to see. The allowed number for each digit are 0 – 9. You should generate each digit and then concatenate the digits to form the 3 or 4-pick resultant number.

The application should continue to run until the user indicates they don’t want to generate any additional lottery numbers. A sample run might look like this.

**** Welcome to the Pick-3, Pick-4 lottery number generator *********

Select from the following menu:

1. Generate 3-Digit Lottery number

2. Generate 4-Digit Lottery number

3. Exit the Application

1 1

You selected 1. The following 3-digit lottery number was generated:

035

Select from the following menu:

1. Generate 3-Digit Lottery number

2. Generate 4-Digit Lottery number

3. Exit the Application

2

You selected 2. The following 4-digit lottery number was generated:

1489

Select from the following menu:

1. Generate 3-Digit Lottery number

2. Generate 4-Digit Lottery number

3. Exit the Application

3

You selected 3.

Thanks for trying the Lottery Application.

*********************************************************

Hints:

1. Use Sentinel while loop

2. How can you verify that each digit has the full-range of values 0-9

3. Create and use functions as often as possible

4. Use comments to document your code

The second exercise (40 points) produces x,y values using Python math functions. The results of these function calls will be used as input to another program of your choice for plotting the results. The plots can be made using Excel, Octave, or any other online or other graphing tool you have available.

The Math functions and values range of x-values are described below:

a. Generate x, sin(x) for x values ranging from -2PI -> 2PI with an increment of PI/64

b. Generate x, cos(x) for x values ranging from -2PI -> 2PI with an increment of PI/64

c. Generate x, sqrt(x) for x values ranging from 0 -> 200 with an increment of 0.5

d. Generate x, log10(x) for x values ranging from 0 -> 200 with an increment of 0.5

Since we aren’t using Python File I/O yet, you will need to use standard I/O and perhaps even copy and paste the output of the Python application to your graphing tool. Be sure both x and f(x) values are provided as input to the tool.

2 For graphing, provide the following graphs:

a. One graph with both x, sin(x) and x, cos(x) displayed. Be sure to include, a title, legends and x and y axis labels.

b. One graph with both x, sqrt(x) and x, log10(x) displayed. Be sure to include a title, legends and x and y axis labels.

Hints:

1. Use the Python Math library

2. print() statements will allow you to display the, x, f(x) results

3. Create and use functions as often as possible

4. Use comments to document your code

3. Document your results for each application within the AWS Cloud9 classroom environment. Provide screen captures and descriptions for each test case you provide for your lottery generator. Provide at least 5 test cases. For the Math data generator, provide tables clearly showing the x, f(x) data points generated from your Python application. In addition, include your two graphs as described above. (20 points)

Any submissions that do not represent work originating from the student will be submitted to the Dean’s office and evaluated for possible academic integrity violations and sanctions.

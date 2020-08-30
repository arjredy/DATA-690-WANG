## Summary from the class:
- How to use Terminal, Jupyter notebook in notebooks.ai
- How to create a GitHub Repo
- How to create a markdown cell in GitHub Repository. 

## What kinds of categories come under "Data"?
- Tabular or spread-sheet 
- Multidimensional arrays (Matrices)
- Multiple tables of data interrelated by key columns
- Evenly or unevenly spaced time series.

## Essential Python Libraries:

### NumPy:
NumPy, short for Numerical Python, has long been a cornerstone of numerical computing in Python. It provides the data structures, algorithms, and library glue needed for most scientific applications involving numerical data in Python.

### Pandas:
Pandas provides high-level data structures and functions designed to make working with structured or tabular data fast, easy, and expressive. Since its emergence in 2010, it has helped enable Python to be a powerful and productive data analysis environment. The primary objects in pandas that will be used in this book are the DataFrame, a tabular, column-oriented data structure with both row and column labels, and the series, a one-dimensional labeled array object.

### Matplotlib:
matplotlib is the most popular Python library for producing plots and other twodimensional data visualizations. It is designed for creating plots suitable for publication. While there are other visualization libraries available to Python programmers, matplotlib is the most widely used and as such has generally good integration with the rest of the ecosystem. I think it is a safe choice as a default visualization tool.

### SciPy:
SciPy is a collection of packages addressing a number of different standard problem domains in scientific computing.

## Python Interpreter:
Python is an interpreted language. The Python interpreter runs a program by executing one statement at a time. The standard interactive Python interpreter can be invoked on the command line with the python command.

## Running the Jupyter Notebook:
One of the major components of the Jupyter project is the notebook, a type of interactive document for code, text (with or without markup), data visualizations, and other output. The Jupyter notebook interacts with kernels, which are implementations of the Jupyter interactive computing protocol in any number of programming languages.
Python’s Jupyter kernel uses the IPython system for its underlying behavior.

### Interrupting running code:
Pressing Ctrl-C while any code is running, whether a script through %run or a long running command, will cause a KeyboardInterrupt to be raised. This will cause nearly all Python programs to stop immediately except in certain unusual cases.

## Python Language Basics:

### Language Semantics:
The Python language design is distinguished by its emphasis on readability, simplicity, and explicitness. Some people go so far as to liken it to “executable pseudocode.”

### Indentation, not braces:
Python uses whitespace (tabs or spaces) to structure code instead of using braces as in many other languages like R, C++, Java, and Perl. Consider a for loop from a sorting
algorithm.

### Everything is an object:
An important characteristic of the Python language is the consistency of its object model. Every number, string, data structure, function, class, module, and so on exists
in the Python interpreter in its own “box,” which is referred to as a Python object.

### Comments:
Any text preceded by the hash mark (pound sign) # is ignored by the Python interpreter. This is often used to add comments to code.

### Duck typing:
Often you may not care about the type of an object but rather only whether it has certain methods or behavior. This is sometimes called “duck typing”

from tkinter import *
root = Tk()
root.geometry("1300x345")
scroll = Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
t = Text(root,yscrollcommand=scroll.set)
t.pack(fill=X,expand=True)
t.insert(END,'''
Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[29]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[30]

Python was created in the late 1980s, and first released in 1991, by Guido van Rossum as a successor to the ABC programming language. Python 2.0, released in 2000, introduced new features, such as list comprehensions, and a garbage collection system with reference counting, and was discontinued with version 2.7 in 2020.[31] Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3. With Python 2's end-of-life (and pip having dropped support in 2021[32]), only Python 3.6.x[33] and later are supported, with older versions still supporting e.g. Windows 7 (and old installers not restricted to 64-bit Windows).
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
gfgfgfgdfgfgdfgffgg
Python interpreters are supported for mainstream operating systems and available for a few more (and in the past supported many more). A global community of programmers develops and maintains CPython, a free and open-source[34] reference implementation. A non-profit organization, the Python Software Foundation, manages and directs resources for Python and CPython development
''')
scroll.config(command=t.yview)




root.mainloop()
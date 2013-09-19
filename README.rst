pyperclip
=========

This is a cross-platform clipboard module for Python

I got tired of not having a good cross-platform module for accessing the clipboard in Python, so I put this together. It is a module that loads ``copy()`` and ``paste()`` functions depending on what your operating system (or window manager) is.

It has the following requirements:

* The Python ``which`` module (for finding commands on the path)
* ''Windows'' - No additional requirements. You don’t need the ``win32`` module installed; this uses ``ctypes`` to load built-in Windows DLLs.
* ''Mac'' - Requires the ``pbcopy`` and ``pbpaste`` commands, which come with OS X.
* ''Linux'' - Requires the ``xclip`` command, which possibly comes with the OS. If not, run ``sudo apt-get install xclip``. Or have the ``gtk`` or ``PyQt4`` modules installed.
* Pyperclip runs on both Python 2 and Python 3.

Usage is simple::

   import pyperclip
   pyperclip.copy('The text to be copied to the clipboard.')
   spam = pyperclip.paste()


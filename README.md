# commonUtils

A collection of python libraries to help with user input, amongst other utilities.


# Importing information

Until this uploaded to PyPi, please see Python's [importing documentation](https://docs.python.org/3/reference/import.html), or search for "Python relative imports", when handling organising directories and libraries.

Library files can be imported as such:

```py
import commonUtils

TEXT = commonUtils.ft('text', 'bold')
```

Or:

```py
from commonUtils import TextFormatting

TEXT - TextFormatting.ft('text', 'bold')
```


# GetInput.py

Allows for prompts and explicit data type conversion.
Takes `text` and `mode` as arguments.

```py
import commonUtils as CU
from CU import GetInput

USER_INPUT = GetInput.gi(text = 'Prompting text?', mode = str)
print(USER_INPUT)
```
Returns a string of `USER_INPUT`.


# TextFormatting

Allows for quick text formatting into different colours for CLI applications.
Takes `text`, `formatType` and `printText` as arguments.

```py
import commonUtils as CU
from CU import TextFormatting

TextFormatting.ft(text = 'Sample text', formatType = 'bold', printText = True)
```

Prints & returns emboldened `Sample text`.

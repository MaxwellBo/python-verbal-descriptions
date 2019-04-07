# python-verbal-descriptions
🗣 A command line tool that can generate English verbal descriptions for Python source files or snippets.

## Usage

There are multiple ways you can use this project, firstly; as a command-line tool:

```
python-verbal -t file -s example.py
```

(alternatively)

```
python -m python_verbal_descriptions -h
```

and as a Python library:

```python
from python_verbal_descriptions import verbalise_code

verbalise_code('x = 3')
```


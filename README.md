# gitmodules
This project was developed to avoid problems with gitmodules importing in Python projects.

## Dependencies
This project has no any dependencies, it uses only <b>os</b> and <b>sys</b> standard libraries.

## Usage
Install this project via PyPi:

```
pip install gitmodules
```

Import this module to your project before importing git submodules

```python
import gitmodules
import my_git_submodule_1
import my_git_submodule_2
```

## Example
Here is an <a href=https://github.com/KuYaki/gitmodules_example_a>example</a> with a problem explanation in its readme.

## How does it work
Right while importing this module tries to find .gitmodules file in your project, 
parse it and append all the git submodules directories to the 'sys.path'. 
After what it recursively repeat this action for all the git submodules.

## Important notes
This module doesn't change current work directory, so that if some submodule 
was assumed to work with its root folder via current work directory it will fail.

You don't need to call any functions from the <b>gitmodules</b> to make it work and it may call
'Unused import statement' code violation. To avoid it, add next comment in front of this import:

```python
# noinspection PyUnresolvedReferences
import gitmodules
```

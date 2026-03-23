*This project has been created as part of the 42 curriculum by khhammou*

## Description

The concept we learn in this module is python virtual enviroments
if you install packages globally, everything shares the same python enviroment
but if you have for example 2 projects where each project needs a specific version of pandas for example
Global python cannot safely handle that
the solution is to use Virtual Environments
Example structure:
matrix_env/
    bin/
        python
        activate
    lib/
        python3.11/
            site-packages/
All packages installed inside it go to:
matrix_env/lib/python3.x/site-packages instead of the global location
Test if i am running inside a virtual environment or not by:

If you have a big project with many dependencies -> put them all in a requirements.txt file and run pip install -r requirements.txt

1_sys.prefix
Inside venv:
sys.prefix = /path/matrix_env
Outside venv:
sys.prefix = /usr

2_ sys.base_prefix
This always points to the global python installation
so detection logic is basically:
if sys.prefix != sys.base_prefix:
    you are inside a venv

Other info to display:
Current python executable from sys.executable
example path: /usr/bin/python3
or /home/user/matrix_env/bin/python

Package install path:
This is where pip install puts packages
you can find it using:
site.getsitepackages()
Example path: /usr/lib/python3.11/site-packages
or matrix_env/lib/python3.11/site-packages

Instructions to create a venv:
python3 -m venv matrix_env
source matrix_env/bin/activate

What is a dependency:
Any external library your program needs like pandas
Your program must check whether each dependency is installed 
instead of importing normally -> import pandas
use dynamic importing
importlib.import_module("pandas")
if the module exists then success else catch the exception and print install instructions
if missing:
Install with:
pip install -r requirements.txt
or
poetry install
inside requirements.txt, put each dependency on a line by itself example:
pandas
numpy
matplotlib

pyproject.toml: This is the poetry format
Example structure:
[tool.poetry]
name = "matrix-loader"
version = "0.1.0"

[tool.poetry.dependencies]
python = "^3.10"
pandas = "*"
numpy = "*"
matplotlib = "*"

poetry automatically creates its own virtual environment
Run program with:
poetry run python loading.py

Data Analysis part:
exmaple concept is to generate fake data like: matrix_signal_strength
then:
create array with numpy
put it into a pandas dataframe
plot it into matplotlib
save figure
matrix_analysis.png

Exercise 2:
oracle.py

Real applications must not hardcode secrets like
API_KEY = "123456" it is a serious security mistake
Instead they use enviromental variables

Example environment variable:
Linux:
    export API_KEY=abc123
python reads it using:
os.getenv("API_KEY")

.env file
During development its annoying to export variables manually
so developers use .env
Example:
MATRIX_MODE=development
DATABASE_URL=sqlite:///zion.db
API_KEY=matrix-secret
LOG_LEVEL=DEBUG
ZION_ENDPOINT=https://zion.net/api

python-dotenv
This library loads .env automatically
Concept: load_dotenv()
Then environment variables become available via:
os.getenv()

Priority order:
Real environment variables override everything
ex: API_KEY=real_key python oracle.py
.env values
default values in code

Security Rule:
.env must never be committed to git
so .gitignore must contain .env
Instead you provide:
.env.example
Example:
MATRIX_MODE=
DATABASE_URL=
API_KEY=
LOG_LEVEL=
ZION_ENDPOINT=
this shows users what variables exist without exposing secrets

Poetry:
dependency resolver
manages environments
uses pyproject.toml

Main ways to install python packages:
1_ pip install flake8
it downloads package from PyPI, and installs it into the current python environment
Where it installs depends on environment:
global python -> system site-packages
virtual env -> venv site-packages
user install -> ~/.local/lib/...

Variants:
specify version:
pip install flake8==6.1.0
upgrade package:
pip install --upgrade flake8

2_ pip install --user
pip install --user flake8
installs into user directory, not system python
~/.local/lib/python3.11/site-packages
avoids needing root privileges
Executables go into: ~/.local/bin
if directory isnt in PATH, commands like flake8 will not work directly

3_ installing inside a virtual environment
Example:
python3 -m venv venv
source venv/bin/activate
pip install flake8
now flake8 installed inside: venv/lib/python3.x/site-packages
and executable:
venv/bin/flake8

4_ using poetry
poetry install
What it does:
- Reads pyproject.toml
- Creates a virtual environment
- Installs all dependencies listed there
Example:
pyproject.toml has:
[tool.poetry.dependencies]
python = "^3.10"
pandas = "^2.0"
numpy = "^1.25"
then run poetry install
Run programs with poetry run python3 script.py

Executables placed in:
/usr/bin
/usr/local/bin
~/.local/bin
venv/bin

Your system has a PATH variable that tells the shell where to look
Example:
echo $PATH
if flake8 in installed in one of those directories -> command works directly

if package installed in ~/.local/bin/flake8
but ~/.local/bin is not in PATH
flake8 will fail,
But python3 -m flake8 works because Python runs the module directly
python3 -m means run a module as a script
python internally does something similar to:
import flake8
flake8.__main__()
it executes the package's __main__.py

Real world workflow:
poetry new project
cd project
poetry add pandas numpy matplotlib
poetry install
poetry run python script.py

using python3 -m pip install package 
instead of
pip install package
is better since it guarantees pip corresponds to the same python interpreter
Example problem:
python -> python 3.11
pip -> python 3.9
using python3 -m pip prevents this mismatch

Getting in and out of a virtual environment:
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 construct.py
deactivate

matrix_env/
 ├── bin/
 │    ├── python
 │    ├── pip
 │    └── activate
 │
 ├── lib/
 │    └── python3.11/
 │         └── site-packages/
 │
 └── pyvenv.cfg
-m means run a module as a script so we need python3 -m venv matrix_env
venv is a module 

for ex1
python3 loading.py should show missing dependencies and installation instructions
then go inside a venv to run pip install -r requirements.txt
python3 -m venv env
source \env\bin\activate
pip install -r requirements.txt
to exit the env, deactivate
or
poetry install --no-root # for the errors
poetry run python loading.py

ex2
enter a virtua environment then do this
pip install python-dotenv

### Instructions

You run this code by doing python3 file_name.py

## Resources

The internet

## AI Usage

Testing my code with test cases and helping me find syntax errors# python-module-8

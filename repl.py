import os
from colorama import *
import sys
user_home = os.path.expanduser("~")
if os.path.isfile(f"{user_home}/.pythonrepl_code"):
  print(f"Error: Existing repl. Delete {user_home}/.pythonrepl_code to continue.")
  exit(1)
print("Creating an empty REPL file...")
with open(f"{user_home}/.pythonrepl_code", "w") as code:
  code.write("")
imports = []
print(f"""Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.patch} [PyREPL ({pyrepl_version})] on {sys.platform}
Type "help", "copyright", "credits" or "license" for more information.""")
try:
  # Function to add module to REPL code.
  def add_module(module):
        imports.append(module)
        print(f"Added {module}. Actual Python importing won't work; this breaks the module.")
  while True:
        repl = input(">>> ")
        if repl.startswith("import "):
           add_module(repl.replace("import ","",1))
        os.unlink(f"{user_home}/.pythonrepl_code")
        for i in imports:
          with open(f"{user_home}/.pythonrepl_code", "a") as code:
            code.write(f"import {i} # Import {i}\n")
        with open(f"{user_home}/.pythonrepl_code", "a") as code:
          code.write("\n" + repl)
        os.unlink(f"{user_home}/.pythonrepl_code")
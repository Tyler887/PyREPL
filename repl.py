import os
from colorama import *
import sys
pyrepl_version = "dev"
user_home = os.path.expanduser("~")
if os.path.isfile(f"{user_home}/.pythonrepl_code"):
  os.unlink(f"{user_home}/.pythonrepl_code")
with open(f"{user_home}/.pythonrepl_code", "w") as code:
  code.write("")
imports = []
print(f"""Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} [PyREPL ({pyrepl_version})] on {sys.platform}
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
        dead_end = False
        if repl.endswith(":"):
          while not dead_end:
            addtorepl = input("         ")
            if addtorepl != "":
              repl = repl + "\n" + addtorepl
              addtorepl = ""
            else:
              dead_end = True
        os.system(f"python{sys.version_info.major} {user_home}/.pythonrepl_code")
        os.unlink(f"{user_home}/.pythonrepl_code")
        with open(f"{user_home}/.pythonrepl_code", "w") as code:
              code.write("")
        repl = ""
        dead_end = False
except KeyboardInterrupt:
  print("\nKeyboardInterrupt")

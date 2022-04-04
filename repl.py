import os
from colorama import *
import sys
import importlib
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
      if importlib.util.find_spec(module) is None:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} {module} does not exist.")
      else:
        imports.append(module)
  while True:
        repl = input(">>> ")
        if repl.startswith("import "):
           add_module(repl.replace("import ","",1))
        os.unlink(f"{user_home}/.pythonrepl_code")
        for i in imports:
          with open(f"{user_home}/.pythonrepl_code", "a") as code:
            code.write(f"import {i} # Import {i}\n")
        dead_end = False
        if repl.endswith(":"):
          while not dead_end:
            addtorepl = input("    ")
            if addtorepl != "":
              repl = f"""{repl}
{addtorepl}"""
              addtorepl = ""
            else:
              dead_end = True
        with open(f"{user_home}/.pythonrepl_code", "a") as code:
          code.write("\n" + repl)
        os.system(f"python{sys.version_info.major} {user_home}/.pythonrepl_code")
        os.unlink(f"{user_home}/.pythonrepl_code")
        with open(f"{user_home}/.pythonrepl_code", "w") as code:
              code.write("")
        repl = ""
        dead_end = False
except KeyboardInterrupt:
  print("\nKeyboardInterrupt")

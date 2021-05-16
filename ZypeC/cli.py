from ZypeC.compilers import compile
import sys
import os
import platform
from rich import print

def cli():
    if sys.argv[1] == '--version' or sys.argv[1] == '-v':
        print("[bold red]Zype[/bold red]: v1.2.0")
    else:
        compile()
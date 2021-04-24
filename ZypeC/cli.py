from ZypeC.compilers import compile
import sys, os, platform

def showVer():
    versionDetails = f'Zype v1.1 on {sys.platform} {platform.version()}'
    return versionDetails

def showHelp():
    helpDetails = f'{version()}\n\nHelp:\nUsage: zype (Command)\nCommands\n--------\n\nstart - Starts Compilation based on zype.config.json file.\nversion - Shows version info\nhelp - Shows this help message.'
    return helpDetails

def cli():
    start = compile()
    version = showVer()
    help = showHelp()
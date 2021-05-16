import markdown
import os
import json
import errno
import ZypeSDK as z
import sys


def compile():
    file = sys.argv[1]
    cType = sys.argv[2]
    to = sys.argv[3]
    if cType == 'md' and to == 'html':
        if os.path.isfile(file):
            with open(file, 'r') as md:
                text = md.read()
                html = markdown.markdown(text)
                html = f"""<!DOCTYPE html>
    <html>
    <head>
    <title>ZypeC Generated HTML</title>

        <meta charset="utf-8" />
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link href="https://raw.githubusercontent.com/Zype-Z/ZypeC/main/assets/favicon.png" rel="icon">
    </head>

    <body>
    {html}
    </body>
    </html>"""
                hfile = file.replace('.md', '.html')
                with open(f'{hfile}', 'w') as fh:
                    fh.write(html)
        else:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), file)
    elif cType == 'zype' and to == 'json':
        ZypeFile = z.Open(file)
        JSONFile = file.replace('.zype', '.json')
        with open(f'{JSONFile}', 'w') as JSON:
            JSON.write(ZypeFile)
    else:
        raise ValueError(f"Zype: {cType} is not supported")

if __name__ == "__main__":
    print("Can't be used without CLI.")

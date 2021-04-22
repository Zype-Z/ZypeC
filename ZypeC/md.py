import markdown
import os
import json
import errno
from glob import glob

def compile():
    if os.path.isfile('zype.config.json'):
        with open('zype.config.json', 'r') as zype:
            data = json.load(zype)
            compiler = data['compiler']
            if os.path.isfile(compiler):
                with open(compiler, 'r') as compiler:
                    compiler = json.load(compiler)
                    file = compiler['file']
                    Content_Type = compiler['Content-Type']
                    toFile = compiler['to']
                    if Content_Type == 'text/markdown':
                        if toFile == 'html':
                            if os.path.isfile(file):
                                with open(file, 'r') as md:
                                    text = md.read()
                                    html = markdown.markdown(text)
                                    html = f"""<!doctype html>
<html>
<head>
<title>Zype Generated HTML</title>

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
                                    return fh.write(html)
                            else:
                                raise FileNotFoundError(
                                        errno.ENOENT, os.strerror(errno.ENOENT), file)
                        else:
                            raise ValueError(
                                    f"Zype: Can't Compile {file} to {file.replace('.md', '.'+toFile)}")
                    else:
                        raise ValueError(
                                f"Zype: {Content_Type} is not supported")
            else:
                raise FileNotFoundError(
                        errno.ENOENT, os.strerror(errno.ENOENT), compiler)
    else:
        raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), 'Zype.json')
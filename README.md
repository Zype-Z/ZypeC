<p align='center'>
    <img src='https://raw.githubusercontent.com/TechGeeks-Dev/tgcc/main/assets/favicon.png'>
</p>
# ZypeC
[![Generic badge](https://img.shields.io/badge/PyPI-v1.0-GREEN.svg)](https://shields.io/)&nbsp;[![PyPI Release Create](https://github.com/Zype-Z/ZypeC/actions/workflows/Create-Release.yaml/badge.svg)](https://github.com/Zype-Z/ZypeC/actions/workflows/Create-Release.yaml)&nbsp;[![CodeQL](https://github.com/Zype-Z/ZypeC/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Zype-Z/ZypeC/actions/workflows/codeql-analysis.yml)<br>

## Installation

```shell
pip install ZypeC
```

## Usage

First create a `zype.config.json` file with a **`compiler`** key:
```json
{
    "compiler": "compiler.json"
}
```
You can replace `compiler.json` with anything else and create that file with the value of:

```json
{
    "file": "file.md",
    "Content-Type": "text/markdown",
    "to": "html"
}
```

Then run:
```shell
zype start
```

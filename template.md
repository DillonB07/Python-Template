# Editing and Customizing Your Package

## Intro
This template will give general information on how to build and publish your package. I am creating this tutorial on [repl.it](https://repl.it), but other Python editors work. This was built with Python 3.8, though 

## Files
Make sure to check that your files include the following:

```
python-package-template
├── console.sh
├── setup.py
├── README.md
├── LICENSE
├── pypackage
│   ├── __init__.py
│   └── module_a.py
├── tests
│   └── sample_test.py
└── cmd
    ├── build.sh
    ├── pip.sh
    └── rm.sh
```

You can download these files by:
- [Downloading the latest release](https://github.com/BD103/python-package-template/releases)
- [Cloning the repo on Github](https://github.com/BD103/python-package-template/generate) (Might be unstable)
- [Forking on Replit](https://repl.it/github/BD103/python-package-template)

## How [PyPI](https://pypi.org) Works

> If you already know this, then you can skip this section. I do recommend reading it though! It's quite helpful.

Before you can start creating a package, you need to know how PyPI works.
Pronounced Py-P-I, PyPI is an online package database. It allows you to upload your own packages, as well as download others. You can download these packages from the [actual website](https://pypi.org), or you can use PIP.
PIP is a package that is also [conveniently on PyPI](https://pypi.org/project/pip/), though you don't need to download this. It is automatically bundled with Python. [You can find a list of these built-in packages here.](https://docs.python.org/3/library/) To download a package, first make sure you checkmarked _Add Python 3.* to PATH_ when installing Python. Next, open command prompt. **This is not IDLE!** There, type `pip install package`, replacing `package` with the name. You can also find commands like this on the website.
This command downloads the wheel file of the package, and puts it in a special folder. If you don't know what a wheel file is, look at the following image.

![How Python Compresses Packages](https://packaging.python.org/_images/py_pkg_tools_and_libs.png)

> You can find more on this on [packaging.python.org](https://packaging.python.org/overview/#python-binary-distributions).

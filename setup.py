from setuptools import setup

APP=['loancalculator.py']
OPTIONS = {
    'iconfile':'loanIcon.png', 'argv_emulation' : True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)

# Terminal command: python3 setup.py py2app -A (for alias, i.e. runs only on my mac)
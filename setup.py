import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="psgfiglet",
    version="1.21.0",
    author="PySimpleGUI",
    author_email="mike@PySimpleGUI.org",
    description="Create Figlets using a PySimpleGUI GUI and pyfiglet. A PySimpleGUI Demo Program.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/PySimpleGUI/psgfiglet",
    packages=['psgfiglet'],
    install_requires=['PySimpleGUI', 'pyfiglet'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Topic :: Multimedia :: Graphics",
        "Operating System :: OS Independent"
    ],
    package_data={"":["*.ico"]},
    entry_points={
        'gui_scripts': [
            'psgfiglet=psgfiglet.psgfiglet:main'
        ],
    },
)

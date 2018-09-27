from setuptools import setup

setup(
    # ...,
    name='sysml',
    version='0.1.0',
    packages=['sysml'],
    author="Sean Marquez",
    author_email="capsulecorplab@gmail.com",
    description="A Python package for the Systems Modeling Language (SysML)",
    url="https://github.com/spacedecentral/SysML.py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    # ...,
)

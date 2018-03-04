import setuptools

setuptools.setup(
    name='python-verbal-descriptions',
    version='0.0.1',
    description='A command line tool that can generate English verbal descriptions for Python source files or snippets.',
    author='Maxwell Bo',
    url='https://github.com/MaxwellBo/python-verbal-descriptions',
    license='LICENSE.txt',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'python-verbal = python_verbal_descriptions.__main__:main'
        ]
    }
)

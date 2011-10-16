from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.markdown')).read()

version = '0.1'

install_requires = [
    # "PyQt4"
]

setup(name='qunittest',
    version=version,
    description="Unittest plugin which helps you to test asynchronous PyQt4 code.",
    long_description=README,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Software Development :: Testing"
    ],
    keywords='gui testing unit',
    author='Dawid Fatyga',
    author_email='dawid.fatyga@gmail.com',
    url='http://dejw.github.com/qunittest',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            []
    }
)

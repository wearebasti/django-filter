import os
import sys
from setuptools import setup, find_packages

f = open('README.rst')
readme = f.read()
f.close()

version = '1.0.2'

if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

setup(
    name='django-filter',
    version=version,
    description=('Django-filter is a reusable Django application for allowing'
                 ' users to filter querysets dynamically.'),
    long_description=readme,
    author='Alex Gaynor',
    author_email='alex.gaynor@gmail.com',
    maintainer='Carlton Gibson',
    maintainer_email='carlton.gibson@noumenal.es',
    url='https://github.com/carltongibson/django-filter/tree/master',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ],
    zip_safe=False,
)

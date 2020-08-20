from setuptools import setup, find_packages
from bootstrap4form.meta import VERSION

setup(
    name='django-bootstrap4-form',
    version=str(VERSION),
    description="django-bootstrap4-form",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords='bootstrap4,django',
    author='gwasser',
    author_email='garret@wassiverse.com',
    url='http://github.com/gwasser/django-bootstrap4-form',
    license='MIT',
    test_suite='runtests.runtests',
    install_requires = [
        "django>=2.2,<3",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

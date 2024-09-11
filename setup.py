import os
import sys

from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
elif sys.argv[-1] == "clean":
    import shutil

    if os.path.isdir("build"):
        shutil.rmtree("build")
    if os.path.isdir("dist"):
        shutil.rmtree("dist")
    if os.path.isdir("gmail_oauth_backend.egg-info"):
        shutil.rmtree("gmail_oauth_backend.egg-info")

setup(
    name='django-gmail-oauth-backend',
    version='0.1.7',
    description='Simplifies Gmail authentication for Django applications using OAuth 2.0. WITHOUT App Passwords!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yeongbin-jo/django-gmail-oauth-backend',
    author='Yeongbin Jo',
    author_email='iam.yeongbin.jo@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=5.0',
        'google-auth>=2.0',
        'google-api-python-client>=2.0',
        'google-auth-oauthlib>=1.2',
    ],
    python_requires='>=3.11'
)

from setuptools import setup


setup(
    name='curling',
    version='0.2.2',
    description='Slumber wrapper for Django that works well with Tastypie',
    long_description=open('README.rst').read(),
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    install_requires=['argparse', 'requests', 'PyJWT-mozilla',
                      'mock', 'slumber==0.5.3', 'Django', 'pygments',
                      'oauth2==1.5.211', 'httplib2'],
    packages=['curling'],
    url='https://github.com/andymckay/curling',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Framework :: Django'
    ],
    entry_points={
        'console_scripts': [
            'curling = curling.command:main'
        ]
    }
)

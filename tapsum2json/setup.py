from distutils.core import setup

setup(
    name='tapsum2json',
    version='0.0.1',
    packages=[''],
    entry_points={
        'console_scripts':[
            'tapsum2json=main:main'
        ]
    },
    url='',
    license='GNU GPL v3',
    author='Aleksandr Kantorez',
    author_email='no.money.no.honey5151@gmail.com',
    description='TAP summary to JSON'
)

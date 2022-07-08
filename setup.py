import setuptools
setuptools.setup(
    name='CSV2TSV',
    version='0.1',
    author='Robert Cook',
    description='',
    packages=['csv_2_tsv'],
    entry_points = '''
        [console_scripts]
        csv_2_tsv=csv_2_tsv.cli:csv_2_tsv
    ''',
    install_requires=[
        'setuptools',
        'pandas >= 1.4.3',
        'numpy >= 1.16.0'
    ],
    python_requires='>=3.5'
)
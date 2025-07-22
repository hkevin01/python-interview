from setuptools import find_packages, setup

setup(
    name='python-interview-assistant',
    version='0.1.0',
    description='PyQt GUI for Python interview preparation',
    author='hkevin01',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=['java_questions', 'cpp_questions', 'language_selector'],
    install_requires=[
        'pyqt5',
        'scikit-learn',
        'pytorch'
    ],
    entry_points={
        'console_scripts': [
            'python-interview=src.main:main'
        ]
    },
)

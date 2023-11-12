from setuptools import setup, find_packages

setup(
    name='math_quiz_game',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        
        # Add any other Python packages your project depends on
    ],
    entry_points={
        'console_scripts': [
            'math-quiz=math_quiz.quiz:math_quiz',
        ],
    },
)
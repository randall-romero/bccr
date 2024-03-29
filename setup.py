""" The bccr package setup.
Based on setuptools

Randall Romero-Aguilar, 2015-2022
"""

from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bccr',
    version='2022.06.29',
    description='Herramientas para descargar datos del Banco Central de Costa Rica',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Randall Romero-Aguilar',
    author_email='randall.romero@outlook.com',
    url='http://randall-romero.com/code/bccr',
    license='MIT',
    keywords='BCCR datos',
    packages=['bccr', 'demos', ],
    python_requires='>=3.7',
    install_requires=[
        'pandas',
        'numpy',
        'anytree',
        'requests',
        'beautifulsoup4',
        'plotly',
        'dash>=2.2.0',
        'dash-extensions==0.0.71',
        'jupyter-dash'],
    package_data={'bccr': ['data/indicadores.pkl', 'data/indicators.pkl', 'data/cuadros.pkl']},
    include_package_data=True
)




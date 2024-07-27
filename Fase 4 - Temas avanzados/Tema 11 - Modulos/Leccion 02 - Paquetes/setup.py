# Este fichero siempre debe llamarse setup
from setuptools import setup

setup(
    name='Mensajes',
    version='1.0.1',
    description='Un paquete para saludar y despedir',
    author='Juan David R O', 
    author_email='hola@email.com',
    url='https://davidolmos-portfolio.netlify.app/',
    packages=['mensajes','mensajes.bienvenida','mensajes.despedida'],
    scripts=['test.py']
)
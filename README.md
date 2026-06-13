Proyecto integrador de la materia "Fundamentos de programación" inpartida por el profesor Gandhi Hernandez en el Instituto Superior Tecnológico Inmaculada Concepción (ISTIC) 

Alumno: Gregory Rodriguez

Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Prerrequisitos 📋

1.- Instalar python desde la pagina oficial:

Descarga de python
2.- Verificar instalacion de python

  python --version
3.- Verificar la instalación del gestor de paquetes PIP

  pip --version
4.- Instalación de editor de codigo Visual Studio Code

Descarga de VSC
Instalación local
Abrir visual estudio code y abrir una terminal con Ctrl+Shift+ñ

hacer un clon del repositorio

  git clone https://github.com/kniball4726/Python.git
Desde el terminal entrar en la carpeta Python

  cd python
  
Estando dentro del proyecto desde terminal se debe correr el archivo pyproject.toml, el cual contiene las librerias utilizadas para el proyecto

  pip install poetry
  
Para verificar la instalacion 

  poetry --version
  
  Al verificar instalar con:

  poetry install 
  
Se deben instalar las dependencias utilizadas en el proyecto para que funciona de manera optima

    pyinstaller --onefile app.py
al correr este comando se crearan dos carpetas denominadas build y dist

dentro de la carpeta dist encontraremos un archivo llamado app.exe

este ejecutable de windows puede utilizarse directamente desde el escritorio de su pc otorgandole un acceso directo, se puede modificar el nombre y el icono

Forma de uso


Autor
Gregory Rodriguez - Trabajo inicial, Desarrollo y documentación

@kniball4726

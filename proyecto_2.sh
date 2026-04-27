#!/bin/bash

echo "Iniciando Pipeline: Arqueología Galáctica y el Misterio de Omega Centauri "

#1. Ejecutar la descarga de datos

bash 1_descarga_omega.sh

echo "Creando base de datos local y limpiando datos nulos"

python 2_crear_db.py

echo "Generando gráficas de movimiento propio y diagrama H-R"

python 3_analisis.py 

echo "Proceso completado con exito"
echo "Revisa los archivos: movimiento_propio.png y diagrama_hr_omega.png"

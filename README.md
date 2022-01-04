# py_ocr_poc
Prueba de concepto de OCR en python utilizando tesseract.

Para probarlo:
1. Crear los directorios input y output en el mismo directorio del docker-compose.yml.
1. Dejar en el directorio input el pdf del que se quiere extraer el texto
1. Levantar el contenedor ` docker-compose up -d`
1. Entrar al contenedor `docker exec -it ocr-py bash`
1. Ejecutar `python ./ocr_pdf.py --input-dir=/input --output-dir=/output`
1. Esperar a que se procese, el resultado quedará en un archivo de txt con igual nombre que el pdf dentro de un directorio con el nombre del pdf dentro del directorio output


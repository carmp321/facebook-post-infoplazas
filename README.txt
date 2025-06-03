INSTRUCCIONES PARA USAR LA APP

1. LOCALMENTE:
   - Instala dependencias:
       pip install -r requirements.txt
   - Ejecuta la app:
       python app.py
   - Abre el navegador en http://127.0.0.1:5000

2. PUBLICAR EN RENDER.COM:
   - Sube este proyecto a GitHub.
   - Ve a https://render.com y crea un nuevo "Web Service".
   - Selecciona:
       Runtime: Python 3
       Start Command: gunicorn app:app
   - Render instalará automáticamente las dependencias y servirá la app.

¡Listo!

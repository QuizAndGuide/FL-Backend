SCRIPTS:

- matchesround.py" ejecutable como "python3 manage.py matchesround" hace la peticion a la API de BESOCCER 
  y devuelve los partidos de la jornada en formato json, que es guardado como round.json, luego los mediante el RoundSerializer guarda todos los datos.

- matchesroundandnext.py ejecutable como "python3 manage.py matchesroundandnext" hace una peticion de la temporada en curso y la 
  siguiente y los procesa igual que matchesround.py sin guardar el archivo. ****   en proceso   ****



-el script clasificacion.py popula la db clasificacion definida por el modelo:

class Clasificacion(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.IntegerField()
    group_name = models.CharField(max_length=255,null=True,blank=True)
    conference = models.IntegerField()
    team = models.CharField(max_length=200)
    points = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    shield = models.URLField(null=True,blank=True)
    cflag = models.URLField(null=True,blank=True)
    basealias = models.CharField(max_length=255)
    gf = models.IntegerField(null=True,blank=True)
    ga = models.IntegerField(null=True,blank=True)
    avg = models.IntegerField()
    matchs_coef = models.CharField(max_length=255,null=True,blank=True)
    points_coef = models.CharField(max_length=255,null=True,blank=True)
    coef = models.CharField(max_length=255,null=True,blank=True)
    coefficients = models.CharField(max_length=255,null=True,blank=True)
    mark = models.CharField(max_length=255,null=True,blank=True)
    class_mark = models.CharField(max_length=255,null=True,blank=True)
    round = models.IntegerField()
    pos = models.IntegerField()
    countrycode = models.CharField(max_length=4)
    abbr = models.CharField(max_length=10)
    form = models.CharField(max_length=15)
    direction = models.CharField(max_length=200,blank=True)
    type_id = models.IntegerField(null=True,blank=True)
    type = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        return 'Casificación'
    class Meta:
        ordering = ['pos']

 que crea una tabla en la que una entrada es:

{
  "id": 2107,
  "group": 1,
  "group_name": null,
  "conference": 0,
  "team": "Real Madrid",
  "points": 25,
  "wins": 8,
  "draws": 1,
  "losses": 1,
  "shield": "https://t.resfu.com/img_data/escudos/medium/2107.jpg?size=120x&lossy=1&v=36",
  "cflag": "https://t.resfu.com/media/img/flags/st3/large/es.png?size=100x65c&lossy=1&v=36",
  "basealias": "real-madrid",
  "gf": 21,
  "ga": 7,
  "avg": 14,
  "matchs_coef": "",
  "points_coef": "",
  "coef": "",
  "coefficients": null,
  "mark": "1",
  "class_mark": "campeon",
  "round": 11,
  "pos": 1,
  "countrycode": "ES",
  "abbr": "RMA",
  "form": "lwwwd",
  "direction": "",
  "type_id": 4,
  "type": "Regular"
}
 
el problema que he notado es que actualiza la tabla y no guarda las clasificaciones de las jornadas anteriores,
se me ocurre hacer el campo round primary key y asi guardar las jornadas y no tener solamente la clasificacion actual, tambien hay que implementar en el scripts la peticion de las ligas menores. 
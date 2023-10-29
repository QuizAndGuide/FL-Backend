
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
 
lo que tengo que cambiar es que actualiza la tabla y no guarda las clasificaciones de las jornadas anteriores, el json que devuelve es:

table: list
    la lista tiene 20 diccionarios asi:
    {id: str
    group: str
    group_name: NoneType
    conference: str
    team: str
    points: str
    wins: int
    draws: int
    losses: int
    shield: str
    cflag: str
    basealias: str
    gf: str
    ga: str
    avg: int
    matchs_coef: str
    points_coef: str
    coef: str
    coefficients: NoneType
    mark: int
    class_mark: str
    round: str
    pos: str
    countrycode: str
    abbr: str
    form: str
    direction: str
    },
info: dict
    type: str
    type_id: str
legends: list
    group: str
    legend: list
        pos: int
        title: str
        class_color: str
    penalty: list

lo que estoy haciendo ahora en unir el diccionario info con cada elemento de la lista asi:


for n in json_data['table']:
    dict = n | json_data['info']




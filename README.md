
-el script clasificacion.py convierte hace request de la clasificacion, convierte el json a un diccionario, el json tiene un esquema:

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

despues para guardar los datos en una coleccion se crea un nuevo diccionario que por cada instancia de la lista 'tabla', al que se le suma el diccionario 'info' y luego se renombra el campo id de cada entrada por team_id, siendo id la que genera django por defecto, no es necesario especificarla en este caso, ya que no viene proporcionada por la API de besoccer, con esto se soluciona el problema de almacenamiento de jornadas diferentes.

otra opcion seria generar una tabla por cada jornada


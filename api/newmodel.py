from django.contrib import admin
from django.conf import settings
from djongo import models

class UserProfile(models.Model):
    MEMBERSHIP_FREE = 'F'
    MEMBERSHIP_PREMIUM = 'P'
    MEMBERSHIP_PREMIUMPLUS = 'P+'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_FREE 'Free')
        (MEMBERSHIP_PREMIUM 'Premium')
        (MEMBERSHIP_PREMIUMPLUS 'Premium+')
    ]
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=100 unique=True)
    coins = models.IntegerField(default=1000) 
    rating = models.IntegerField(default=1200)  
    country = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    membership = models.CharField(
        max_length=2 choices=MEMBERSHIP_CHOICES default=MEMBERSHIP_FREE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        permissions = [
            ('view_history', 'Can view history')
        ]


class Category(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    league_id = models.CharField(max_length=10)
    order = models.IntegerField()
    year = models.CharField(max_length=4)
    c_pending = models.CharField(max_length=4)
    alias = models.CharField(max_length=20)
    shortName = models.CharField(max_length=20)
    logo = models.URLField()
    c_playing = models.CharField(max_length=4)
    c_recent = models.CharField(max_length=4)
    c_played = models.CharField(max_length=4)
    c_future = models.CharField(max_length=4)
    c_past = models.CharField(max_length=4)
    start_date = models.DateField()
    end_date = models.DateField()
    troncal = models.CharField(max_length=4)
    cat = models.CharField(max_length=4)
    ctype = models.CharField(max_length=4)
    level = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=5)
    continent = models.CharField(max_length=4)
    current_round = models.CharField(max_length=4)
    total_group = models.CharField(max_length=4)
    total_rounds = models.CharField(max_length=4)
    end = models.CharField(max_length=4)
    cat_level = models.CharField(max_length=4)
    flag = models.URLField()
    logo_png = models.URLField()
    phase = models.CharField(max_length=10,blank=True,null=True)
    playoff = models.CharField(max_length=4)
    group_code = models.CharField(max_length=4)
    status_messages = models.JSONField()
    legend = models.JSONField()
    legend_dict = models.JSONField()
    
    
class TeamInfo(models.model):
    full_name = models.CharField(max_length=100,null=True,blank=True)
    short_name = models.CharField(max_length=5,null=True,blank=True)
    shield = models.CharField(max_length=300,null=True,blank=True)
    shield_big = models.CharField(max_length=300,null=True,blank=True)
    shield_png = models.CharField(max_length=300,null=True,blank=True)
    stadium = models.CharField(max_length=100,null=True,blank=True)
    managerNow = models.CharField(max_length=50,null=True,blank=True)
    seats = models.CharField(max_length=10,null=True,blank=True)
    yearFoundation = models.CharField(max_length=4,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    adress = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    chairman = models.CharField(max_length=100,null=True,blank=True)
    fans = models.CharField(max_length=10,null=True,blank=True)
    yearBuilt = models.CharField(max_length=5,null=True,blank=True)
    size = models.CharField(max_length=50,null=True,blank=True)
    historical = models.CharField(max_length=1000,blank=True,null=True)
    twitter = models.CharField(max_length=50,null=True,blank=True)
    last_change = models.CharField(max_length=30,null=True,blank=True)
    patrocinador = models.CharField(max_length=50,null=True,blank=True)
    team_b = models.CharField(max_length=30,null=True,blank=True)
    proveedor = models.CharField(max_length=50,null=True,blank=True)
    lugar_entrenamiento = models.CharField(max_length=100,null=True,blank=True)
    int = models.CharField(max_length=5,null=True,blank=True)
    int_sub = models.CharField(max_length=5,null=True,blank=True)
    admin_workers = models.CharField(max_length=5,null=True,blank=True)
    sports_workers = models.CharField(max_length=5,null=True,blank=True)
    squadyearlybudget = models.CharField(max_length=10,null=True,blank=True)
    presidentNow = models.CharField(max_length=50,null=True,blank=True)
    img_stadium = models.CharField(max_length=300,null=True,blank=True)
    team_flag = models.CharField(max_length=300,null=True,blank=True)
    
    class Meta:
        abtract = True

class Table(models.Model):
    group = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    conference = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=200)
    points = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    shield = models.URLField(blank=True, null=True)
    cflag = models.URLField(blank=True, null=True)
    gf = models.IntegerField(blank=True, null=True)
    ga = models.IntegerField(blank=True, null=True)
    avg = models.IntegerField(blank=True, null=True)
    matchs_coef = models.CharField(max_length=255, blank=True, null=True)
    points_coef = models.CharField(max_length=255, blank=True, null=True)
    coef = models.CharField(max_length=255, blank=True, null=True)
    coefficients = models.CharField(max_length=255, blank=True, null=True)
    mark = models.CharField(max_length=255, blank=True, null=True)
    class_mark = models.CharField(max_length=255, blank=True, null=True)
    round = models.IntegerField(blank=True, null=True)
    pos = models.IntegerField(blank=True, null=True)
    countrycode = models.CharField(max_length=10)
    abbr = models.CharField(max_length=20)
    form = models.CharField(max_length=255)
    direction = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    # Estos campos están relacionados con el diccionario "info"
    # donde "type_id" representa el ID del tipo y "type" es el tipo en sí.

    class Meta:
        abstract = True
        
class SimplePlayer(models.Model):
    id = models.IntegerField(primary_key=True)
    team_id = models.IntegerField()
    nick = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    birthdate = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    foot = models.IntegerField()
    side = models.IntegerField()
    role = models.IntegerField()
    year = models.IntegerField()
    squadNumber = models.IntegerField(blank=True)
    num = models.CharField(max_length=10,blank=True)
    pos = models.CharField(max_length=10,blank=True)
    idplayer = models.CharField(max_length=10,blank=True)
    goals = models.CharField(max_length=10,blank=True)
    reds = models.CharField(max_length=10,blank=True)
    yellows = models.CharField(max_length=10,blank=True)
    CountryCode = models.CharField(max_length=2)
    gender = models.IntegerField(blank=True)
    image = models.URLField()

    def __str__(self):
        return self.nick

    
class Team(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    id_comp = models.CharField(max_length=10)
    basealias = models.CharField(max_length=30)
    name_show = models.CharField(max_length=50, null=True, blank=True)
    full_name = models.CharField(max_length=100,null=True,blank=True)
    short_name = models.CharField(max_length=5,null=True,blank=True)
    shield = models.CharField(max_length=300,null=True,blank=True)
    shield_big = models.CharField(max_length=300,null=True,blank=True)
    shield_png = models.CharField(max_length=300,null=True,blank=True)
    stadium = models.CharField(max_length=100,null=True,blank=True)
    managerNow = models.CharField(max_length=50,null=True,blank=True)
    seats = models.CharField(max_length=10,null=True,blank=True)
    yearFoundation = models.CharField(max_length=4,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    adress = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    chairman = models.CharField(max_length=100,null=True,blank=True)
    fans = models.CharField(max_length=10,null=True,blank=True)
    yearBuilt = models.CharField(max_length=5,null=True,blank=True)
    size = models.CharField(max_length=50,null=True,blank=True)
    historical = models.CharField(max_length=1000,blank=True,null=True)
    twitter = models.CharField(max_length=50,null=True,blank=True)
    last_change = models.CharField(max_length=30,null=True,blank=True)
    patrocinador = models.CharField(max_length=50,null=True,blank=True)
    team_b = models.CharField(max_length=30,null=True,blank=True)
    proveedor = models.CharField(max_length=50,null=True,blank=True)
    lugar_entrenamiento = models.CharField(max_length=100,null=True,blank=True)
    int = models.CharField(max_length=5,null=True,blank=True)
    int_sub = models.CharField(max_length=5,null=True,blank=True)
    admin_workers = models.CharField(max_length=5,null=True,blank=True)
    sports_workers = models.CharField(max_length=5,null=True,blank=True)
    squadyearlybudget = models.CharField(max_length=10,null=True,blank=True)
    presidentNow = models.CharField(max_length=50,null=True,blank=True)
    img_stadium = models.CharField(max_length=300,null=True,blank=True)
    team_flag = models.CharField(max_length=300,null=True,blank=True)
    
        #clasificacion
    group = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    conference = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=200)
    points = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    shield = models.URLField(blank=True, null=True)
    cflag = models.URLField(blank=True, null=True)
    gf = models.IntegerField(blank=True, null=True)
    ga = models.IntegerField(blank=True, null=True)
    avg = models.IntegerField(blank=True, null=True)
    matchs_coef = models.CharField(max_length=255, blank=True, null=True)
    points_coef = models.CharField(max_length=255, blank=True, null=True)
    coef = models.CharField(max_length=255, blank=True, null=True)
    coefficients = models.CharField(max_length=255, blank=True, null=True)
    mark = models.CharField(max_length=255, blank=True, null=True)
    class_mark = models.CharField(max_length=255, blank=True, null=True)
    round = models.IntegerField(blank=True, null=True)
    pos = models.IntegerField(blank=True, null=True)
    countrycode = models.CharField(max_length=10)
    abbr = models.CharField(max_length=20)
    form = models.CharField(max_length=255)
    direction = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)

    squad = models.ManyToManyField(SimplePlayer, blank=True)
    
    def __str__(self):
        return self.basealias
    
    class Meta:
        abtract = True

class Table(models.Model):
    group = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    conference = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=200)
    points = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    shield = models.URLField(blank=True, null=True)
    cflag = models.URLField(blank=True, null=True)
    gf = models.IntegerField(blank=True, null=True)
    ga = models.IntegerField(blank=True, null=True)
    avg = models.IntegerField(blank=True, null=True)
    matchs_coef = models.CharField(max_length=255, blank=True, null=True)
    points_coef = models.CharField(max_length=255, blank=True, null=True)
    coef = models.CharField(max_length=255, blank=True, null=True)
    coefficients = models.CharField(max_length=255, blank=True, null=True)
    mark = models.CharField(max_length=255, blank=True, null=True)
    class_mark = models.CharField(max_length=255, blank=True, null=True)
    round = models.IntegerField(blank=True, null=True)
    pos = models.IntegerField(blank=True, null=True)
    countrycode = models.CharField(max_length=10)
    abbr = models.CharField(max_length=20)
    form = models.CharField(max_length=255)
    direction = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    clasificacion = models.OneToOneField(Table, on_delete=models.CASCADE, null=True, blank=True)
    squad = models.ManyToManyField(SimplePlayer, blank=True)
    
    #clasificacion
    group = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    conference = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=200)
    points = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    shield = models.URLField(blank=True, null=True)
    cflag = models.URLField(blank=True, null=True)
    gf = models.IntegerField(blank=True, null=True)
    ga = models.IntegerField(blank=True, null=True)
    avg = models.IntegerField(blank=True, null=True)
    matchs_coef = models.CharField(max_length=255, blank=True, null=True)
    points_coef = models.CharField(max_length=255, blank=True, null=True)
    coef = models.CharField(max_length=255, blank=True, null=True)
    coefficients = models.CharField(max_length=255, blank=True, null=True)
    mark = models.CharField(max_length=255, blank=True, null=True)
    class_mark = models.CharField(max_length=255, blank=True, null=True)
    round = models.IntegerField(blank=True, null=True)
    pos = models.IntegerField(blank=True, null=True)
    countrycode = models.CharField(max_length=10)
    abbr = models.CharField(max_length=20)
    form = models.CharField(max_length=255)
    direction = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)

    squad = models.ManyToManyField(SimplePlayer, blank=True)
    
    def __str__(self):
        return self.basealias
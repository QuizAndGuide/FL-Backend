from django.contrib import admin
from django.conf import settings
from djongo import models

class UserProfile(models.Model):
    MEMBERSHIP_FREE = 'F'
    MEMBERSHIP_PREMIUM = 'P'
    MEMBERSHIP_PREMIUMPLUS = 'P+'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_FREE, 'Free'),
        (MEMBERSHIP_PREMIUM, 'Premium'),
        (MEMBERSHIP_PREMIUMPLUS, 'Premium+'),
    ]
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    coins = models.IntegerField(default=1000) 
    rating = models.IntegerField(default=1200)  
    country = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    membership = models.CharField(
        max_length=2, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_FREE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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


    
class Teams(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    id_comp = models.CharField(max_length=10,null=True,blank=True)
    basealias = models.CharField(max_length=20,null=True,blank=True)
    name_show = models.CharField(max_length=50,null=True,blank=True)
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

    def __str__(self):
        return self.basealias



class Clasificacion(models.Model):
    team_id = models.IntegerField()
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
        ordering = ['pos', 'group']
    # TYPE_1 = 'campeon'
    # TYPE_2 = 'cha'
    # TYPE_3 = 'uefa'
    # TYPE_4 = 'Regular'
    # TYPE_5 = 'elimconf'
    # TYPE_6 = 'desc'
                                              #es un intento de incorporar la leyenda, no es practico, por ahora
                                              
    # TYPE_CHOICES = [ 
    #     (TYPE_1, 'Campe\u00f3n'),
    #     (TYPE_2, 'Champions League'),
    #     (TYPE_3, 'Europa League'),
    #     (TYPE_4, 'laliga'),
    #     (TYPE_5, 'Fase Eliminatoria Conference League'),
    #     (TYPE_6, 'Descenso')
    # ]
    # type = models.CharField(max_length=40,choices=TYPE_CHOICES,null=True,blank=True)

    
class Player(models.Model):
    player_id = models.CharField(max_length=10,primary_key=True)
    team_id = models.CharField(max_length=50,blank=True)
    nick = models.CharField(max_length=50,blank=True)
    name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    alias = models.CharField(max_length=50,blank=True)
    birthdate = models.CharField(max_length=50,blank=True)
    height = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    foot = models.CharField(max_length=10,blank=True)
    side = models.CharField(max_length=10,blank=True)
    role = models.CharField(max_length=10,blank=True)
    squadNumber = models.IntegerField(blank=True)
    num = models.CharField(max_length=10,blank=True)
    pos = models.CharField(max_length=10,blank=True)
    goals = models.IntegerField(blank=True)
    reds = models.IntegerField(blank=True)
    yellows = models.IntegerField(blank=True)
    CountryCode = models.CharField(max_length=5,blank=True)
    age = models.IntegerField(blank=True)
    rating = models.FloatField(blank=True)
    total_value = models.FloatField(blank=True)
    cage = models.IntegerField(blank=True)
    ycards = models.IntegerField(blank=True)
    rcards = models.IntegerField(blank=True)
    cards = models.IntegerField(blank=True)
    assists = models.IntegerField(blank=True)
    matched = models.IntegerField(blank=True)
    called = models.IntegerField(blank=True)
    lineup = models.IntegerField(blank=True)
    minutes = models.IntegerField(blank=True)
    goals_conceded = models.IntegerField(blank=True)
    goals2 = models.IntegerField(blank=True)
    goals_penalty = models.IntegerField(blank=True)
    total_appearances = models.IntegerField(blank=True)
    total_minutes = models.IntegerField(blank=True)
    total_goalsconceded = models.IntegerField(blank=True)
    total_penaltyerrors = models.IntegerField(blank=True)
    total_penaltysaves = models.IntegerField(blank=True)
    total_subs = models.IntegerField(blank=True)
    total_subs_in = models.IntegerField(blank=True)
    total_subs_out = models.IntegerField(blank=True)
    total_own_goals = models.IntegerField(blank=True)
    total_full_matches_completed = models.IntegerField(blank=True)
    total_lineup_appearances = models.IntegerField(blank=True)
    assist = models.IntegerField(blank=True)
    birthplace = models.CharField(max_length=255,blank=True)
    palmaresTxt = models.TextField(blank=True)
    real_value = models.FloatField(blank=True)
    total_value_1y = models.FloatField(blank=True)
    pos1 = models.CharField(max_length=10,blank=True)
    pos2 = models.CharField(max_length=10,blank=True)
    pos3 = models.CharField(max_length=10,blank=True)
    pos4 = models.CharField(max_length=10,blank=True)
    pos1p = models.FloatField(blank=True)
    pos2p = models.FloatField(blank=True)
    pos3p = models.FloatField(blank=True)
    pos4p = models.FloatField(blank=True)
    national_team = models.CharField(max_length=255,blank=True)
    national_caps = models.IntegerField(blank=True)
    national_lineup = models.IntegerField(blank=True)
    national_goals = models.IntegerField(blank=True)
    national_team_u17 = models.CharField(max_length=255,blank=True)
    national_team_u19 = models.CharField(max_length=255,blank=True)
    national_team_u20 = models.CharField(max_length=255,blank=True)
    national_team_u21 = models.CharField(max_length=255,blank=True)
    national_team_u23 = models.CharField(max_length=255,blank=True)
    national_caps_u17 = models.IntegerField(blank=True)
    national_caps_u19 = models.IntegerField(blank=True)
    national_caps_u20 = models.IntegerField(blank=True)
    national_caps_u21 = models.IntegerField(blank=True)
    national_caps_u23 = models.IntegerField(blank=True)
    national_called = models.IntegerField(blank=True)
    national_debut = models.CharField(max_length=255,blank=True)
    national_last = models.CharField(max_length=255,blank=True)
    national_min_age = models.FloatField(blank=True)
    national_max_age = models.FloatField(blank=True)
    career_max_value = models.FloatField(blank=True)
    player_status = models.CharField(max_length=255,blank=True)
    role_name = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.name

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

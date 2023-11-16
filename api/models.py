from django.contrib import admin
from django.conf import settings
from djongo import models

class Profile(models.Model):
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


    
class Round(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    group = models.IntegerField()
    total_group = models.IntegerField()
    round = models.IntegerField()
    local = models.CharField(max_length=25, blank=True, null=True)
    visitor = models.CharField(max_length=25, blank=True, null=True)
    league_id = models.IntegerField()
    stadium = models.CharField(max_length=255, blank=True, null=True)
    team1 = models.IntegerField()
    team2 = models.IntegerField()
    conference = models.IntegerField()
    dteam1 = models.IntegerField()
    dteam2 = models.IntegerField()
    numc = models.IntegerField()
    no_hour = models.BooleanField(default=False)
    local_abbr = models.CharField(max_length=3, blank=True, null=True)
    visitor_abbr = models.CharField(max_length=3, blank=True, null=True)
    competition_name = models.CharField(max_length=25, blank=True, null=True)
    competition_id = models.IntegerField()
    split_league = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)
    type_id = models.IntegerField()
    playoffs = models.BooleanField(default=False)
    group_code = models.IntegerField()
    total_rounds = models.IntegerField()
    coef = models.FloatField()
    cflag_local = models.URLField()
    cflag_visitor = models.URLField()
    local_shield = models.URLField()
    visitor_shield = models.URLField()
    extraTxt = models.CharField(max_length=255, blank=True, null=True)
    schedule = models.DateTimeField()
    date = models.DateField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    local_goals = models.CharField(max_length=3, blank=True, null=True)
    visitor_goals = models.CharField(max_length=3, blank=True, null=True)
    result = models.CharField(max_length=10)
    live_minute = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    channels = models.JSONField()
    winner = models.CharField(max_length=10, blank=True, null=True)
    penaltis1 = models.IntegerField(blank=True, null=True)
    penaltis2 = models.IntegerField(blank=True, null=True)
    prorroga = models.BooleanField(default=False)
       

class Stats(models.Model):
    player_id = models.IntegerField()
    nick = models.CharField(max_length=30) 
    name = models.CharField(max_length=255) 
    role = models.IntegerField()
    flag = models.CharField(max_length=2)
    last_name = models.CharField(max_length=255)
    team_id = models.IntegerField()
    cc = models.CharField(max_length=2)
    team_name = models.CharField(max_length=30)
    goals = models.IntegerField(blank=True, null=True)
    yellow_cards = models.IntegerField(blank=True, null=True)
    red_cards = models.IntegerField(blank=True, null=True)
    asists = models.IntegerField(blank=True, null=True)
    year = models.IntegerField()
    player_alias = models.CharField(max_length=30)
    team_alias = models.CharField(max_length=30)
    team_shield = models.URLField()
    player_image = models.URLField()
    team_flag = models.URLField()

# class Goleadores(models.Model):
#     player_id = models.IntegerField()
#     nick = models.CharField(max_length=25), 
#     name = models.CharField(max_length=255) 
#     role = models.IntegerField()
#     flag = models.CharField(max_length=2)
#     last_name = models.CharField(max_length=15)
#     team_id = models.IntegerField()
#     cc = models.CharField(max_length=2)
#     team_name = models.CharField(max_length=15)
#     total = models.IntegerField(blank=True, null=True)
#     year = models.IntegerField()
#     player_alias = models.CharField(max_length=30)
#     team_alias = models.CharField(max_length=15)
#     team_shield = models.URLField()
#     player_image = models.URLField()
#     team_flag = models.URLField()

# class Agenda(models.Model):
#     Agenda = models.JSONField()
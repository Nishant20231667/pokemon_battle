import uuid
from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    japanese_name = models.CharField(max_length=100, null=True, blank=True)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, null=True, blank=True)
    attack = models.IntegerField()
    defense = models.IntegerField()
    hp = models.IntegerField()
    speed = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    abilities = models.CharField(max_length=255, null=True, blank=True)
    against_bug = models.FloatField()
    against_dark = models.FloatField()
    against_dragon = models.FloatField()
    against_electric = models.FloatField()
    against_fairy = models.FloatField()
    against_fight = models.FloatField()
    against_fire = models.FloatField()
    against_flying = models.FloatField()
    against_ghost = models.FloatField()
    against_grass = models.FloatField()
    against_ground = models.FloatField()
    against_ice = models.FloatField()
    against_normal = models.FloatField()
    against_poison = models.FloatField()
    against_psychic = models.FloatField()
    against_rock = models.FloatField()
    against_steel = models.FloatField()
    against_water = models.FloatField()
    base_egg_steps = models.IntegerField()
    base_happiness = models.IntegerField()
    base_total = models.IntegerField()
    capture_rate = models.CharField(max_length=50)
    classfication = models.CharField(max_length=100)
    experience_growth = models.IntegerField()
    height_m = models.FloatField(null=True)
    percentage_male = models.FloatField(null=True, blank=True)
    pokedex_number = models.IntegerField(unique=True)
    weight_kg = models.FloatField(null=True)
    generation = models.IntegerField()
    is_legendary = models.BooleanField()

    def __str__(self):
        return self.name



class Battle(models.Model):
    STATUS_CHOICES = [
        ('BATTLE_INPROGRESS', 'In Progress'),
        ('BATTLE_COMPLETED', 'Completed'),
        ('BATTLE_FAILED', 'Failed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pokemon_a = models.ForeignKey(Pokemon, related_name='battles_as_a', on_delete=models.CASCADE)
    pokemon_b = models.ForeignKey(Pokemon, related_name='battles_as_b', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='BATTLE_INPROGRESS')
    result = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Battle {self.id} between {self.pokemon_a.name} and {self.pokemon_b.name}"
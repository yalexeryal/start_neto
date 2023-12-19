from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ListProfessions(models.Model):
    name_professions = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name_professions


class Positions(models.Model):
    name_positions = models.CharField(max_length=200)

    def __str__(self):
        return self.name_positions


class EducationBlocks(models.Model):
    education_blocks = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.education_blocks


class Units(models.Model):
    name_unit = models.CharField(max_length=50, unique=True)
    id_profession = models.ForeignKey("Professions", related_name="Профессия", on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name_unit


class Professions(models.Model):
    name_profession = models.CharField(max_length=200)
    kod_profession = models.IntegerField()
    id_units = models.ForeignKey(Units, on_delete=models.CASCADE)
    id_lead_coordinator = models.ForeignKey("Persons", related_name="ВКН", on_delete=models.CASCADE)
    id_coordinator = models.ForeignKey("Persons", related_name="Координатор+", on_delete=models.CASCADE)
    id_education_block = models.ForeignKey("EducationBlock", related_name="Блок обучения+", on_delete=models.CASCADE)
    date_start = models.DateField()
    date_finish = models.DateField()
    date_closing = models.DateField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name_profession}-{self.kod_profession}"


class Persons(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField(blank=True)
    id_position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    email_persons = models.EmailField()
    slack = models.CharField(max_length=20)
    discord = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"


class EducationBlock(models.Model):
    name_education_block = models.CharField(max_length=20)
    kod_education_block = models.IntegerField()
    id_profession = models.ForeignKey(Professions, related_name="Профессиb", on_delete=models.CASCADE)
    id_coordinator = models.ForeignKey(Persons, related_name="Координатор", on_delete=models.CASCADE)
    date_start = models.DateField()
    date_finish = models.DateField()
    date_closing = models.DateField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_education_block}-{self.kod_education_block}"

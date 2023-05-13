from django.db import models

# Create your models here.

class AircraftModel(models.Model):
    id = models.UUIDField(primary_key = True, auto_created=True)
    model_name = models.CharField(max_length=100)
    manufacturer_name = models.CharField(max_length=100)


class PartDetails(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    new_part_water_usage = models.IntegerField(default=0)
    new_part_energy_consumption = models.IntegerField(default=0)
    new_part_landfill_waste = models.IntegerField(default=0)
    new_part_part_carbon_footprint = models.IntegerField(default=0)
    new_part_toxicity_score = models.FloatField(default=0)
    renew_part_energy_consumption = models.FloatField(default=0)
    renew_part_water_usage = models.IntegerField(default=0)
    renew_part_landfill_waste = models.IntegerField(default=0)
    renew_part_carbon_foot_print = models.IntegerField(default=0)
    renew_part_toxicity_score = models.FloatField(default=0)
    carbon_footprint_saved = models.FloatField(default=0)
    water_usage_saved = models.FloatField(default=0)
    landfill_waste_saved = models.FloatField(default=0)
    energy_saved = models.FloatField(default=0)
    life_cycle_assesment_score = models.FloatField(default=0)


class Part(models.Model):
    part_id = models.UUIDField(primary_key = True, auto_created=True)
    name = models.CharField(max_length= 50)
    material_composition = models.CharField(max_length=50)
    age = models.IntegerField()
    condition = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    potential_use_case = models.CharField(max_length=100, default=None)
    recycle_rate = models.FloatField(default=0)
    remanufacturing_potential = models.FloatField(default=0)
    renew_material_content = models.FloatField(default=0)
    toxic_score_difference = models.FloatField(default=0)
    remanufacturing_potential_percent = models.FloatField(default=0)
    lifecycle_assesment = models.FloatField(default=0)
    model_id = models.ForeignKey(AircraftModel, db_column='model_id', related_name='aircraft_model',
                                 on_delete=models.DO_NOTHING)
    part_detail_id = models.ForeignKey(PartDetails, related_name='part_details', on_delete=models.DO_NOTHING)





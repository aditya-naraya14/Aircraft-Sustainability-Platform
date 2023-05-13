from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from aircraft.models import Part, AircraftModel, PartDetails
from  django.db import transaction
from rest_framework.decorators import api_view
import  uuid
# Create your views here.

class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Part
        exclude = []


class AircraftModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftModel
        exclude = ()

class PartDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartDetails
        exclude = ()



class PartViewSet(viewsets.ModelViewSet):
    model = Part
    serializer_class = PartSerializer
    queryset = Part.objects.all().select_related('part_detail_id')

    @transaction.atomic
    def create(self, request):
        # print(request.data)
        aircraft_obj = dict(
            {
                "id": uuid.uuid4(),
                "model_name": request.data.get('model_name'),
                "manufacturer_name": request.data.get('manufacturer_name')
            }
        )
        aircraft_model = AircraftModel.objects.filter(model_name=request.data.get('model_name'), manufacturer_name=request.data.get('manufacturer_name'))
        print(len(aircraft_model))
        if len(aircraft_model) == 0:
            aircraft_model = AircraftModel.objects.create(**aircraft_obj)

        part_detail_obj = {
            "id": uuid.uuid4(),
            "new_part_water_usage": request.data.get('new_part_water_usage'),
            "new_part_energy_consumption": request.data.get('new_part_energy_consumption'),
            "new_part_landfill_waste": request.data.get('new_part_landfill_waste'),
            "new_part_part_carbon_footprint": request.data.get('new_part_part_carbon_footprint'),
            "new_part_toxicity_score": request.data.get('new_part_toxicity_score'),
            "renew_part_energy_consumption": request.data.get('renew_part_energy_consumption'),
            "renew_part_water_usage": request.data.get('renew_part_water_usage'),
            "renew_part_landfill_waste": request.data.get('renew_part_landfill_waste'),
            "renew_part_carbon_foot_print": request.data.get('renew_part_carbon_foot_print'),
            "renew_part_toxicity_score": request.data.get('renew_part_toxicity_score'),
            "carbon_footprint_saved": request.data.get('carbon_footprint_saved'),
            "water_usage_saved": request.data.get('water_usage_saved'),
            "landfill_waste_saved": request.data.get('landfill_waste_saved'),
            "energy_saved": request.data.get('energy_saved'),
        }

        part_details = PartDetails.objects.create(**part_detail_obj)

        create_dict = dict({
            "part_id": uuid.uuid4(),
            "name": request.data.get('name'),
            "material_composition": request.data.get('material_composition'),
            "age": request.data.get('age'),
            "condition": request.data.get('condition'),
            "location": request.data.get('location'),
            "potential_use_case": request.data.get('potential_use_case'),
            "recycle_rate": request.data.get('recycle_rate'),
            "remanufacturing_potential": request.data.get('remanufacturing_potential'),
            "renew_material_content": request.data.get('renew_material_content'),
            "toxic_score_difference": request.data.get('toxic_score_difference'),
            "remanufacturing_potential_percent": request.data.get('remanufacturing_potential_percent'),
            "lifecycle_assesment": request.data.get('lifecycle_assesment'),
            "model_id": aircraft_model,
            "part_detail_id": part_details
        })
        part_id = Part.objects.create(**create_dict)

        action_data = PartSerializer(part_id)
        print(action_data)
        return Response(action_data.data)

class AircraftModelViewSet(viewsets.ModelViewSet):
    model = AircraftModel
    serializer_class = AircraftModelSerializer
    queryset = AircraftModel.objects.all()

class PartDetailModelViewSet(viewsets.ModelViewSet):
    model = PartDetails
    serializer_class = PartDetailsSerializer
    queryset = PartDetailsSerializer


class DataToDisplay(serializers.ModelSerializer):
    model_name = serializers.CharField(source="model_id.model_name")
    manufacturer_name = serializers.CharField(source="model_id.manufacturer_name")
    new_part_water_usage = serializers.IntegerField(source="part_detail_id.new_part_water_usage")
    new_part_energy_consumption = serializers.IntegerField(source="part_detail_id.new_part_energy_consumption")
    new_part_landfill_waste = serializers.IntegerField(source="part_detail_id.new_part_landfill_waste")
    new_part_part_carbon_footprint = serializers.IntegerField(source="part_detail_id.new_part_part_carbon_footprint")
    new_part_toxicity_score = serializers.FloatField(source="part_detail_id.new_part_toxicity_score")
    renew_part_energy_consumption = serializers.FloatField(source="part_detail_id.renew_part_energy_consumption")
    renew_part_water_usage = serializers.IntegerField(source="part_detail_id.renew_part_water_usage")
    renew_part_landfill_waste = serializers.IntegerField(source="part_detail_id.renew_part_landfill_waste")
    renew_part_carbon_foot_print = serializers.IntegerField(source="part_detail_id.renew_part_carbon_foot_print")
    renew_part_toxicity_score = serializers.FloatField(source="part_detail_id.renew_part_toxicity_score")
    carbon_footprint_saved = serializers.FloatField(source="part_detail_id.carbon_footprint_saved")
    water_usage_saved = serializers.FloatField(source="part_detail_id.water_usage_saved")
    landfill_waste_saved = serializers.FloatField(source="part_detail_id.landfill_waste_saved")
    energy_saved = serializers.FloatField(source="part_detail_id.energy_saved")


    class Meta:
        model = Part
        exclude = ('model_id', 'part_detail_id')

part_list = PartViewSet.as_view({'get': 'list', 'post': 'create'})
aircraft_list = AircraftModelViewSet.as_view({'get': 'list', 'post': 'create'})

@api_view(['GET'])
def get_values_to_display(request):
    data = Part.objects.select_related('part_detail_id', 'model_id').all()
    resp_data = DataToDisplay(data, many=True).data
    return Response(resp_data)
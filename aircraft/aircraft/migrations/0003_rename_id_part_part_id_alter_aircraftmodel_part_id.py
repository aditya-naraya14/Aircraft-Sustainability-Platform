# Generated by Django 4.2.1 on 2023-05-13 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("aircraft", "0002_alter_aircraftmodel_part_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="part",
            old_name="id",
            new_name="part_id",
        ),
        migrations.AlterField(
            model_name="aircraftmodel",
            name="part_id",
            field=models.ForeignKey(
                db_column="part_id",
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="id",
                to="aircraft.part",
            ),
        ),
    ]
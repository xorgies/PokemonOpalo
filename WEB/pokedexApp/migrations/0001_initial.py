# Generated by Django 5.0 on 2023-12-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('genderRate', models.CharField(max_length=50)),
                ('growthRate', models.CharField(max_length=50)),
                ('rareness', models.IntegerField()),
                ('happiness', models.IntegerField()),
                ('compatibility', models.CharField(max_length=50)),
                ('stepsToHatch', models.IntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('color', models.CharField(max_length=50)),
                ('pokedex', models.TextField()),
            ],
        ),
    ]

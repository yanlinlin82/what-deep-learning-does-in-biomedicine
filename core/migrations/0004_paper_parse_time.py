# Generated by Django 5.0.7 on 2024-08-06 16:21

from django.db import migrations, models

def assign_parse_time(apps, schema_editor):
    Paper = apps.get_model('core', 'Paper')
    for paper in Paper.objects.all():
        paper.parse_time = paper.created
        paper.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_paper_pub_date_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='parse_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.RunPython(assign_parse_time),
    ]

# Generated by Django 3.2.9 on 2021-11-17 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0025_alter_exam_result_db_exam_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_result_db',
            name='exam_type',
            field=models.CharField(choices=[('Written', 'Written'), ('Practical', 'Practical')], default='Written', max_length=10),
        ),
    ]

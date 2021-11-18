# Generated by Django 3.2.9 on 2021-11-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0026_alter_exam_result_db_exam_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle_db',
            name='username',
        ),
        migrations.AddField(
            model_name='vehicle_db',
            name='citizenship',
            field=models.CharField(default='1234567890', max_length=30),
        ),
        migrations.AlterField(
            model_name='vehicle_db',
            name='vehicle_type',
            field=models.CharField(choices=[('Two-Wheeler', 'Two-Wheeler'), ('Four-Wheeler', 'Four-Wheeler'), ('Many-Wheeler', 'Many-Wheeler')], default='Two-Wheeler', max_length=15),
        ),
    ]
# Generated by Django 4.0 on 2022-01-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_requests', '0013_alter_offerrequests_related_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerrequests',
            name='status',
        ),
        migrations.AddField(
            model_name='offerrequests',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]

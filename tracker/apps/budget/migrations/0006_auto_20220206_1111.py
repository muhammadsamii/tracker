# Generated by Django 3.1.6 on 2022-02-06 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_auto_20220206_1101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budget',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='expense_category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='income_category',
            options={'ordering': ['id']},
        ),
    ]

# Generated by Django 4.0.1 on 2022-10-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_items_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_type',
            field=models.CharField(choices=[('Sword', 'Sword'), ('Dagger', 'Dagger'), ('Bow', 'Bow'), ('Axe', 'Axe'), ('Spear', 'Spear'), ('Staff', 'Staff'), ('Mace', 'Mace'), ('Warrior Armor', 'Warrior_armor'), ('Mage Armor', 'Mage_armor'), ('Rogue Armor', 'Rogue_armor'), ('Priest Armor', 'Priest_armor'), ('Accesories', 'Accesories')], default='', max_length=32, verbose_name='item_type'),
        ),
    ]

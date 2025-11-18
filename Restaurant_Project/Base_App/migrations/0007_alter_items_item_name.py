

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0006_alter_items_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Item_name',
            field=models.CharField(max_length=40),
        ),
    ]

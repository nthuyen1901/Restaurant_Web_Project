

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0008_alter_items_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Image',
            field=models.ImageField(upload_to='items/'),
        ),
    ]

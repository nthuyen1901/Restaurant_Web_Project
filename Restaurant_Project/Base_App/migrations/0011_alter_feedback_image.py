

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0010_feedback_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Image',
            field=models.ImageField(blank=True, upload_to='feedback/'),
        ),
    ]

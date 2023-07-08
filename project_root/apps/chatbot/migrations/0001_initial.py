```python
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ChatBot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('api_key', models.CharField(max_length=255)),
                ('platform', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
```
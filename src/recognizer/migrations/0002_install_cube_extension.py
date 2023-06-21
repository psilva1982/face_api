from django.db import migrations

def create_cube_extension(apps, schema_editor):
    schema_editor.execute("CREATE EXTENSION cube;")

class Migration(migrations.Migration):

    run_before = [
        ('recognizer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_cube_extension)
    ]

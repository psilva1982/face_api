from django.db import migrations
from django.contrib.auth import get_user_model
from django.conf import settings

def create_demo_user(apps, schema_editor):

    email = "demo@demo.com"

    User = get_user_model()
    demo_user = User.objects.create(
        email=email,
        name="Demo user",
        is_staff=True,
        is_active=True,
        is_superuser=True
    )
    demo_user.set_password('demo')
    demo_user.save()

    UserModel = apps.get_model("users", "User")
    EmailAddress = apps.get_model("account", "EmailAddress")

    user = UserModel.objects.get(email=email)
    EmailAddress.objects.create(
        user=user,
        email=email,
        verified=True,
        primary=True
    )


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_demo_user),
    ]

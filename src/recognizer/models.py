from django.db import models
from django.utils.crypto import get_random_string
from recognizer import functions

import uuid


def upload_to(instance, filename):
    extension = filename.split(".")[1]
    rand_str = get_random_string(length=8)
    file = f"{rand_str}.{extension}"
    return "photos/{0}/{1}/{2}".format(
        instance.person.database.name.lower(), instance.person.uuid, file
    )


class PersonDatabase(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=64)

    class Meta:
        ordering = ["name"]
        verbose_name = "database"
        verbose_name_plural = "databases"

    def __str__(self) -> str:
        return self.name


class Person(models.Model):
    uuid = models.UUIDField(unique=True, blank=False, null=False, default=uuid.uuid4)
    database = models.ForeignKey(PersonDatabase, on_delete=models.PROTECT)
    name = models.CharField(max_length=254)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    @property
    def profile_image(self):
        return self.photos.all().first()

    @staticmethod
    def sql_search_face(image_file, in_memory_file=False, after_remove=False):
        return functions.sql_face_search(
            image_file, in_memory_file=in_memory_file, after_remove=after_remove
        )


class PersonPhoto(models.Model):
    uuid = models.UUIDField(unique=True, blank=False, null=False, default=uuid.uuid4)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="photos")
    file = models.ImageField(upload_to=upload_to)
    processed = models.BooleanField(default=False)
    processed_error = models.BooleanField(default=False)

    p001 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p002 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p003 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p004 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p005 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p006 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p007 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p008 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p009 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p010 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p011 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p012 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p013 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p014 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p015 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p016 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p017 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p018 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p019 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p020 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p021 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p022 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p023 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p024 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p025 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p026 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p027 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p028 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p029 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p030 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p031 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p032 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p033 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p034 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p035 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p036 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p037 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p038 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p039 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p040 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p041 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p042 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p043 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p044 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p045 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p046 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p047 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p048 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p049 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p050 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p051 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p052 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p053 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p054 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p055 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p056 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p057 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p058 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p059 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p060 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p061 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p062 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p063 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p064 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p065 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p066 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p067 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p068 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p069 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p070 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p071 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p072 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p073 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p074 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p075 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p076 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p077 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p078 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p079 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p080 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p081 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p082 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p083 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p084 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p085 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p086 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p087 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p088 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p089 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p090 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p091 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p092 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p093 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p094 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p095 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p096 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p097 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p098 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p099 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p100 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p101 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p102 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p103 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p104 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p105 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p106 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p107 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p108 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p109 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p110 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p111 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p112 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p113 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p114 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p115 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p116 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p117 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p118 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p119 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p120 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p121 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p122 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p123 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p124 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p125 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p126 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p127 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)
    p128 = models.DecimalField(max_digits=30, decimal_places=28, null=True, blank=True)

    @property
    def arrayPoints(self):
        return [
            self.p001 if self.p001 is not None else 9.9,
            self.p002 if self.p002 is not None else 9.9,
            self.p003 if self.p003 is not None else 9.9,
            self.p004 if self.p004 is not None else 9.9,
            self.p005 if self.p005 is not None else 9.9,
            self.p006 if self.p006 is not None else 9.9,
            self.p007 if self.p007 is not None else 9.9,
            self.p008 if self.p008 is not None else 9.9,
            self.p009 if self.p009 is not None else 9.9,
            self.p010 if self.p010 is not None else 9.9,
            self.p011 if self.p011 is not None else 9.9,
            self.p012 if self.p012 is not None else 9.9,
            self.p013 if self.p013 is not None else 9.9,
            self.p014 if self.p014 is not None else 9.9,
            self.p015 if self.p015 is not None else 9.9,
            self.p016 if self.p016 is not None else 9.9,
            self.p017 if self.p017 is not None else 9.9,
            self.p018 if self.p018 is not None else 9.9,
            self.p019 if self.p019 is not None else 9.9,
            self.p020 if self.p020 is not None else 9.9,
            self.p021 if self.p021 is not None else 9.9,
            self.p022 if self.p022 is not None else 9.9,
            self.p023 if self.p023 is not None else 9.9,
            self.p024 if self.p024 is not None else 9.9,
            self.p025 if self.p025 is not None else 9.9,
            self.p026 if self.p026 is not None else 9.9,
            self.p027 if self.p027 is not None else 9.9,
            self.p028 if self.p028 is not None else 9.9,
            self.p029 if self.p029 is not None else 9.9,
            self.p030 if self.p030 is not None else 9.9,
            self.p031 if self.p031 is not None else 9.9,
            self.p032 if self.p032 is not None else 9.9,
            self.p033 if self.p033 is not None else 9.9,
            self.p034 if self.p034 is not None else 9.9,
            self.p035 if self.p035 is not None else 9.9,
            self.p036 if self.p036 is not None else 9.9,
            self.p037 if self.p037 is not None else 9.9,
            self.p038 if self.p038 is not None else 9.9,
            self.p039 if self.p039 is not None else 9.9,
            self.p040 if self.p040 is not None else 9.9,
            self.p041 if self.p041 is not None else 9.9,
            self.p042 if self.p042 is not None else 9.9,
            self.p043 if self.p043 is not None else 9.9,
            self.p044 if self.p044 is not None else 9.9,
            self.p045 if self.p045 is not None else 9.9,
            self.p046 if self.p046 is not None else 9.9,
            self.p047 if self.p047 is not None else 9.9,
            self.p048 if self.p048 is not None else 9.9,
            self.p049 if self.p049 is not None else 9.9,
            self.p050 if self.p050 is not None else 9.9,
            self.p051 if self.p051 is not None else 9.9,
            self.p052 if self.p052 is not None else 9.9,
            self.p053 if self.p053 is not None else 9.9,
            self.p054 if self.p054 is not None else 9.9,
            self.p055 if self.p055 is not None else 9.9,
            self.p056 if self.p056 is not None else 9.9,
            self.p057 if self.p057 is not None else 9.9,
            self.p058 if self.p058 is not None else 9.9,
            self.p059 if self.p059 is not None else 9.9,
            self.p060 if self.p060 is not None else 9.9,
            self.p061 if self.p061 is not None else 9.9,
            self.p062 if self.p062 is not None else 9.9,
            self.p063 if self.p063 is not None else 9.9,
            self.p064 if self.p064 is not None else 9.9,
            self.p065 if self.p065 is not None else 9.9,
            self.p066 if self.p066 is not None else 9.9,
            self.p067 if self.p067 is not None else 9.9,
            self.p068 if self.p068 is not None else 9.9,
            self.p069 if self.p069 is not None else 9.9,
            self.p070 if self.p070 is not None else 9.9,
            self.p071 if self.p071 is not None else 9.9,
            self.p072 if self.p072 is not None else 9.9,
            self.p073 if self.p073 is not None else 9.9,
            self.p074 if self.p074 is not None else 9.9,
            self.p075 if self.p075 is not None else 9.9,
            self.p076 if self.p076 is not None else 9.9,
            self.p077 if self.p077 is not None else 9.9,
            self.p078 if self.p078 is not None else 9.9,
            self.p079 if self.p079 is not None else 9.9,
            self.p080 if self.p080 is not None else 9.9,
            self.p081 if self.p081 is not None else 9.9,
            self.p082 if self.p082 is not None else 9.9,
            self.p083 if self.p083 is not None else 9.9,
            self.p084 if self.p084 is not None else 9.9,
            self.p085 if self.p085 is not None else 9.9,
            self.p086 if self.p086 is not None else 9.9,
            self.p087 if self.p087 is not None else 9.9,
            self.p088 if self.p088 is not None else 9.9,
            self.p089 if self.p089 is not None else 9.9,
            self.p090 if self.p090 is not None else 9.9,
            self.p091 if self.p091 is not None else 9.9,
            self.p092 if self.p092 is not None else 9.9,
            self.p093 if self.p093 is not None else 9.9,
            self.p094 if self.p094 is not None else 9.9,
            self.p095 if self.p095 is not None else 9.9,
            self.p096 if self.p096 is not None else 9.9,
            self.p097 if self.p097 is not None else 9.9,
            self.p098 if self.p098 is not None else 9.9,
            self.p099 if self.p099 is not None else 9.9,
            self.p100 if self.p100 is not None else 9.9,
            self.p101 if self.p101 is not None else 9.9,
            self.p102 if self.p102 is not None else 9.9,
            self.p103 if self.p103 is not None else 9.9,
            self.p104 if self.p104 is not None else 9.9,
            self.p105 if self.p105 is not None else 9.9,
            self.p106 if self.p106 is not None else 9.9,
            self.p107 if self.p107 is not None else 9.9,
            self.p108 if self.p108 is not None else 9.9,
            self.p109 if self.p109 is not None else 9.9,
            self.p110 if self.p110 is not None else 9.9,
            self.p111 if self.p111 is not None else 9.9,
            self.p112 if self.p112 is not None else 9.9,
            self.p113 if self.p113 is not None else 9.9,
            self.p114 if self.p114 is not None else 9.9,
            self.p115 if self.p115 is not None else 9.9,
            self.p116 if self.p116 is not None else 9.9,
            self.p117 if self.p117 is not None else 9.9,
            self.p118 if self.p118 is not None else 9.9,
            self.p119 if self.p119 is not None else 9.9,
            self.p120 if self.p120 is not None else 9.9,
            self.p121 if self.p121 is not None else 9.9,
            self.p122 if self.p122 is not None else 9.9,
            self.p123 if self.p123 is not None else 9.9,
            self.p124 if self.p124 is not None else 9.9,
            self.p125 if self.p125 is not None else 9.9,
            self.p126 if self.p126 is not None else 9.9,
            self.p127 if self.p127 is not None else 9.9,
            self.p128 if self.p128 is not None else 9.9,
        ]

    def training(self):
        functions.extract_facial_points(self)

    class Meta:
        ordering = ["person__name"]
        verbose_name = "photo"
        verbose_name_plural = "photos"

    def __str__(self) -> str:
        return str(self.uuid)

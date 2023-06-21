from django.apps import apps
from django.conf import settings
from django.db import connection
from recognizer.exceptions import TrainingErrorException

import cv2
import dlib
import numpy as np
import os

recognizer_path = apps.get_app_config("recognizer").path
face_detector = dlib.get_frontal_face_detector()
points_detector = dlib.shape_predictor(
    f"{recognizer_path}/dlib/shape_predictor_68_face_landmarks.dat"
)
face_recognizer = dlib.face_recognition_model_v1(
    f"{recognizer_path}/dlib/dlib_face_recognition_resnet_model_v1.dat"
)


def extract_facial_points(person_photo):
    image = cv2.imread(person_photo.file.path)
    detected_faces = face_detector(image, 2)
    num_faces = len(detected_faces)

    if num_faces > 1:
        person_photo.processed_error = True
        person_photo.save()
        raise TrainingErrorException(
            f"More than one face detected in this file {person_photo.file.name}"
        )

    elif num_faces < 1:
        person_photo.processed_error = True
        person_photo.save()
        raise TrainingErrorException(
            f"No face detected in this file {person_photo.file.name}"
        )

    else:
        facial_points = points_detector(image, detected_faces[0])
        descriptor = face_recognizer.compute_face_descriptor(image, facial_points)
        descriptor_list = [df for df in descriptor]
        descriptor_array = np.asarray(descriptor_list, dtype=np.float64)
        points = descriptor_array

        person_photo.p001 = points[0]
        person_photo.p002 = points[1]
        person_photo.p003 = points[2]
        person_photo.p004 = points[3]
        person_photo.p005 = points[4]
        person_photo.p006 = points[5]
        person_photo.p007 = points[6]
        person_photo.p008 = points[7]
        person_photo.p009 = points[8]
        person_photo.p010 = points[9]
        person_photo.p011 = points[10]
        person_photo.p012 = points[11]
        person_photo.p013 = points[12]
        person_photo.p014 = points[13]
        person_photo.p015 = points[14]
        person_photo.p016 = points[15]
        person_photo.p017 = points[16]
        person_photo.p018 = points[17]
        person_photo.p019 = points[18]
        person_photo.p020 = points[19]
        person_photo.p021 = points[20]
        person_photo.p022 = points[21]
        person_photo.p023 = points[22]
        person_photo.p024 = points[23]
        person_photo.p025 = points[24]
        person_photo.p026 = points[25]
        person_photo.p027 = points[26]
        person_photo.p028 = points[27]
        person_photo.p029 = points[28]
        person_photo.p030 = points[29]
        person_photo.p031 = points[30]
        person_photo.p032 = points[31]
        person_photo.p033 = points[32]
        person_photo.p034 = points[33]
        person_photo.p035 = points[34]
        person_photo.p036 = points[35]
        person_photo.p037 = points[36]
        person_photo.p038 = points[37]
        person_photo.p039 = points[38]
        person_photo.p040 = points[39]
        person_photo.p041 = points[40]
        person_photo.p042 = points[41]
        person_photo.p043 = points[42]
        person_photo.p044 = points[43]
        person_photo.p045 = points[44]
        person_photo.p046 = points[45]
        person_photo.p047 = points[46]
        person_photo.p048 = points[47]
        person_photo.p049 = points[48]
        person_photo.p050 = points[49]
        person_photo.p051 = points[50]
        person_photo.p052 = points[51]
        person_photo.p053 = points[52]
        person_photo.p054 = points[53]
        person_photo.p055 = points[54]
        person_photo.p056 = points[55]
        person_photo.p057 = points[56]
        person_photo.p058 = points[57]
        person_photo.p059 = points[58]
        person_photo.p060 = points[59]
        person_photo.p061 = points[60]
        person_photo.p062 = points[61]
        person_photo.p063 = points[62]
        person_photo.p064 = points[63]
        person_photo.p065 = points[64]
        person_photo.p066 = points[65]
        person_photo.p067 = points[66]
        person_photo.p068 = points[67]
        person_photo.p069 = points[68]
        person_photo.p070 = points[69]
        person_photo.p071 = points[70]
        person_photo.p072 = points[71]
        person_photo.p073 = points[72]
        person_photo.p074 = points[73]
        person_photo.p075 = points[74]
        person_photo.p076 = points[75]
        person_photo.p077 = points[76]
        person_photo.p078 = points[77]
        person_photo.p079 = points[78]
        person_photo.p080 = points[79]
        person_photo.p081 = points[80]
        person_photo.p082 = points[81]
        person_photo.p083 = points[82]
        person_photo.p084 = points[83]
        person_photo.p085 = points[84]
        person_photo.p086 = points[85]
        person_photo.p087 = points[86]
        person_photo.p088 = points[87]
        person_photo.p089 = points[88]
        person_photo.p090 = points[89]
        person_photo.p091 = points[90]
        person_photo.p092 = points[91]
        person_photo.p093 = points[92]
        person_photo.p094 = points[93]
        person_photo.p095 = points[94]
        person_photo.p096 = points[95]
        person_photo.p097 = points[96]
        person_photo.p098 = points[97]
        person_photo.p099 = points[98]
        person_photo.p100 = points[99]
        person_photo.p101 = points[100]
        person_photo.p102 = points[101]
        person_photo.p103 = points[102]
        person_photo.p104 = points[103]
        person_photo.p105 = points[104]
        person_photo.p106 = points[105]
        person_photo.p107 = points[106]
        person_photo.p108 = points[107]
        person_photo.p109 = points[108]
        person_photo.p110 = points[109]
        person_photo.p111 = points[110]
        person_photo.p112 = points[111]
        person_photo.p113 = points[112]
        person_photo.p114 = points[113]
        person_photo.p115 = points[114]
        person_photo.p116 = points[115]
        person_photo.p117 = points[116]
        person_photo.p118 = points[117]
        person_photo.p119 = points[118]
        person_photo.p120 = points[119]
        person_photo.p121 = points[120]
        person_photo.p122 = points[121]
        person_photo.p123 = points[122]
        person_photo.p124 = points[123]
        person_photo.p125 = points[124]
        person_photo.p126 = points[125]
        person_photo.p127 = points[126]
        person_photo.p128 = points[127]

        person_photo.processed = True
        person_photo.save()


def sql_face_search(image_file, in_memory_file=False, after_remove=True):
    if in_memory_file:
        image = cv2.imdecode(
            np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED
        )
    else:
        file = f"{settings.MEDIA_ROOT}/{image_file}"
        image = cv2.imread(file)
    detected_faces = face_detector(image, 2)

    identified_persons = []

    for face in detected_faces:
        e, t, d, b = (  # noqa: F841
            int(face.left()),
            int(face.top()),
            int(face.right()),
            int(face.bottom()),
        )
        facial_points = points_detector(image, face)
        descriptor = face_recognizer.compute_face_descriptor(image, facial_points)
        descriptor_list = list(descriptor)

        points = np.asarray(descriptor_list, dtype=np.float64)

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT person_id, cube_distance(
                cube(
                    array[
                        p001, p002, p003, p004, p005, p006, p007, p008, p009, p010,
                        p011, p012, p013, p014, p015, p016, p017, p018, p019, p020,
                        p021, p022, p023, p024, p025, p026, p027, p028, p029, p030,
                        p031, p032, p033, p034, p035, p036, p037, p038, p039, p040,
                        p041, p042, p043, p044, p045, p046, p047, p048, p049, p050,
                        p051, p052, p053, p054, p055, p056, p057, p058, p059, p060,
                        p061, p062, p063, p064, p065, p066, p067, p068, p069, p070,
                        p071, p072, p073, p074, p075, p076, p077, p078, p079, p080,
                        p081, p082, p083, p084, p085, p086, p087, p088, p089, p090,
                        p091, p092, p093, p094, p095, p096, p097, p098, p099, p100,
                        p101, p102, p103, p104, p105, p106, p107, p108, p109, p110,
                        p111, p112, p113, p114, p115, p116, p117, p118, p119, p120,
                        p121, p122, p123, p124, p125, p126, p127, p128
                ]),

                cube(
                    array[
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s
                    ])
                ) as distancia FROM recognizer_personphoto
                WHERE
                    p001 NOTNULL OR p002 NOTNULL OR p003 NOTNULL OR p004 NOTNULL OR p005 NOTNULL OR p006 NOTNULL OR p007 NOTNULL OR p008 NOTNULL OR p009 NOTNULL OR p010 NOTNULL OR
                    p011 NOTNULL OR p012 NOTNULL OR p013 NOTNULL OR p014 NOTNULL OR p015 NOTNULL OR p016 NOTNULL OR p017 NOTNULL OR p018 NOTNULL OR p019 NOTNULL OR p020 NOTNULL OR
                    p021 NOTNULL OR p022 NOTNULL OR p023 NOTNULL OR p024 NOTNULL OR p025 NOTNULL OR p026 NOTNULL OR p027 NOTNULL OR p028 NOTNULL OR p029 NOTNULL OR p030 NOTNULL OR
                    p031 NOTNULL OR p032 NOTNULL OR p033 NOTNULL OR p034 NOTNULL OR p035 NOTNULL OR p036 NOTNULL OR p037 NOTNULL OR p038 NOTNULL OR p039 NOTNULL OR p040 NOTNULL OR
                    p041 NOTNULL OR p042 NOTNULL OR p043 NOTNULL OR p044 NOTNULL OR p045 NOTNULL OR p046 NOTNULL OR p047 NOTNULL OR p048 NOTNULL OR p049 NOTNULL OR p050 NOTNULL OR
                    p051 NOTNULL OR p052 NOTNULL OR p053 NOTNULL OR p054 NOTNULL OR p055 NOTNULL OR p056 NOTNULL OR p057 NOTNULL OR p058 NOTNULL OR p059 NOTNULL OR p060 NOTNULL OR
                    p061 NOTNULL OR p062 NOTNULL OR p063 NOTNULL OR p064 NOTNULL OR p065 NOTNULL OR p066 NOTNULL OR p067 NOTNULL OR p068 NOTNULL OR p069 NOTNULL OR p070 NOTNULL OR
                    p071 NOTNULL OR p072 NOTNULL OR p073 NOTNULL OR p074 NOTNULL OR p075 NOTNULL OR p076 NOTNULL OR p077 NOTNULL OR p078 NOTNULL OR p079 NOTNULL OR p080 NOTNULL OR
                    p081 NOTNULL OR p082 NOTNULL OR p083 NOTNULL OR p084 NOTNULL OR p085 NOTNULL OR p086 NOTNULL OR p087 NOTNULL OR p088 NOTNULL OR p089 NOTNULL OR p090 NOTNULL OR
                    p091 NOTNULL OR p092 NOTNULL OR p093 NOTNULL OR p094 NOTNULL OR p095 NOTNULL OR p096 NOTNULL OR p097 NOTNULL OR p098 NOTNULL OR p099 NOTNULL OR p100 NOTNULL OR
                    p101 NOTNULL OR p102 NOTNULL OR p103 NOTNULL OR p104 NOTNULL OR p105 NOTNULL OR p106 NOTNULL OR p107 NOTNULL OR p108 NOTNULL OR p109 NOTNULL OR p110 NOTNULL OR
                    p111 NOTNULL OR p112 NOTNULL OR p113 NOTNULL OR p114 NOTNULL OR p115 NOTNULL OR p116 NOTNULL OR p117 NOTNULL OR p118 NOTNULL OR p119 NOTNULL OR p120 NOTNULL OR
                    p121 NOTNULL OR p122 NOTNULL OR p123 NOTNULL OR p124 NOTNULL OR p125 NOTNULL OR p126 NOTNULL OR p127 NOTNULL OR p128 NOTNULL

                ORDER BY
                    cube(
                        array[
                            p001, p002, p003, p004, p005, p006, p007, p008, p009, p010,
                            p011, p012, p013, p014, p015, p016, p017, p018, p019, p020,
                            p021, p022, p023, p024, p025, p026, p027, p028, p029, p030,
                            p031, p032, p033, p034, p035, p036, p037, p038, p039, p040,
                            p041, p042, p043, p044, p045, p046, p047, p048, p049, p050,
                            p051, p052, p053, p054, p055, p056, p057, p058, p059, p060,
                            p061, p062, p063, p064, p065, p066, p067, p068, p069, p070,
                            p071, p072, p073, p074, p075, p076, p077, p078, p079, p080,
                            p081, p082, p083, p084, p085, p086, p087, p088, p089, p090,
                            p091, p092, p093, p094, p095, p096, p097, p098, p099, p100,
                            p101, p102, p103, p104, p105, p106, p107, p108, p109, p110,
                            p111, p112, p113, p114, p115, p116, p117, p118, p119, p120,
                            p121, p122, p123, p124, p125, p126, p127, p128
                        ])
                    <->
                    cube(
                        array[
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s
                        ])
                    LIMIT 10;
                """,
                [
                    points[0],
                    points[1],
                    points[2],
                    points[3],
                    points[4],
                    points[5],
                    points[6],
                    points[7],
                    points[8],
                    points[9],
                    points[10],
                    points[11],
                    points[12],
                    points[13],
                    points[14],
                    points[15],
                    points[16],
                    points[17],
                    points[18],
                    points[19],
                    points[20],
                    points[21],
                    points[22],
                    points[23],
                    points[24],
                    points[25],
                    points[26],
                    points[27],
                    points[28],
                    points[29],
                    points[30],
                    points[31],
                    points[32],
                    points[33],
                    points[34],
                    points[35],
                    points[36],
                    points[37],
                    points[38],
                    points[39],
                    points[40],
                    points[41],
                    points[42],
                    points[43],
                    points[44],
                    points[45],
                    points[46],
                    points[47],
                    points[48],
                    points[49],
                    points[50],
                    points[51],
                    points[52],
                    points[53],
                    points[54],
                    points[55],
                    points[56],
                    points[57],
                    points[58],
                    points[59],
                    points[60],
                    points[61],
                    points[62],
                    points[63],
                    points[64],
                    points[65],
                    points[66],
                    points[67],
                    points[68],
                    points[69],
                    points[70],
                    points[71],
                    points[72],
                    points[73],
                    points[74],
                    points[75],
                    points[76],
                    points[77],
                    points[78],
                    points[79],
                    points[80],
                    points[81],
                    points[82],
                    points[83],
                    points[84],
                    points[85],
                    points[86],
                    points[87],
                    points[88],
                    points[89],
                    points[90],
                    points[91],
                    points[92],
                    points[93],
                    points[94],
                    points[95],
                    points[96],
                    points[97],
                    points[98],
                    points[99],
                    points[100],
                    points[101],
                    points[102],
                    points[103],
                    points[104],
                    points[105],
                    points[106],
                    points[107],
                    points[108],
                    points[109],
                    points[110],
                    points[111],
                    points[112],
                    points[113],
                    points[114],
                    points[115],
                    points[116],
                    points[117],
                    points[118],
                    points[119],
                    points[120],
                    points[121],
                    points[122],
                    points[123],
                    points[124],
                    points[125],
                    points[126],
                    points[127],
                    points[0],
                    points[1],
                    points[2],
                    points[3],
                    points[4],
                    points[5],
                    points[6],
                    points[7],
                    points[8],
                    points[9],
                    points[10],
                    points[11],
                    points[12],
                    points[13],
                    points[14],
                    points[15],
                    points[16],
                    points[17],
                    points[18],
                    points[19],
                    points[20],
                    points[21],
                    points[22],
                    points[23],
                    points[24],
                    points[25],
                    points[26],
                    points[27],
                    points[28],
                    points[29],
                    points[30],
                    points[31],
                    points[32],
                    points[33],
                    points[34],
                    points[35],
                    points[36],
                    points[37],
                    points[38],
                    points[39],
                    points[40],
                    points[41],
                    points[42],
                    points[43],
                    points[44],
                    points[45],
                    points[46],
                    points[47],
                    points[48],
                    points[49],
                    points[50],
                    points[51],
                    points[52],
                    points[53],
                    points[54],
                    points[55],
                    points[56],
                    points[57],
                    points[58],
                    points[59],
                    points[60],
                    points[61],
                    points[62],
                    points[63],
                    points[64],
                    points[65],
                    points[66],
                    points[67],
                    points[68],
                    points[69],
                    points[70],
                    points[71],
                    points[72],
                    points[73],
                    points[74],
                    points[75],
                    points[76],
                    points[77],
                    points[78],
                    points[79],
                    points[80],
                    points[81],
                    points[82],
                    points[83],
                    points[84],
                    points[85],
                    points[86],
                    points[87],
                    points[88],
                    points[89],
                    points[90],
                    points[91],
                    points[92],
                    points[93],
                    points[94],
                    points[95],
                    points[96],
                    points[97],
                    points[98],
                    points[99],
                    points[100],
                    points[101],
                    points[102],
                    points[103],
                    points[104],
                    points[105],
                    points[106],
                    points[107],
                    points[108],
                    points[109],
                    points[110],
                    points[111],
                    points[112],
                    points[113],
                    points[114],
                    points[115],
                    points[116],
                    points[117],
                    points[118],
                    points[119],
                    points[120],
                    points[121],
                    points[122],
                    points[123],
                    points[124],
                    points[125],
                    points[126],
                    points[127],
                ],
            )

            result = cursor.fetchall()

            for identify in result:
                accuracy = (1 - identify[1]) * 100
                from recognizer.models import Person

                person = Person.objects.get(pk=identify[0])

                if accuracy > 50:
                    # e, t, d, b
                    person_find = {
                        "person": person,
                        "accuracy": f"{round(accuracy, 2)}",
                        # "esq": e,
                        # "dir": d,
                        # "top": t,
                        # "bot": b
                    }

                    exist = any(
                        person == identified["person"]
                        for identified in identified_persons
                    )
                    if not exist:
                        identified_persons.append(person_find)

        if not in_memory_file and os.path.exists(file) and after_remove:
            os.remove(file)

    return identified_persons

def month(month, Lang="ru"):
    d = {
        "ru": [
            "������", "�������", "����",
            "������", "���", "����",
            "����", "������", "��������",
            "�������", "������", "�������"
        ],
        "en": [
            "January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"
        ]
    }
    return d[Lang][month - 1]
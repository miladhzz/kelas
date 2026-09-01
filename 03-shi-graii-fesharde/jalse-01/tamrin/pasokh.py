"""
پاسخ تمرین جلسه ۱ — فقط برای مدرس
این فایل را به شاگردان ندهید.
"""


class Teacher:
    tedad_kol = 0

    def __init__(self, name, reshte):
        self.name = name
        self.reshte = reshte
        self.kelas_ha = []
        Teacher.tedad_kol += 1

    def moarefi(self):
        print(f"من {self.name} هستم و رشته {self.reshte} تدریس می‌کنم.")

    def ezafe_kelas(self, nam_kelas):
        self.kelas_ha.append(nam_kelas)

    @classmethod
    def namayesh_tedad_kol(cls):
        print(f"تعداد کل معلم‌ها: {cls.tedad_kol}")


if __name__ == "__main__":
    m1 = Teacher("علی", "پایتون")
    m2 = Teacher("مریم", "جاوا")

    m1.moarefi()
    m2.moarefi()

    m1.ezafe_kelas("پایتون مقدماتی")
    m1.ezafe_kelas("شی‌گرایی فشرده")

    print(f"کلاس‌های {m1.name}: {m1.kelas_ha}")
    print(f"کلاس‌های {m2.name}: {m2.kelas_ha}")

    Teacher.namayesh_tedad_kol()

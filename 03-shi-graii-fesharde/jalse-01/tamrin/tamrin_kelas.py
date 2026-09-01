"""
تمرین جلسه ۱ — شی‌گرایی فشرده
کلاس Teacher (معلم) را کامل کنید.
"""


class Teacher:
    # TODO: یک class attribute به نام tedad_kol بسازید (مقدار اولیه: 0)
    # این attribute تعداد کل معلم‌های ساخته‌شده را نگه می‌دارد

    def __init__(self, name, reshte):
        # TODO: name و reshte را به عنوان instance attribute ذخیره کنید
        # TODO: یک لیست خالی برای kelas_ha (کلاس‌هایی که معلم تدریس می‌کند) بسازید
        # TODO: tedad_kol را یکی زیاد کنید
        pass

    def moarefi(self):
        # TODO: یک جمله چاپ کنید، مثلاً:
        # "من علی هستم و رشته پایتون تدریس می‌کنم."
        pass

    def ezafe_kelas(self, nam_kelas):
        # TODO: نام کلاس را به لیست kelas_ha اضافه کنید
        # نکته: از متغیر محلی به‌جای instance attribute استفاده نکنید!
        pass

    @classmethod
    def namayesh_tedad_kol(cls):
        # این متد را لمس نکنید — برای تست است
        print(f"تعداد کل معلم‌ها: {cls.tedad_kol}")


# --- تست (بعد از کامل کردن، این بخش باید درست کار کند) ---
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

# تمرین: مدیریت نمرات دانش‌آموز
# هدف: تمرین لیست، ایندکس، pop، شرط، عملگرهای ریاضی و منطقی

# TODO 1: یک لیست خالی به نام scores بسازید
scores = None

# TODO 2: سه نمره از کاربر بگیرید (عدد صحیح) و به لیست اضافه کنید
s1 = int(input("First score: "))
# TODO: s1 را با append به scores اضافه کنید

s2 = int(input("Second score: "))
# TODO: s2 را با append به scores اضافه کنید

s3 = int(input("Third score: "))
# TODO: s3 را با append به scores اضافه کنید

# TODO 3: طول لیست را با len چاپ کنید
print("Number of scores:", None)

# TODO 4: ایندکس نمره‌ای که می‌خواهید حذف کنید را بگیرید و به int تبدیل کنید
index_str = input("Index of score to remove (0 to 2): ")
index = None  

# TODO 5: شرط بررسی ایندکس معتبر (index >= 0 and index < len(scores))
if None:
    # TODO 6: با pop(index) نمره را حذف و در removed ذخیره کنید
    removed = None
    print("Score removed:", removed)
    print("Current list:", scores)
else:
    print("Invalid index")
    # pass  # می‌توانید از pass استفاده کنید

# TODO 7: اگر طول لیست دقیقاً 2 بود، میانگین دو نمره باقی‌مانده را حساب کنید
if len(scores) == 2:
    # TODO 8: مجموع دو نمره را با + حساب کنید
    total = None 
    # TODO 9: میانگین را حساب کنید (total تقسیم بر 2)
    average = None

    # TODO 10: اگر میانگین >= 10 بود "Passed" وگرنه "Failed" چاپ کنید
    if None:
        print("Result: Passed")
    else:
        print("Result: Failed")
else:
    print("Average not calculated due to invalid index.")

# TODO 11: از کاربر بپرسید آیا می‌خواهید آخرین نمره را حذف کنید؟ (yes/no)
answer = input("Remove last score? (yes/no): ")

# TODO 12: اگر answer برابر "yes" بود و لیست خالی نبود، آخرین عنصر را با pop حذف کنید
# اگر answer برابر "yes" بود و لیست خالی بود، پیام "List is empty, nothing to remove" بدهید
# در غیر این صورت "No removal performed" چاپ کنید
if answer == "yes" and None:
    removed_last = None  # TODO: pop بدون آرگومان
    print("Last score removed:", removed_last)
    print("Final list:", scores)
elif answer == "yes" and None:
    print("List is empty, nothing to remove")
else:
    print("No removal performed")
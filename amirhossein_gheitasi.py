from tkinter import *
from tkinter import messagebox
import json

product_list = []
count = 0


def save_product():
    global count
    try:
        # دریافت مقادیر از فرم
        product_name = name.get()
        product_quantity = quantity.get()
        product_price = price.get()

        # اعتبارسنجی
        if not product_name:
            messagebox.showerror("خطا", "لطفاً نام محصول را وارد کنید")
            return

        if product_quantity <= 0:
            messagebox.showerror("خطا", "مقدار باید بزرگتر از صفر باشد")
            return

        if product_price <= 0:
            messagebox.showerror("خطا", "قیمت باید بزرگتر از صفر باشد")
            return

        # ذخیره محصول
        product = {
            'name': product_name,
            'quantity': product_quantity,
            'price': product_price
        }

        product_list.append(product)
        count += 1
        count_label.config(text=f"count={count}")

        # نمایش پیام موفقیت
        messagebox.showinfo("ذخیره شد", "محصول با موفقیت ذخیره شد")

        # چاپ لیست در کنسول
        print(json.dumps(product_list, indent=2, ensure_ascii=False))

        # پاک کردن فرم
        name.set("")
        quantity.set(1)
        price.set(1)

    except Exception as e:
        messagebox.showerror("خطا", f"مشکل در ذخیره اطلاعات:\n{str(e)}")


# ایجاد پنجره اصلی
window = Tk()
window.title("سیستم ثبت محصول")
window.geometry("250x280")

# متغیرهای فرم
name = StringVar()
quantity = IntVar(value=1)
price = IntVar(value=1)

# ویجت‌های فرم
Label(window, text='name').place(x=20, y=20)
Entry(window, textvariable=name).place(x=80, y=20)

Label(window, text='quantity').place(x=20, y=60)
Entry(window, textvariable=quantity).place(x=80, y=60)

Label(window, text='price').place(x=20, y=100)
Entry(window, textvariable=price).place(x=80, y=100)

count_label = Label(window, text='count=0')
count_label.place(x=80, y=150)

Button(window, text='save', width=10, command=save_product).place(x=80, y=180)

window.mainloop()
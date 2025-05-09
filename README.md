# ATM_App

This project is a simulation of an ATM (Automated Teller Machine) built using Python and PyQt6.  
It allows users to log in, choose language (English or Persian), and perform basic banking operations.

## Features

- 🔐 User Login Page
- 🌐 Language Selection (English / فارسی)
- 💵 Get Cash (predefined amounts)
- 🔄 Money Transfer (with validation)
- 🔒 Change Password
- 📊 Account Balance Display
- ✅ Done Page with restart/exit options
- 🌍 Multilingual support using `QTranslator`

## Technologies Used

- Python 3
- PyQt6
- Object-Oriented Programming (OOP)

## توضیحات تکمیلی
اول از همه در صفحه ی اول یک login page  تعریف کردم،اگر باکس ها را خالی بگزاریم یک مسیج باکس باز میشود که در آن پیام هشدار است.
در صغحه دوم میتوانیم زبانی که میخواهیم با آن کارمان را ادامه دهیم انتخاب کنیم که من دیفالت زبان برنامم رو انگلیسی گزاشتم.
در این کد از فلش های back and forward  استفاده کردم که کاربر بتواند به راحتی در تمام صفحات حرکت کند.
در صفحه س MainAtm چهار کار اصلی و ساده ای که کاربر میتواند با atm  انجام دهد آمده است مثل برداشت وجه، تغییر رمز عبور، کارت به کارت کردن و موجودی حساب را چک کند آمده است
با استفاده از گزینه ی برداشت وجه کاربر میتواند مبلغ پیشنهادی را انتخاب کنه و به صفحه بعد برود و با انتخاب گزینه  goodby  برنامه و کار ماربر تمام شود و یا با انتخاب  back to menu  به صفحه  MainAtm برود
در گزینه ی کارت به کارت کردن کاربر باید یک شماره حساب 16 رقمی وارد کند، اگر کمتر از 16 عدد وارد کند یا از حروف به جای عدد و یا در قسمت مبلغ از اعداد منفی استفاده کند پیام هشدار میگیرد در غیر اینصورت پیاک موفقیت در یک مسیچ باکس برای کاربر نمایش داده میشود
در قسمت موجودی حساب هم برای کاربر یک موجودی ثابت تعریف کردیم که با کیلیک کردن بر روی آن گزینه میتواند موجودی حساب خود را ببیند.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/heliakrd/ATM_App.git
   cd ATM_App

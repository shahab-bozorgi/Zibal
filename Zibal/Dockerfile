FROM python:3.12-slim

WORKDIR /app

# کپی فایل requirements.txt به داخل کانتینر
COPY ./requirements/requirements.txt /app/

# نصب پکیج‌ها از requirements.txt
RUN pip install --no-cache-dir --no-deps -r /app/requirements.txt

# نصب نسخه خاص gunicorn
RUN pip install gunicorn==23.0.0

# بروز رسانی pip
RUN pip install --upgrade pip

# پاکسازی کش pip
RUN pip cache purge

# تنظیمات پایتون برای جلوگیری از نوشتن فایل‌های bytecode و buffer کردن خروجی
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# کپی کردن باقی‌مانده فایل‌ها به داخل کانتینر
COPY . /app/

# پورت 8000 را برای استفاده از gunicorn در نظر می‌گیریم
EXPOSE 8000

# اجرای اپلیکیشن با gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Zibal.wsgi:application"]

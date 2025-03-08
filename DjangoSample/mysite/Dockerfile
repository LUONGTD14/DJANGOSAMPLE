# Python image
FROM python:3.10.5

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép toàn bộ mã nguồn vào container
COPY . /app/

# install requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port cho Django
EXPOSE 8000

# run migrate to update database and run server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

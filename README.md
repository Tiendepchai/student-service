# **Service Quản Lý Sinh Viên (Student Service)**  

Dịch vụ này sẽ quản lý thông tin sinh viên với các tính năng chính:  
- **Tạo sinh viên mới**  
- **Lấy danh sách sinh viên**  
- **Lấy thông tin một sinh viên cụ thể**  
- **Cập nhật thông tin sinh viên**  
- **Xóa sinh viên**  

## **Công nghệ sử dụng**
- **Flask**: Xây dựng API RESTful  
- **Flask-SQLAlchemy**: ORM để làm việc với database  
- **Marshmallow**: Validate dữ liệu  
- **MySQL hoặc PostgreSQL**: Lưu trữ dữ liệu  
- **Docker**: Đóng gói service  

## **Cấu trúc thư mục**
```
student_service/
│── app.py                  # Main Flask App
│── config.py               # Cấu hình MySQL
│── database.py             # Kết nối MySQL
│── models.py               # Định nghĩa bảng Student
│── routes.py               # Xử lý API endpoints
│── requirements.txt        # Thư viện cần thiết
│── .gitignore        # Thư viện cần thiết
│── Dockerfile              # (Nếu deploy bằng Docker)
└── .env                    # Config biến môi trường
```
---

## **1. Cài đặt môi trường**  
Trước tiên, hãy tải về thư mục dự án:  
```sh
git clone https://github.com/Tiendepchai/student-service.git
```
Tạo một môi trường ảo và cài đặt Flask:  
```sh
pip install -r requirements.txt
```

---

## **2. Các API**
Dưới đây là cấu trúc **dịch vụ quản lý sinh viên**.

### **File: `app.py`**
Chứa API Flask và khởi tạo database.
---

### **File: `models.py`**
Chứa model **Student**.
---

### **File: `schemas.py`**
Dùng **Marshmallow** để validate dữ liệu.
---

### **File: `resources/student.py`**
---

## **3. Chạy Dịch Vụ**
### **Bước 1: Tạo Database**
Chạy MySQL và tạo database:
```sh
sudo -u root
```
```sql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON student_db.* TO 'admin'@'localhost';
CREATE DATABASE student_db;
```

### **Bước 2: Chạy API**
```sh
python app.py
```
API sẽ chạy tại `http://127.0.0.1:5000`.

---

## **4. Kiểm thử API với cURL hoặc Postman**
#### **Tạo sinh viên mới**
```sh
curl -X POST http://127.0.0.1:5000/students -H "Content-Type: application/json" -d '{
  "name": "Nguyen Van A",
  "email": "nguyenvana@example.com",
  "age": 20,
  "major": "Computer Science"
}'
```

#### **Lấy danh sách sinh viên**
```sh
curl http://127.0.0.1:5000/students
```

#### **Lấy thông tin sinh viên theo ID**
```sh
curl http://127.0.0.1:5000/students/1
```

#### **Cập nhật sinh viên**
```sh
curl -X PUT http://127.0.0.1:5000/students/1 -H "Content-Type: application/json" -d '{
  "name": "Nguyen Van B",
  "email": "nguyenvanb@example.com",
  "age": 21,
  "major": "Mathematics"
}'
```

#### **Xóa sinh viên**
```sh
curl -X DELETE http://127.0.0.1:5000/students/1
```

---

## **5. Đóng gói với Docker**
### **File: `Dockerfile`**
```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

### **File: `docker-compose.yml`**
```yaml
version: '3.10'
services:
  student_service:
    build: .
    ports:
      - "5000:5000"
    environment:
      - SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:password@db/student_db
    depends_on:
      - db

  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: student_db
      MYSQL_USER: admin
      MYSQL_PASSWORD: password
    ports:
      - "3306:3306"
```

### **Chạy Docker**
```sh
docker-compose up --build
```
---

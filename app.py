from flask import Flask
from routes import student_bp
from models import create_student_table

app = Flask(__name__)

# Tạo bảng nếu chưa có
create_student_table()

# Đăng ký blueprint
app.register_blueprint(student_bp)

if __name__ == '__main__':
    app.run(debug=True)

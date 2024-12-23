## Sistem Pengiriman Barang, Makanan, dan Pengantaran Orang

Selamat datang di repositori Sistem Pengiriman!

Sistem ini dirancang menggunakan Python dengan antarmuka grafis berbasis PyQt5 untuk mempermudah pengelolaan dan pelacakan layanan pengiriman barang, makanan, serta pengantaran orang. 
Dengan fitur modern dan desain antarmuka yang ramah pengguna, aplikasi ini cocok digunakan oleh admin maupun pelanggan.

## Technology Used 
<div style="display: flex; justify-content: center; align-items: center; gap: 20px; margin: 0 auto; text-align: center;">
    <img src="desain/pythoon.png" alt="HTML" style="width: 50px; height: 50px; object-fit: cover; border: none; background: none; border-radius: 8px;">
    <img src="desain/mysql.png" alt="CSS" style="width: 50px; height: 50px; object-fit: cover; border: none; background: none; border-radius: 8px;">
</div>

## Installation
Follow these steps to run the application on your device:

1. Clone this repository:

    git clone https://github.com/Fanzirfan27/Project-Sistem-Pengiriman.git<br>
    cd Project-Sistem-Pengiriman <br>

2. Create a virtual environment (optional but recommended):

    python -m venv env <br>
    source env/bin/activate # For MacOS/Linux <br>
    env\Scripts\activate   # For Windows <br>

3. Install dependencies:

    pip install pyqt5 pyqt5-tools pandas mysql-connector-python <br>

4. Configure the database:

    Ensure MySQL is installed.<br>
    Import the db_sistem_pengiriman.sql file into MySQL to create the database structure.<br>

5. Run the application:
   
    python main.py

import os
import socket
from flask import Flask, send_from_directory

app = Flask(__name__)

# Statik dosyaları sun (index.html ve diğerleri)
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

if __name__ == '__main__':
    ip = get_local_ip()
    print("="*50)
    print(f"[*] OYUN SERVERI BASLATILIYOR...")
    print(f"[*] Senin Adresin: https://{ip}:5000")
    print(f"(!) DIKKAT: Tarayici 'Guvenli Degil' diyebilir.")
    print(f"    'Gelismis' -> 'Siteye Ilerle' (Proceed) demeniz lazim.")
    print("="*50)
    
    # Ad-hoc SSL (Basit HTTPS)
    # pip install pyopenssl gerekebilir, yoksa hata verebilir.
    try:
        app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
    except Exception as e:
        print("\n❌ HTTPS Başlatılamadı (pyopenssl eksik olabilir).")
        print("📲 HTTP olarak başlatılıyor (Mikrofon çalışmayabilir!)")
        print(f"🏠 Adres: http://{ip}:5000")
        print("="*50)
        app.run(host='0.0.0.0', port=5000)

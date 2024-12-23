import math

def hitung_jarak(lat1, lon1, lat2, lon2):
    # Konversi derajat ke radian
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # Radius bumi dalam kilometer
    R = 6371
    # Perbedaan koordinat
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # Rumus haversine
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    jarak = R * c
    return jarak  # Hasil dalam kilometer
def hitung_pengiriman_barang(jarak, berat, jumlah, tarif_kg, tarif_unit, tarif_km, diskon):
    biaya_jarak = jarak * tarif_km
    total = (berat * tarif_kg + jumlah * tarif_unit + biaya_jarak) - diskon
    return max(total, 0)
def hitung_pengiriman_makanan(jarak, jumlah, tarif_per_makanan, tarif_km, diskon):
    biaya_jarak = jarak * tarif_km
    total = (jumlah * tarif_per_makanan + biaya_jarak) - diskon
    return max(total, 0)
def hitung_pengiriman_orang(jarak, kategori, tarif_bike, tarif_car, tarif_km, diskon):
    tarif_kategori = tarif_bike if kategori == 'bike' else tarif_car
    biaya_jarak = jarak * tarif_km
    total = (tarif_kategori + biaya_jarak) - diskon
    return max(total, 0)


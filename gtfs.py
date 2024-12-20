import pandas as pd
import os
import json

# A mappa elérési útja
gtfs_folder = r"C:\Users\User\Downloads\gtfsMavMenetrend"

# A GTFS fájlok betöltése
files = ['feed_info.txt', 'shapes.txt', 'calendar.txt', 'stop_times.txt', 'agency.txt', 'routes.txt', 'stops.txt', 'trips.txt']

data = {}

for file in files:
    file_path = os.path.join(gtfs_folder, file)
    if os.path.exists(file_path):
        # Betöltjük a fájlt pandas DataFrame-be és konvertáljuk dictionary-vé
        df = pd.read_csv(file_path)
        data[file] = df.to_dict('records')  # 'records' format will give us a list of dictionaries
    else:
        print(f"Fájl nem található: {file_path}")

# Adatok tárolása JSON fájlba
json_output_path = r"C:\Users\User\Downloads\gtfs_data.json"
with open(json_output_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Az adatok JSON formátumban elmentve: {json_output_path}")
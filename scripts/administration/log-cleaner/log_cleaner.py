import os
import time

def clean_logs(directory, days):
    # Zeit in Sekunden umrechnen
    seconds = days * 24 * 60 * 60
    current_time = time.time()

    if not os.path.exists(directory):
        print("Verzeichnis nicht gefunden.")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Prüfen, ob es eine Datei ist und auf .log endet
        if os.path.isfile(file_path) and file.endswith(".log"):
            file_age = os.path.getmtime(file_path)
            
            if current_time - file_age > seconds:
                os.remove(file_path)
                print(f"Gelöscht: {file}")

if __name__ == "__main__":
    print("--- Log-File Cleaner ---")
    path = input("Pfad zum Log-Ordner: ")
    age = int(input("Lösche Dateien älter als (Tage): "))
    clean_logs(path, age)

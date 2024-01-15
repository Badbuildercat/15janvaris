import csv

def nolasit(csv_fails):
    try:
        with open(csv_fails, 'r', newline='') as fails:
            csvLasitajs = csv.reader(fails)
            print("Otras kolonnas dati:")
            for rindina in csvLasitajs:
                if len(rindina) > 1:  
                    print(rindina[1]) 
    except FileNotFoundError:
        print(f"Kluda: fails '{csv_fails}' nav atrasts.")
    except Exception as e:
        print(f"Kluda: {e}")

nolasit("dati.csv")

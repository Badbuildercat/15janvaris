def nolasit(fails):
    try:
        with open(fails, 'r') as fails:
            rindas = fails.readlines()
            if len(rindas) >= 3:
                print("Tresas rindas saturs:")
                print(rindas[2])
                print(f"Kluda: fails '{fails}' satur mazak par 3 rindām.")
    except FileNotFoundError:
        print(f"Kluda: fails '{fails}' nav atrasts.")
    except Exception as e:
        print(f"Kluda: {e}")

nolasit("texts2.txt")

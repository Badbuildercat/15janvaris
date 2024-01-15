def nolasit():
    try:
        fails_nosaukums = input("faila nosaukumu: ")
        paplasinajums = input("faila paplasinajumu: ")
        pilns_nosaukums = f"{fails_nosaukums}.{paplasinajums}"
        with open(pilns_nosaukums, 'r') as fails:
            saturs = fails.read()
            print(f"Faila '{pilns_nosaukums}' saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Kluda: fails '{pilns_nosaukums}' nav atrasts.")
    except PermissionError:
        print(f"Kluda: nav atlaujas lasit failu '{pilns_nosaukums}'.")
    except Exception as e:
        print(f"Kluda: {e}")

nolasit()
#cvs nestrādā nezinu kapēc
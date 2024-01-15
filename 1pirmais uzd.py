

def lasit(texts):
    try:
        with open(texts, 'r') as fails:  
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: fails '{texts}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")


lasit("texts.txt")
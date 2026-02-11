import json

input_file = 'lab_5.ipynb'
output_file = 'lab_5.ipynb'

try:
    print(f"Wczytuję plik: {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Sprawdzenie czy istnieje sekcja metadata
    if 'metadata' in notebook:
        # Sprawdzenie czy w metadata są widgets
        if 'widgets' in notebook['metadata']:
            print("ZNALEZIONO uszkodzoną sekcję 'widgets'. Usuwam tylko ją...")
            del notebook['metadata']['widgets']
            
            # Zapisz tylko jeśli dokonano zmiany
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, ensure_ascii=False, indent=1)
            print(f"SUKCES! Zapisano naprawiony plik jako: {output_file}")
            print("Twoje kody i wyniki pozostały nienaruszone.")
        else:
            print("Nie znaleziono sekcji 'widgets' w metadanych. Plik wygląda na czysty pod tym względem.")
    else:
        print("Błąd struktury pliku: brak pola 'metadata'.")

except FileNotFoundError:
    print(f"Błąd: Nie widzę pliku '{input_file}'. Upewnij się, że skrypt jest w tym samym folderze.")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")
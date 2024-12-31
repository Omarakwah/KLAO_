from number_simplifier import simplify_numbers

def run_test_cases():
    test_cases = [
        "324.620,22 Euro wurden gespendet.",
        "1.897 Menschen nahmen teil.",
        "25 Prozent der Bevölkerung sind betroffen.",
        "90 Prozent stimmten zu.",
        "14 Prozent lehnten ab.",
        "Bei 38,7 Grad Celsius ist es sehr heiß.",
        "denn die Rente steigt um 4,57 Prozent.",
        "Im Jahr 2024 gab es 1.234 Ereignisse.",
        "Am 1. Januar 2024 waren es 5.678 Teilnehmer.",
        "Im Jahr 2025 gab es 2018 Ereignisse."
    ]

    for test in test_cases:
        print(simplify_numbers(test))

if __name__ == "__main__":
    run_test_cases()
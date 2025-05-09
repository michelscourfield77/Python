import math

def evaluer_expression(expr):
    variables_autorisees = {
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'log': math.log,
        'pi': math.pi,
        'e': math.e,
        '__builtins__': {}
    }
    return eval(expr, variables_autorisees)

# Code exécutable directement
if __name__ == "__main__":
    expression = "2 + 3 * sqrt(4)"  # Une expression de test
    resultat_attendu = evaluer_expression(expression)

    # Simulation d'un résultat utilisateur
    resultat_obtenu = 8.0

    # Calcul de l'écart (delta)
    delta = resultat_attendu - resultat_obtenu

    # Logique 1 (ajustement basé sur l'écart)
    if delta < 0:
        correction = resultat_obtenu - abs(delta)
    else:
        correction = resultat_obtenu + delta

    # --- Affichage complet ---
    print("--- Analyse du premier calcul ---")
    print(f"Expression posée : {expression}")
    print(f"Résultat attendu : {resultat_attendu}")
    print(f"Résultat obtenu : {resultat_obtenu}")
    print(f"Δ (Écart) = {delta}")
    print(f"Correction : {resultat_obtenu} {'+' if delta >= 0 else '-'} {abs(delta)} = {correction}")

    # --- Logique 2 (ajustement pour retrouver le bon résultat) ---
    print("\n--- Analyse du deuxième calcul ---")
    print(f"Résultat obtenu (de la logique 1) : {resultat_obtenu}")
    print(f"Écart Δ : {delta}")
    print("\n--- Calcul de la logique 2 ---")
    print("Nous réutilisons l'écart Δ de la logique 1 :", delta)
    print(f"Résultat attendu (logique 2) = {resultat_obtenu} + ({delta})")
    resultat_attendu_logique2 = resultat_obtenu + delta
    print(f"Résultat attendu pour la logique 2 : {resultat_attendu_logique2}")





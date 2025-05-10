import math

def evaluer_expression(expr):
    # Environnement sécurisé
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

def calculer_ecart_et_correction(resultat_obtenu, resultat_attendu):
    ecart = resultat_obtenu - resultat_attendu
    correction = resultat_obtenu - ecart
    return ecart, correction

# --- Programme principal ---

expression = input("Entrez une expression mathématique (ex : 2 + 3 * 4 - sqrt(9)) : ")
resultat_attendu = evaluer_expression(expression)

resultat_obtenu = float(input("Quel résultat as-tu obtenu ? "))

# --- Logique 1 ---
delta = resultat_attendu - resultat_obtenu

# Correction basée sur l'écart
if delta < 0:
    correction = resultat_obtenu - abs(delta)
else:
    correction = resultat_obtenu + delta

# --- Affichage de la logique 1 ---
print("\n--- Analyse du premier calcul ---")
print(f"Expression posée : {expression}")
print(f"Résultat attendu : {resultat_attendu}")
print(f"Résultat obtenu : {resultat_obtenu}")
print(f"Δ (Écart) = {delta}")
print(f"Correction : {resultat_obtenu} {'+' if delta >= 0 else '-'} {abs(delta)} = {correction}")

# --- Logique 2 ---
print("\n--- Analyse du deuxième calcul ---")
print(f"Résultat obtenu (de la logique 1) : {resultat_obtenu}")
print(f"Écart Δ : {delta}")

# Calcul logique 2
resultat_attendu_logique2 = resultat_obtenu + delta

print("\n--- Calcul de la logique 2 ---")
print("Nous réutilisons l'écart Δ de la logique 1 :", delta)
print(f"Résultat obtenu (de la logique 1) : {resultat_obtenu}")
print(f"Calcul du résultat attendu pour la logique 2 :")
print(f"Résultat attendu = Résultat obtenu + Δ")
print(f"Résultat attendu = {resultat_obtenu} + ({delta})")
print(f"Résultat attendu = {resultat_attendu_logique2}")

print("\nLogique 1 : Voici ce qui était correct, voici ce que vous avez fait, et voici l'erreur.")
print("Logique 2 : Voici l'erreur que vous avez faite, en partant de votre réponse, voici comment on revient à la bonne réponse.")



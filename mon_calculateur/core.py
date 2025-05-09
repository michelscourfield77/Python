# mon_calculateur/core.py

from math import sqrt

def analyser_expression(expression: str, resultat_attendu: float):
    try:
        resultat_obtenu = eval(expression, {"sqrt": sqrt})
        delta = abs(resultat_attendu - resultat_obtenu)
        print(f"Expression posée : {expression}")
        print(f"Résultat attendu : {resultat_attendu}")
        print(f"Résultat obtenu : {resultat_obtenu}")
        print(f"Δ (Écart) = {delta}")
        print(f"Correction : {resultat_attendu} + {delta} = {resultat_attendu + delta}")
    except Exception as e:
        print("Erreur :", e)

# Si lancé directement, demande une saisie utilisateur
if __name__ == "__main__":
    expr = input("Entrez une expression mathématique : ")
    res = float(input("Entrez le résultat attendu : "))
    analyser_expression(expr, res)







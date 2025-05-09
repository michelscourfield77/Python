
import math

def evaluer_expression(expr: str) -> float:
    """
    Évalue une expression mathématique de manière sécurisée.
    Paramètres :
        expr (str) : L'expression mathématique à évaluer.
    Retour :
        float : Le résultat de l'évaluation.
    """
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

def calculer_ecart_et_correction(resultat_attendu: float, resultat_obtenu: float) -> tuple:
    """
    Calcule l'écart (delta) entre deux résultats et propose une correction.
    Paramètres :
        resultat_attendu (float) : Le bon résultat.
        resultat_obtenu (float) : Le résultat saisi par l'utilisateur.
    Retour :
        tuple : (delta, correction)
    """
    delta = resultat_attendu - resultat_obtenu
    if delta < 0:
        correction = resultat_obtenu - abs(delta)
    else:
        correction = resultat_obtenu + delta
    return delta, correction



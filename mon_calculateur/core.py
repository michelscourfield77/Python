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
    
    print(f"Expression : {expression}")
    print(f"Résultat attendu : {resultat_attendu}")







# Mon Calculateur

Un petit module Python pour évaluer des expressions mathématiques et analyser les erreurs de calcul.

## Exemple d'utilisation

```python
from mon_calculateur.core import evaluer_expression, calculer_ecart_et_correction

expr = "2 + 3 * sqrt(4)"
résultat = evaluer_expression(expr)
print("Résultat :", résultat)




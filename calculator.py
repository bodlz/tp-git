"""Ce module fournit des fonctions de base pour les opérations mathématiques."""

def addition(number_a, number_b):
    """Retourne la somme de number_a et number_b."""
    return number_a + number_b

def soustraction(number_a, number_b):
    """Retourne la différence entre number_a et number_b."""
    return number_a - number_b

def division(number_a, number_b):
    """Retourne le résultat de la division de number_a par number_b.

    Lève une erreur si number_b est zéro.
    """
    if number_b == 0:
        raise ValueError("Le diviseur ne peut pas être zéro.")
    return number_a / number_b

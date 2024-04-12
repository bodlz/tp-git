"""Module de test pour vérifier les fonctions du module calculator."""

# Imports des fonctions depuis le module calculator
from calculator import addition, soustraction, division

def test_addition():
    """Teste la fonction addition avec des entiers positifs."""
    assert addition(1, 2) == 3

def test_soustraction():
    """Teste la fonction soustraction avec des entiers positifs."""
    assert soustraction(5, 2) == 3

def test_division():
    """Teste la fonction division avec des entiers positifs."""
    assert division(10, 2) == 5

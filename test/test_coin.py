from src.coin import Coin
from pytest import approx

def test_coin():
    c = Coin()
    assert isinstance(c, Coin)
    assert c.states == ['H', 'T']

def test_flip():
    c = Coin()
    assert c.flip() in c.states

def test_fair_coin():
    c = Coin()
    outcomes = []
    for i in range (100_000):
        outcomes.append(c.flip())
    assert (outcomes.count('H')/ 100_000) == approx (0.50, rel=1e-2)
from prime_sh4432 import is_prime
def test_is_prime():
    prime_numbers=[2,7,13,19]
    composite_numbers=[8,9,15]
    for prime in prime_numbers:
        assert is_prime(prime), f"{prime} is not recognized as prime."
    for composite in composite_numbers:
        assert not is_prime(composite), f"{composite} is recognized as prime, but it's composite."
    print("Tests passed.")
    

from collections import namedtuple
from typing import NamedTuple, cast
import unittest

# Note how Z=0 and A=1
alphabet = "ZABCDEFGHIJKLMNOPQRSTUVWXY"

# Size of the finite field
m = len(alphabet)

# A smarter algorithm would be
# https://en.wikipedia.org/wiki/Itoh%E2%80%93Tsujii_inversion_algorithm
# However, but I think for the purposes of this exercise, this should suffice :)
def find_inverse(c: int) -> int | None:
    for i in range(10000000):
        if (c * i) % m == 1:
            return i
    return None

# Multiplicative inverses of 0..25 modulo 26
# inverses = [find_inverse(c) for c in range(m)]
inverses: list[int | None] = [None, 1, None, 9, None, 21, None, 15, None, 3, None, 19, None, None, None, 7, None, 23, None, 11, None, 5, None, 17, None, 25]

class Key:
    a: int
    b: int
    
    def __init__(self, a, b):
        if a < 0 or a >= m:
            raise ValueError("a must be in the range 0..25")
        if b < 0 or b >= m:
            raise ValueError("b must be in the range 0..25")
        if inverses[a] is None:
            raise ValueError("a must have a multiplicative inverse")

        self.a = a
        self.b = b

def encrypt(message: str, key: Key) -> list[int]:
    indices = [alphabet.find(c) for c in message]
    assert all(i >= 0 for i in indices) # str.find returns -1 if the character is not found
    return [(key.a * i + key.b) % m for i in indices]
    
def decrypt(ciphertext: list[int], key: Key) -> str:
    inv_a = cast(int, inverses[key.a])
    inv_b = m - key.b
    return "".join(alphabet[inv_a * (c + inv_b) % m] for c in ciphertext)

class Test(unittest.TestCase):
    def encrypt_decrypt(self, message: str, key: Key):
        ciphertext = encrypt(message, key)
        self.assertEqual(decrypt(ciphertext, key), message)
        
    def test_inverse(self):
        self.assertEqual(1, cast(int, inverses[3]) * 3 % m)
    
    """
    Check that all found inverses are actually inverses
    """
    def test_inverses(self):
        self.assertNotIn(False, (t[0] * t[1] % m == 1 for t in zip(inverses, range(m)) if t[0] is not None))
        
    def test_encrypt_a(self):
        self.assertEqual([8, 5, 12, 12, 15], encrypt("HELLO", Key(1, 0)))
    
    def test_encrypt_decrypt_b(self):
        key = Key(1, 5)
        self.encrypt_decrypt("HELLO", key)
        self.encrypt_decrypt("WORLD", key)
        self.encrypt_decrypt("GOODBYE", key)
    
    def test_encrypt_decrypt_a(self):
        key = Key(3, 0)
        self.encrypt_decrypt("HELLO", key)
        self.encrypt_decrypt("WORLD", key)
        self.encrypt_decrypt("GOODBYE", key)
    
    def test_encrypt_decrypt_extra(self):
        self.encrypt_decrypt("ITSECURITY", Key(11, 9))
        self.encrypt_decrypt("CRYPTOGRAPHY", Key(7, 3))
        self.encrypt_decrypt("ENCRYPTION", Key(5, 7))
        
    def test_reject_invalid_keys_a(self):
        self.assertRaises(ValueError, Key, 0, 0)
        self.assertRaises(ValueError, Key, 2, 0)
        self.assertRaises(ValueError, Key, 8, 0)
    
    def test_reject_invalid_keys_b(self):
        self.assertRaises(ValueError, Key, 1, -1)
        self.assertRaises(ValueError, Key, 1, 27)
        self.assertRaises(ValueError, Key, -1, 0)
        
    def test_reject_invalid_messages(self):
        key = Key(1, 5)
        self.assertRaises(AssertionError, encrypt, "HELLO!", key)
        self.assertRaises(AssertionError, encrypt, "hello", key)
        self.assertRaises(AssertionError, encrypt, " ", key)
        
    def test_allow_empty_message(self):
        key = Key(1, 5)
        self.assertEqual("", decrypt(encrypt("", key), key))

if __name__ == '__main__':
    unittest.main()

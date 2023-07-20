import unittest


def generate_prime_numbers(limit):
    primes = []
    for num in range(2, limit+1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes


def check_email(email):
    return '@' in email

class Test(unittest.TestCase):
    def test_generate_prime_numbers(self):
        result = generate_prime_numbers(10)
        self.assertEqual(result, [2, 3, 5, 7])

    def test_check_email(self):
        self.assertTrue(check_email('mail@mail.com'))
        self.assertFalse(check_email('mail.com'))
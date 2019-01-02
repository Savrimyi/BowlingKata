import unittest


def run_tests():
    tests = unittest.TestLoader().discover('.', pattern='Test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    run_tests()

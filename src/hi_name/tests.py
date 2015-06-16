import sys
import unittest


class HiTest(unittest.TestCase):

    def test_hi(self):

        # triggers any file output
        import hi_name 
        
        output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
        
        self.assertIn('hi, ', output, 'Try again')


if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)

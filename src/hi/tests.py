import sys
import unittest


class HiTest(unittest.TestCase):

    def test_hi(self):

        # triggers any file output
        import hi 
        
        output = sys.stdout.getvalue().strip() # because stdout is an StringIO instance
        
        self.assertEqual(output,'hi')


if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)

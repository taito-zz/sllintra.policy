from sllintra.policy.setuphandlers import setupVarious

import unittest
import mock


class TestCase(unittest.TestCase):
    """Test case for function: setupVarious"""

    def test(self):
        context = mock.Mock()
        context.readDataFile.return_value = None
        self.assertIsNone(setupVarious(context))

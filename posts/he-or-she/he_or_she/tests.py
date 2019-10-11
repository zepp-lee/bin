import unittest

import numpy as np

from he_or_she import *


class HeOrSheFeatureUnionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.titles = [
            "City of angels versus city of light",
            "Does glamour of the Globes steal the scene from Oscar?",
            "Industry likes the look as more men moisturize",
            "Beach Reads That Can Improve Your Game",
        ]

    def test(self):
        actual = HeOrSheFeatureUnion().transform(self.titles)
        expected = np.array([
            [35, 6],
            [54, 9],
            [46, 7],
            [38, 6],
        ])
        self.assertTrue(np.array_equal(actual, expected))
#!/usr/bin/env python3
"""
    Test xkcd1930 Implementation
    ============================
"""

import logging
import sys
import unittest as ut

sys.path.append("..")

import xkcd1930

logging.basicConfig(level = logging.ERROR)


class test_setup(ut.TestCase):
    NotImplemented


class test_main(ut.TestCase):
    NotImplemented


class test_Xkcd1930(ut.TestCase):
    def setUp(self):
        xkcd1930.setup()
        self.tester = xkcd1930.Xkcd1930()
        self.tester.statement = ""


    def test_generate_image(self):
        self.tester.statement = None # Reset original state
        self.assertFalse(self.tester.generate_image())


    def test_generate_statement(self):
        self.tester.generate_statement()
        self.assertTrue(isinstance(self.tester.statement, str))
        self.assertTrue("?" in self.tester.statement)
        self.assertTrue(self.tester.statement.endswith("."))
        self.assertTrue(self.tester.statement.startswith("Did you know that"))


    def block_appending_methods_test_auxiliary_call(
        self,
        block_appending_method: "method",
        possible_results: tuple,
    ):
        """This method performs subtests for a provided block-appending-method and a tuple of possible
        outcomes.

        Since the block-appending-methods' behavior is intrinsically random, we run the method several
        times and verify that the generated block is among the expected outcomes. We repeat the call
        often enough to *hope* for all options to be generated at least once (no guarantee).

        :param block_appending_method: Instance block-appending-method, usually some self.tester.$method
        :param possible_results: All possible outcomes to be expected by the block-appending-method
        """
        for ii in range(10 * len(possible_results)):
            self.tester.statement = ""
            block_appending_method()
            with self.subTest(i = ii, msg = f"{ii} {self.tester.statement}"):
                self.assertTrue(self.tester.statement in possible_results)


    def test_append_first_block(self):
        possible_results = (
            "the fall equinox ",
            "the spring equinox ",
            "the winter solstice ",
            "the winter Olympics ",
            "the summer solstice ",
            "the summer Olympics ",
            "the earliest sunrise ",
            "the earliest sunset ",
            "the latest sunrise ",
            "the latest sunset ",
            "the harvest moon ",
            "the super moon ",
            "the blood moon ",
            "daylight saving time ",
            "daylight savings time ",
            "leap year ",
            "leap day ",
            "Easter ",
            "Toyota Truck Month ",
            "Shark Week ",
        )
        self.block_appending_methods_test_auxiliary_call(
            self.tester.append_first_block, possible_results
        )


    def test_append_second_block(self):
        possible_results = (
            "happens earlier every year ",
            "happens later every year ",
            "happens at the wrong time every year ",
            "drifts out of sync with the sun ",
            "drifts out of sync with the moon ",
            "drifts out of sync with the zodiac ",
            "drifts out of sync with the Gregorian calendar ",
            "drifts out of sync with the Mayan calendar ",
            "drifts out of sync with the Lunar calendar ",
            "drifts out of sync with the iPhone calendar ",
            "drifts out of sync with the atomic clock in Colorado ",
            "might not happen this year ",
            "might happen twice this year ",
        )
        self.block_appending_methods_test_auxiliary_call(
            self.tester.append_second_block, possible_results
        )


    def test_append_third_block(self):
        possible_results = (
            "because of time zone legislation in Indiana? ",
            "because of time zone legislation in Arizona? ",
            "because of time zone legislation in Russia? ",
            "because of a decree by the Pope in the 1500s? ",
            "because of magnetic field reversal? ",
            "because of an arbitrary decision by Benjamin Franklin? ",
            "because of an arbitrary decision by Isaac Newton? ",
            "because of an arbitrary decision by FDR? ",
            "because of the precession of the Moon? ",
            "because of the precession of the Sun? ",
            "because of the precession of the Earth's axis? ",
            "because of the precession of the equator? ",
            "because of the precession of the prime meridian? ",
            "because of the precession of the International Date Line? ",
            "because of the precession of the Mason-Dixon Line? ",
            "because of the libration of the Moon? ",
            "because of the libration of the Sun? ",
            "because of the libration of the Earth's axis? ",
            "because of the libration of the equator? ",
            "because of the libration of the prime meridian? ",
            "because of the libration of the International Date Line? ",
            "because of the libration of the Mason-Dixon Line? ",
            "because of the nutation of the Moon? ",
            "because of the nutation of the Sun? ",
            "because of the nutation of the Earth's axis? ",
            "because of the nutation of the equator? ",
            "because of the nutation of the prime meridian? ",
            "because of the nutation of the International Date Line? ",
            "because of the nutation of the Mason-Dixon Line? ",
            "because of the libation of the Moon? ",
            "because of the libation of the Sun? ",
            "because of the libation of the Earth's axis? ",
            "because of the libation of the equator? ",
            "because of the libation of the prime meridian? ",
            "because of the libation of the International Date Line? ",
            "because of the libation of the Mason-Dixon Line? ",
            "because of the eccentricity of the Moon? ",
            "because of the eccentricity of the Sun? ",
            "because of the eccentricity of the Earth's axis? ",
            "because of the eccentricity of the equator? ",
            "because of the eccentricity of the prime meridian? ",
            "because of the eccentricity of the International Date Line? ",
            "because of the eccentricity of the Mason-Dixon Line? ",
            "because of the obliquity of the Moon? ",
            "because of the obliquity of the Sun? ",
            "because of the obliquity of the Earth's axis? ",
            "because of the obliquity of the equator? ",
            "because of the obliquity of the prime meridian? ",
            "because of the obliquity of the International Date Line? ",
            "because of the obliquity of the Mason-Dixon Line? ",
        )
        self.block_appending_methods_test_auxiliary_call(
            self.tester.append_third_block, possible_results
        )


    def test_append_fourth_block(self):
        possible_results = (
            "Apparently it causes a predictable increase in car accidents.",
            "Apparently that's why we have leap seconds.",
            "Apparently scientists are really worried.",
            "Apparently it was even more extreme during the Bronze Age.",
            "Apparently it was even more extreme during the Ice Age.",
            "Apparently it was even more extreme during the Cretaceous.",
            "Apparently it was even more extreme during the 1990s.",
            "Apparently there's a proposal to fix it, but it will never happen.",
            "Apparently there's a proposal to fix it, but it actually makes things worse.",
            "Apparently there's a proposal to fix it, but it is stalled in Congress.",
            "Apparently there's a proposal to fix it, but it might be unconstitutional.",
            "Apparently it's getting worse and no one knows why.",
        )
        self.block_appending_methods_test_auxiliary_call(
            self.tester.append_fourth_block, possible_results
        )


    def test_add_choice_to_statement(self):
        OPTION = "Same options"
        self.tester.add_choice_to_statement((OPTION, OPTION))
        self.assertEqual(self.tester.statement, OPTION)


    def test_initiate_block(self):
        POOL = ("Block start ",)
        cr = self.tester.initiate_block(POOL)
        self.assertEqual(self.tester.statement, POOL[0])
        self.assertEqual(cr, 0)

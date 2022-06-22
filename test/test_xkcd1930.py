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


    def test_generate_image(self):
        tester = xkcd1930.Xkcd1930()
        self.assertFalse(tester.generate_image())


    def test_generate_statement(self):
        NotImplemented


    def test_append_first_block(self):
        NotImplemented


    def test_append_second_block(self):
        NotImplemented


    def test_append_third_block(self):
        NotImplemented


    def test_append_fourth_block(self):
        NotImplemented


    def test_add_choice_to_statement(self):
        tester = xkcd1930.Xkcd1930()
        tester.statement = ""
        OPTION = "Same options"
        tester.add_choice_to_statement((OPTION, OPTION))
        self.assertEqual(tester.statement, OPTION)


    def test_initiate_block(self):
        POOL = ("Block start ",)
        tester = xkcd1930.Xkcd1930()
        tester.statement = ""
        cr = tester.initiate_block(POOL)
        self.assertEqual(tester.statement, POOL[0])
        self.assertEqual(cr, 0)

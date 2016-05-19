#!/usr/bin/env python{{ options.py_version }}
# -*- coding: utf-8 -*

import unittest
{% set module_name = options.package_name.lower() %}

from {{module_name}} import *

{% set class_name = options.package_name.capitalize() %}


class {{class_name}}TestCase(unittest.TestCase):

    def test_empty(self):
        raise Exception("Not implemented")


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase({{class_name}}TestCase))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

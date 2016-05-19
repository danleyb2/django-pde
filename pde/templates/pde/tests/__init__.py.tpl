""" {{ options.package_name }}/__init__.py """
# -*- coding: utf-8 -*

{% set module_name = options.package_name.lower() %}
from . import test_{{module_name}}


def suite():
    import unittest
    suite = unittest.TestSuite()
    suite.addTests(test_{{module_name}}.suite())

    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

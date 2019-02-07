#!/usr/bin/env python

import unittest


class VSphereAnsibleTestCase(unittest.TestCase):

    def test_list_inventory(self):
        from vsphere_inventory import VSphere
        self.assertTrue(getattr(VSphere, 'list_inventory'))
        self.assertTrue(callable(getattr(VSphere, 'list_inventory')))

    def test_append_vm_info(self):
        from vsphere_inventory import VSphere
        self.assertTrue(hasattr(VSphere, 'append_vm_info'))
        self.assertTrue(callable(getattr(VSphere, 'append_vm_info')))

    def test_filter_inventory(self):
        from vsphere_inventory import VSphere
        self.assertTrue(hasattr(VSphere, 'filter_inventory'))
        self.assertTrue(callable(getattr(VSphere, 'filter_inventory')))

    def test_grouped_inventory(self):
        from vsphere_inventory import VSphere
        self.assertTrue(hasattr(VSphere, 'grouped_inventory'))
        self.assertTrue(callable(getattr(VSphere, 'grouped_inventory')))

    def test_list_and_save(self):
        from vsphere_inventory import VSphere
        self.assertTrue(hasattr(VSphere, 'list_and_save'))
        self.assertTrue(callable(getattr(VSphere, 'list_and_save')))

    def test_cached_inventory(self):
        from vsphere_inventory import VSphere
        self.assertTrue(hasattr(VSphere, 'cached_inventory'))
        self.assertTrue(callable(getattr(VSphere, 'cached_inventory')))


if __name__ == '__main__':
    unittest.main()

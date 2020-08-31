import unittest
import InventoryAllocator as ia


class Test(unittest.TestCase):

    # test both empty inputs
    def test_1(self):
        self.assertEqual(ia.InventoryAllocator().get_cheapest_shipment({}, []), [])

    # test empty list of warehouses
    def test_2(self):
        self.assertEqual(ia.InventoryAllocator().get_cheapest_shipment({'apple': 1}, []), [])

    # test empty order
    def test_3(self):
        self.assertEqual(ia.InventoryAllocator().get_cheapest_shipment({}, [
            {'name': 'a', 'inventory': {'apple': 1}},
        ]), [])

    # test single warehouse with enough inventory
    def test_4(self):
        self.assertEqual(ia.InventoryAllocator().get_cheapest_shipment({'apple': 1}, [
            {'name': 'a', 'inventory': {'apple': 1}},
        ]), [{'a': {'apple': 1}}])

    # test single ware house without enough inventory
    def test_5(self):
        self.assertEqual(ia.InventoryAllocator().get_cheapest_shipment({'apple': 2}, [
            {'name': 'a', 'inventory': {'apple': 1}}
        ]), [])

    # test multiple warehouses with enough inventory but must split order across warehouses
    def test_6(self):
        self.assertEqual(ia.InventoryAllocator().get_cheapest_shipment({'apple': 5}, [
            {'name': 'a', 'inventory': {'apple': 2}},
            {'name': 'b', 'inventory': {'apple': 2}},
            {'name': 'c', 'inventory': {'apple': 2}}
        ]), [{'a': {'apple': 2}}, {'b': {'apple': 2}}, {'c': {'apple': 1}}])

    # test multiple warehouses without enough inventory 
    def test_7(self):
        self.assertEqual(ia.InventoryAllocator().get_cheapest_shipment({'apple': 3}, [
            {'name': 'a', 'inventory': {'apple': 1}},
            {'name': 'b', 'inventory': {'apple': 1}}
        ]), [])

    # more complex order with multiple items and multiple warehouses. Able to ship if split across warehouses 
    def test_8(self):
        self.assertEqual(ia.InventoryAllocator().get_cheapest_shipment({'apple': 3, 'orange': 3, 'banana': 3}, [
            {'name': 'a', 'inventory': {'apple': 1, 'orange': 1, 'banana': 1}},
            {'name': 'b', 'inventory': {'banana': 2, 'orange': 1}},
            {'name': 'c', 'inventory': {'apple': 3, 'orange': 2}}
        ]), [{'a': {'apple': 1, 'orange': 1, 'banana': 1}}, {'b': {'orange': 1, 'banana': 2}}, {'c': {'apple': 2, 'orange': 1}}])

    # more complex order with multiple items and multiple warehouses, but not enough inventory
    def test_9(self):
        self.assertEqual(ia.InventoryAllocator().get_cheapest_shipment({'apple': 3, 'orange': 3, 'banana': 3}, [
            {'name': 'a', 'inventory': {'apple': 1, 'orange': 1, 'banana': 1}},
            {'name': 'b', 'inventory': {'banana': 2, 'orange': 1}},
            {'name': 'c', 'inventory': {'apple': 3, 'orange': 0}}
        ]), [])


if __name__ == '__main__':
    unittest.main()

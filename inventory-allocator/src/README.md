## Deliverr Coding Challenge

### Raymond Lin's solution
Language: Python 3

I implemented the InventoryAllocator class and solved the challenge in the get_cheapest_shipment method

In the get_cheapest_shipment method I took a greedy algorithm approach where I would iterate each order and then iterate through the list of warehouses which is known to be sorted by cost. By iterating in order through the warehouses I can guarantee that the resulting shipment will be the cheapest.

If there is enough of every item across all the warehouses to fulfill the order, then the output of the method is a list of the warehouses and the amounts of each product that will be shipped. If the order cannot be fulfilled fully, then the output is an empty list.

### Unit Tests

I wrote 9 unit tests which test cases including:

- empty inputs
- a single warehouse without enough inventory
- multiple warehouses with/without enough inventory

To run the unit tests run `python test.py` in the inventory-allocator/src directory
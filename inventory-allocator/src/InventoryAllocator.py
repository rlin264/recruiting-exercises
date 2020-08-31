class InventoryAllocator():
    '''
    Inventory Allocator static class
    Contains the get_chepest_shipment method which satisfies the requirements of the challenge
    '''

    def get_cheapest_shipment(self, order, warehouses):
        '''
        Output the cheapest shipment given an order and a list of warehouse inventories 
        (presorted based on shipment cost).

        :param order: dictionary containing products and quatities
        :param warehouse: list of warehouses (dictionaries with name and inventory)

        :return list containing the resulting shipment from each warehouse sorted by warehouse name
        the list is the in the format: 
        [{'warehouse1':{item1: (qty), item2: (qty) ...}}, {'warehouse2': {item1: (qty), item2: (qty) ...}} ...]
        '''
        cheapest_shipment =  {}
        
        # return an empty list if no order or no warehouse list
        if not order or not warehouses:
            return []

        # iterate through the products in the order
        for product in order:   
            # iterate through the warehouses from least expensive to most expensive
            for warehouse in warehouses:
                #check if there is a >0 qty of product in the warehouse inventory 
                if product in warehouse['inventory'] and warehouse['inventory'][product] > 0:
                    # find number of items taken from the warehouse inventory
                    items = min(warehouse['inventory'][product], order[product])

                    # if warehouse not in cheapest_shipment add it. Initialize with empty dict
                    if warehouse['name'] not in cheapest_shipment:
                        cheapest_shipment[warehouse['name']] = {}

                    # set number of items shipped from the warehouse
                    cheapest_shipment[warehouse['name']][product] = items

                    # subtract the items satisfied from the order
                    order[product] -= items

                    # if order satisfied
                    if order[product] == 0:
                        break
            
            # if order for the prodcut not satisfied then return an empty list
            if order[product] != 0:
                return []
        
        # create return list in specified format
        ret = []
        for warehouse,items in cheapest_shipment.items():
            ret.append({warehouse: items})
        
        # sort output list by the warehouse name
        ret = sorted(ret, key=lambda k: list(k.keys())[0]) 

        return ret

if __name__ == '__main__':
    IA = InventoryAllocator()
    # out = IA.get_cheapest_shipment({ 'apple': 2 }, [{ 'name': 'owd', 'inventory': { 'apple': 2 } }])
    out = IA.get_cheapest_shipment({'apple': 3, 'orange': 3, 'banana': 3}, [
            {'name': 'a', 'inventory': {'apple': 1, 'orange': 1, 'banana': 1}},
            {'name': 'b', 'inventory': {'banana': 2, 'orange': 1}},
            {'name': 'c', 'inventory': {'apple': 3, 'orange': 2}}
            ]
    )
    
    print(out)



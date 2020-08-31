from collections import OrderedDict
import json

class InventoryAllocator():
    '''
    Inventory Allocator class
    '''

    def get_cheapest_shipment(self, order, warehouses):
        cheapest_shipment =  OrderedDict()
        # print('order', order)
        if not order or not warehouses:
            return []

        for product in order:   
            # print('product', product)
            for warehouse in warehouses:
                # print(warehouse['inventory'])
                if product in warehouse['inventory'] and warehouse['inventory'][product] > 0:
                    items = min(warehouse['inventory'][product], order[product])

                    if warehouse['name'] not in cheapest_shipment:
                        cheapest_shipment[warehouse['name']] = {}

                    cheapest_shipment[warehouse['name']][product] = items
                    order[product] -= items
                    if order[product] == 0:
                        break
            
            if order[product] != 0:
                return []
        
        ret = []
        for warehouse,items in cheapest_shipment.items():
            ret.append({warehouse: items})
        
        return ret

if __name__ == '__main__':
    IA = InventoryAllocator()
    # out = IA.get_cheapest_shipment({ 'apple': 2 }, [{ 'name': 'owd', 'inventory': { 'apple': 2 } }])
    out = IA.get_cheapest_shipment({ 'apple': 10 }, 
        [{ 'name': 'owd', 'inventory': { 'apple': 4 } },
         { 'name': 'dm', 'inventory': { 'apple': 5 }}])
    
    print(out)



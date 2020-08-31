class InventoryAllocator():
    '''
    Inventory Allocator class
    '''

    def get_cheapest_shipment(self, order, warehouses):

        cheapest_shipment =  {}
        if not order or not warehouses:
            return []

        for product in order:   
            for warehouse in warehouses:
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



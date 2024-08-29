def fetch_order_details(order_detail_object):
    return {
        "product_id": order_detail_object["product_id"],
        "quantity": order_detail_object["quantity"],
        "total": order_detail_object["total"]
    }

def fetchone_document(order_object):
    return {
        'object_id' : str(order_object['_id']),
        'order_id' : order_object['order_id'],
        'user_id' : order_object['user_id'],
        'order_details' : [fetch_order_details(order_detail_object) for order_detail_object in order_object['order_details']]
    }

def fetchall(orders_list):
    return [fetchone_document(order_object) for order_object in orders_list]



#products

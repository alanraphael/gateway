def merge(exchanges, orders):
    for k, v in exchanges.items():
        v.pop('fees')
        v['order_book_stats'] = orders.get(k, {})

    return exchanges
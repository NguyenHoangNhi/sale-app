def load_categeries():
    return [{
        'id': 1,
        'name': 'mobile'
    },
        {
            'id': 2,
            'name': 'vina'
        }
    ]


def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'IPhone 1000 promax',
        'price': 5000,
        'image': 'https://cdn.tgdd.vn/Products/Images/42/250728/iphone-13-pro-max-xanh-la-thumb-600x600.jpg'
    },
        {
            'id': 2,
            'name': 'IPhone trẻ trung',
            'price': 500,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/250728/iphone-13-pro-max-xanh-la-thumb-600x600.jpg'
        },
        {
            'id': 3,
            'name': 'IPhone năng động',
            'price': 1000,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/250728/iphone-13-pro-max-xanh-la-thumb-600x600.jpg'
        },
        {
            'id': 3,
            'name': 'IPhone năng động',
            'price': 1000,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/250728/iphone-13-pro-max-xanh-la-thumb-600x600.jpg'
        },
        {
            'id': 3,
            'name': 'IPhone năng động',
            'price': 1000,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/250728/iphone-13-pro-max-xanh-la-thumb-600x600.jpg'
        },
        {
            'id': 3,
            'name': 'IPhone năng động',
            'price': 1000,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/250728/iphone-13-pro-max-xanh-la-thumb-600x600.jpg'
        },
        {
            'id': 3,
            'name': 'Samsung năng động',
            'price': 1000,
            'image': 'https://cdn.tgdd.vn/Products/Images/42/250728/iphone-13-pro-max-xanh-la-thumb-600x600.jpg'
        }
    ]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products

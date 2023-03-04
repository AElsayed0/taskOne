{
    'name': "taskOne",
    'version': '1.0',
    'depends': ['base','sale'],
    'author': "-",
    'category': '-',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/sale_order_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo_data.xml',
    ],
}
# -*- coding: utf-8 -*-
{
    'name': "Cafeupo",

    'summary': """Gestion de máquinas de café""",

    'description': """Gestion de las máquinas, productos, reparaciones, proveedores...""",

    'author': "TSI - UPO",
    'website': "https://www.upo.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'mrp'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/products_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [   
    ],
    'installable': True,
    'application': True,
}

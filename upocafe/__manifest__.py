# -*- coding: utf-8 -*-
{
    'name': "UPOCafe",

    'summary': """Gestion de máquinas de café""",

    'description': """Gestion de las máquinas, productos, reparaciones, proveedores...""",

    'author': "Marcos Villareal Muñoz, Antonio Moreno Mendez, Pablo Sanchez Troncoso, Antonio Garrido Massé",
    'website': "https://www.upo.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'mrp', 'hr', 'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/status_view.xml',
        'views/employee_view.xml',
        'views/machine_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [   
        'demo/demo_data.xml'
    ],
    'installable': True,
    'application': True,
}
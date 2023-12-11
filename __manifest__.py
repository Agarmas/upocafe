# -*- coding: utf-8 -*-
{
    'name': "UPOcafé",

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
        'reports/reports.xml',
        'reports/repositions_report.xml',
        'reports/providers_report.xml',
        'views/menu.xml',
        'views/clients_views.xml',
        'views/providers_views.xml',
        'views/products_views.xml',
        'views/payments_views.xml',
        'views/payment_methods_views.xml',
        'views/cancelations_views.xml',
        'views/machines_views.xml',
        'views/reparations_views.xml',
        'views/repositions_views.xml',
        'views/employees_views.xml',
        'views/status_views.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [   
        'demo/demo_data.xml',
    ],
    
    'installable': True,
    'application': True,
}

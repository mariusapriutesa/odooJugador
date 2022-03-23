# -*- coding: utf-8 -*-
{
    'name': "Proyecto jugadores",

    'summary': """
        En este modulo podemos designar diferentes jugadores
        """,

    'description': """
        Este modolo fue creado para gestionar los jugadores
    """,

    'author': "Marius Apriutesa",
    'website': "https://github.dev/mariusapriutesa/odooJugador",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       'security/jugador_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
     'application' : True ,
}

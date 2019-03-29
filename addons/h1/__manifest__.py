# -*- coding: utf-8 -*-
{
    'name': "Hosp M10-H1 PCNT",

    'summary': """
        Aplicació de gestió de pacients. H1""",

    'description': """
        Aplicació de gestió d'un Hospital. Gestió NOMÉS de pacients. H1
    """,

    'author': "cbm",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'M10',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'data/patient.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'application': True,
}

# -*- coding: utf-8 -*-
{
    'name': "Tasques CBM",

    'summary': """
        Aplicació de gestió de tasques""",

    'description': """
        Aplicació de gestió de tasquesssss. Aplicació de gestió de tasquesssss
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
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'data/todo.task.csv',
        'data/todo_task.xml',
	],
    # only loaded in demonstration mode
    'demo': [
        'data/todo.task.csv',
        'data/todo_task.xml',
    ],
    'application': True,
}

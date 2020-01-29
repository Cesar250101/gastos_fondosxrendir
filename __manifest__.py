# -*- coding: utf-8 -*-
{
    'name': "gastos_fondosxrendir",

    'summary': """
    Se crea una relación entre el empleado, el fondo por rendir y la rendición de gastos
                """,

    'description': """
        Se crea un campo many2one en los asientos contables donde estaran los empleados, este campo
        se mostrara cuando el diario tenga la marca de fondo por rendir
        Cuando el empleado este rindiendo los gastos se desplegara los fondos que esta pendientes de rendición
    """,

    'author': "Method",
    'website': "http://www.openmethod.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_expense'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
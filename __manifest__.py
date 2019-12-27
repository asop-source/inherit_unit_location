# -*- coding: utf-8 -*-
{
    'name': "vit unit location",

    'summary': """
        Inherit:
                project(project)
                purchase(purchase)
                stock.picking(inventory)
                uudp pengajuan(uudp)
                vendor bill(account)
                sales order(sales)
                invoice(account)
                HR.payslip(payrol)
                Jurnal entry(account)
                vit_relokasi_budget(vit_budegt_relok)
                vit_budget_cut(vit_budget)

        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "asopkarawang@gmail.com",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inherit',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','vit_employee_analytic','account','purchase','purchase_requisition',
            'vit_uudp','hr','stock','vit_bakn','vit_budget_relokasi','vit_budget_cut',],

    # always loaded
    'data': [
        'views/project.xml',
        'views/purchase_order_qoutation.xml',
        'views/purchase_requisition.xml',
        'views/sale_order.xml',
        'views/inventory_receipts.xml',
        'views/vendor_bill.xml',
        'views/customer_invoice.xml',
        'views/payroll_hr_payslip.xml',
        'views/jurnal_entry.xml',
        'views/vit_bakn_bakn.xml',
        'views/uudp_pengajuan.xml',
        'views/vit_relokasi_budget.xml',
        'views/vit_budget_cut.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
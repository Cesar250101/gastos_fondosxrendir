# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Diarios(models.Model):
    _inherit = 'account.journal'

    es_fondoxrendir = fields.Boolean(string="Es Fondo x Rendir?",  )

class Asientos(models.Model):
    _inherit = 'account.move'

    employee_id = fields.Many2one(comodel_name="hr.employee", string="Empleados", required=False, )
    es_fondoxrendir = fields.Boolean(string="Es Fondo x rendir", related="journal_id.es_fondoxrendir" )
    total_comprobante = fields.Integer(string="Total Comprobante",compute="_compute_amount" ,required=False, )

    @api.one
    @api.depends('line_ids')
    def _compute_amount(self):
        total=0
        for i in self.line_ids:
            total+=i.debit
        self.total_comprobante=total

class NewModule(models.Model):
    _inherit = 'hr.employee'

    fondos_pendientes = fields.One2many(comodel_name="account.move", inverse_name="employee_id", string="Fondos x Rendir", required=False, )

class NewModule(models.Model):
    _inherit = 'hr.expense'

    fondos_pendientes = fields.Many2many(comodel_name="account.move", relation="exp_acco_rel", column1="employee_id", column2="employe_id", string="Fondos x Rendir",)

class NewModule(models.Model):
    _inherit = 'hr.expense.sheet'

    fondos_pendientes = fields.Many2many(comodel_name="account.move", relation="exp_acco_rel", column1="employee_id", column2="employe_id", string="Fondos x Rendir",)


# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class technical_test_tunas(models.Model):
#     _name = 'technical_test_tunas.technical_test_tunas'
#     _description = 'technical_test_tunas.technical_test_tunas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

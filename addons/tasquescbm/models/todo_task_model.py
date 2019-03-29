# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char(help="What needs to be done?")
    is_done = fields.Boolean('Fet?')
    active = fields.Boolean('Activa?', default=True)
    date_deadline = fields.Date('Deadline')
    urgencia = fields.Char(string='Urgència', help="Urgència de la tasca?")
    user_id = fields.Many2one(
        'res.users',
        string='Responsable',
        default=lambda s: s.env.user)
    team_ids = fields.Many2many('res.partner', string='Equip')
    

    @api.multi
    def do_clear_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True



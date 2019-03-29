# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Pacient(models.Model):
    _name = 'h1.pacient'
    _order = 'cognom, nom'
    _rec_name = 'cognom'
    nom = fields.Char(help="Nom del pacient?", required=True)
    #Cognom del pacient
    cognom = fields.Char(size=50,string="Cognom", required=True, help="Cognom")
    #Genere
    genere = fields.Selection(string="Gènere", required=True , selection=[("H","Home"),("D","Dona"),("A","Altres")], help="[H/D/A]")
    #Dni
    dni = fields.Char(size=10,string="DNI", required=True, help="DNI: format [123456789A]")
    #Adreca
    adreca = fields.Char(string="Adreça", required=False, help="Adreça del pacient")
    #Nacionalitat
    nacionalitat = fields.Many2one('res.country', default=68, onDelete="cascade", required=True,help="Trieu la nacionalitat")
     #Data de naixement
    data_naixement = fields.Date(string="Data Naixement", required=False, help="Data Naixement [DD-MM-AAAA]")
    #Admissió
    ingres = fields.Boolean(string="Ingrés", default=False, help="Pacient ingressat?", readonly=True)
    #Data ingres
    data_ingres = fields.Date(string="Data Ingrés", help="Data Ingrés [DD-MM-AAAA]", default=fields.Date.today)
    #Informacio
    informacio = fields.Char(string="Informació", required=False, help="Informació extra")
    #Mutua
    asseguranca = fields.Char(string="Companyia asseguradora", required=False, help="Assegurança privada")

    _sql_constraints = [
        ('nom_cognom_check',
         'CHECK(nom != cognom)',
         "No i cognom han de ser diferents..."),

        ('dni_unique',
         'UNIQUE(dni)',
         "Aquest dni ja figura a la base de dades"),
    ]


# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

# class hospital_dam(models.Model):
#     _name = 'hospital_dam.hospital_dam'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class pacient(models.Model):
	
	_name = 'hospital_dam.pacient'
	_rec_name = 'cognom'
	_order = 'cognom'
	
	
	
	nom = fields.Char(required=True)
	cognom = fields.Char(required=True)
	genere = fields.Selection([('m','m'),('f','f')], required=True)
	dni = fields.Char(required=True)
	adreça = fields.Char()
	data = fields.Date()
	nacionalitat = fields.Many2one('res.country', required=True)
	ingres = fields.Boolean()
	ingres_data = fields.Date()
	info = fields.Text()
	assegurança = fields.Char()
	
	prova_ids = fields.One2many('h2.prova','pacient_id',string='Provas',required=True,help='Provas pacient')
	doctor_rel = fields.Many2many('h2.metge')
	
	nom_complet = fields.Char(compute='_nom_complet')
	num_doctor = fields.Integer(compute='_doctors')
				
	_sql_constraints = [
		('nom_cognom_check','CHECK(nom != cognom)',
		"Nom i cognom han de ser diferents..."),
		('dni_unique',
		'UNIQUE(dni)',"Aquest dni ja figura a la base de dades"),
	]
	
	@api.depends('nom','cognom')
	def _nom_complet(self):
		for record in self:
			if (record.nom and record.cognom):
				record.nom_complet = record.nom + " " + record.cognom
	
	@api.depends('doctor_rel')
	def _doctors(self):
		num = 0
		for record in self:
			for metge in record.doctor_rel:
				num += 1
			record.num_doctor = num
			num = 0 
	
	"""@api.constrains('dni')
	def _check_dni(self):
		for r in self:
			if len(self.dni)!=9:
				raise ValidationError("DNI: Ha de tenir 9 caràcters")"""
				
	@api.onchange('dni')
	def _correct_dni(self):
		tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
		numeros = "1234567890"
		#d = {0:"T" , 1:"R", 2:"W", 3:"A", 4:"G", 5:"M", 6:"I", 7:"F", 8:"P", 9:"D", 10:"X", 11:"B", 12:"N", 13:"J", 14:"Z", 15:"S", 16:"Q", 17:"V", 18:"H", 19:"L", 20:"C", 21:"K", 22:"E"}
		for r in self:
			nif = r.dni
			if (len(nif) == 9):
				letraControl = nif[8].upper()
				dni = nif[:8]
				if ( len(dni) == len( [n for n in dni if n in numeros] ) ):
					if tabla[int(dni)%23] != letraControl:
						raise ValidationError("DNI: Letra Incorrecta")
			"""div = divmod(int(r.dni), 23)
			letra = d[div[1]] #Letra obtenida
			if r.dni[:-1] != letra :
				raise ValidationError("DNI: Letra Incorrecta")""" 
	
class Metge(models.Model):
	_name = 'h2.metge'
	_rec_name = 'cognom'
	_order = 'cognom'
	
	especialitat_id = fields.Many2one('h2.especialitat', ondelete='set null', string="Especialitat", required=False)
	pacient_rel = fields.Many2many('hospital_dam.pacient')
	
	nom = fields.Char(required=True)
	cognom = fields.Char(required=True)
	genere = fields.Selection([('m','m'),('f','f')], required=True)
	dni = fields.Char(required=True)
	adreça = fields.Char()
	anys = fields.Integer(string="Anys d'experiencia")
	
	edifici = fields.Char(string="Aquest metge visita a", related='especialitat_id.edifici')
	
	
class Especialitat(models.Model):
	_name = 'h2.especialitat'
	_rec_name = 'nom'
	_order = 'nom'
	
	nom = fields.Char(required=True)
	edifici = fields.Char(required=True)
	
	metge_ids = fields.One2many('h2.metge','especialitat_id',string='Metges',required=True,help='Metges especialistes')
	
class Prova(models.Model):
	_name = 'h2.prova'
	_rec_name = 'codi'
	_order = 'codi'
	
	nom = fields.Char(required=True)
	codi = fields.Selection([("Radio","Radiologia"),("Extr","Extraccions"),("Electro","Electro")], required=True)
	data = fields.Date(default=fields.Date.today)
	resultats = fields.Text()
	
	pacient_id = fields.Many2one('hospital_dam.pacient')



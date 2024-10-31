from odoo import models, fields, api


class TunasRoom(models.Model):
    _name = 'tunas.room'
    _description = 'Tunas Room'

    name = fields.Char(string='Nama Ruangan', required=True)
    type_room = fields.Selection(string='Tipe Ruangan', selection=[('small_room', 'Meeting Room Kecil'), ('large_room', 'Meeting Room Besar'), ('aula', 'Aula'),], required=True)
    location_room = fields.Selection(string='Lokasi Ruangan', selection=[('1a', '1A'), ('1b', '1B'), ('1c', '1C'), ('2a', '2A'), ('2b', '2B'), ('2c', '2C'),], required=True)
    image = fields.Binary(string='', required=True)
    capacity = fields.Char(string='Kapasitas Ruangan', required=True)
    notes = fields.Text(string='notes')

    

    
    
    
    


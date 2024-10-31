from odoo import models, fields, api

class TunasAritmatika(models.Model):
    _name = 'tunas.aritmatika'
    _description = 'Tunas Aritmatika'

    name = fields.Char(string='Name')
    angka_input = fields.Integer(string='Angka Input')
    angka_output = fields.Char(string='Angka Output', compute='_compute_aritmatika', readonly=True)

    @api.depends('angka_input')
    def _compute_aritmatika(self):
        for record in self:
            if record.angka_input:
                # Hitung deret aritmatika
                a = 2  # Nilai awal
                d = 3  # Beda antar angka
                deret = [a + i * d for i in range(record.angka_input)]
                # Simpan hasil dalam bentuk string
                record.angka_output = ', '.join(map(str, deret))
            else:
                record.angka_output = ''



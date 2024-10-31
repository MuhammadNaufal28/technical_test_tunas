from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class TunasBookingroom(models.Model):
    _name = 'tunas.bookingroom'
    _description = 'Tunas Bookingroom'

    no = fields.Char(string="Nomor Pemesanan",
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    tunas_room_id = fields.Many2one('tunas.room', string='Ruangan', required=True)
    name = fields.Char(string='Nama Pemesanan', required=True)
    date = fields.Datetime('Tanggal Pemesananan', required=True)
    state = fields.Selection([
        ('draft', 'Draft'), ('on_going', 'On Going'), ('done', 'Done')
    ], string='Status', default='draft')

    def action_on_going(self):
        self.write({'state': 'on_going'})

    def action_done(self):
        self.write({'state': 'done'})

    notes = fields.Html(string='Catatan')

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            # Search for records with the same name, excluding the current record
            duplicate_name = self.env['tunas.bookingroom'].search([
                ('name', '=', record.name),
                ('id', '!=', record.id)
            ])
            if duplicate_name:
                raise ValidationError("Nama Pemesanan '%s' sudah ada. Silakan gunakan nama lain." % record.name)

    @api.constrains('date', 'tunas_room_id')
    def _check_date_and_room(self):
        for record in self:
            same_date_and_room = self.env['tunas.bookingroom'].search([
                ('date', '=', record.date),
                ('tunas_room_id', '=', record.tunas_room_id.id),
                ('id', '!=', record.id),
                ('state', '!=', 'done'),
            ])
            if same_date_and_room:
                raise ValidationError('Tanggal dan ruangan ini sudah digunakan oleh booking lain yang belum selesai.')

    @api.model
    def create(self, vals):
        # Generate the sequence number
        if vals.get('no', _("New")) == _("New"):
            sequence_no = self.env['ir.sequence'].next_by_code('no.booking.room') or _("New")
            room = self.env['tunas.room'].browse(vals.get('tunas_room_id'))
            # Append room type if exists
            if room and room.type_room:
                vals['no'] = f"{sequence_no}-{room.type_room}"
            else:
                vals['no'] = sequence_no

        record = super(TunasBookingroom, self).create(vals)
        return record

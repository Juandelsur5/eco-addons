from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    # === ECO: Tipo de Persona (definición de negocio) ===
    eco_partner_type = fields.Selection(
        [
            ('client', 'Cliente'),
            ('supplier', 'Proveedor'),
        ],
        string='Tipo de Persona',
        required=True,
        default='client'
    )

    # === ECO: Ubicación Operativa ===
    x_neighborhood = fields.Char(
        string="Barrio / Vereda"
    )

    x_location_notes = fields.Text(
        string="Observaciones de ubicación"
    )

    x_latitude = fields.Float(
        string="Latitud GPS",
        digits=(10, 6)
    )

    x_longitude = fields.Float(
        string="Longitud GPS",
        digits=(10, 6)
    )

    x_geo_source = fields.Selection(
        [
            ("manual", "Manual"),
            ("mobile_app", "App móvil"),
            ("web_gps", "GPS Web"),
        ],
        string="Origen GPS",
        default="manual"
    )

    x_geo_accuracy = fields.Integer(
        string="Precisión GPS (m)"
    )

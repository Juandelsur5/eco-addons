from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_neighborhood = fields.Char(
        string="Vereda/Barrio",
        help="Vereda rural o barrio urbano del cliente para operación en campo"
    )

    x_location_notes = fields.Text(
        string="Observaciones de ubicación",
        help="Referencias adicionales para direcciones difíciles (ej. portón azul, vía destapada, casa tercera)"
    )

    x_latitude = fields.Float(
        string="Latitud GPS",
        digits=(10, 6),
        help="Latitud GPS del cliente"
    )

    x_longitude = fields.Float(
        string="Longitud GPS",
        digits=(10, 6),
        help="Longitud GPS del cliente"
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
        string="Precisión GPS (m)",
        help="Precisión del GPS en metros"
    )

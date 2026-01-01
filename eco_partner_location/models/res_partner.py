from odoo import models, fields
from odoo import api
import re



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


    # === ECO: Campos RAW (WhatsApp) ===
    x_latitude_raw = fields.Char(string="Latitud (WhatsApp)")
    x_longitude_raw = fields.Char(string="Longitud (WhatsApp)")

    def _dms_to_decimal(self, value):
        if not value:
            return None
        match = re.match(
            r"(\d+)°\s*(\d+)'?\s*([\d.]+)\"?\s*([NSEW])",
            value.strip()
        )
        if not match:
            return None
        deg, minutes, seconds, direction = match.groups()
        decimal = float(deg) + float(minutes) / 60 + float(seconds) / 3600
        if direction in ('S', 'W'):
            decimal = -decimal
        return decimal

    @api.onchange('x_latitude_raw', 'x_longitude_raw')
    def _onchange_raw_coordinates(self):
        if self.x_latitude_raw:
            lat = self._dms_to_decimal(self.x_latitude_raw)
            if lat is not None:
                self.x_latitude = lat
                self.x_geo_source = 'whatsapp'

        if self.x_longitude_raw:
            lon = self._dms_to_decimal(self.x_longitude_raw)
            if lon is not None:
                self.x_longitude = lon
                self.x_geo_source = 'whatsapp'


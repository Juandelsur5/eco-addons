{
    "name": "ECO Partner Location",
    "version": "17.0.1.0.0",
    "summary": "Ubicación operativa de clientes para fuerza de ventas",
    "description": """
Extiende res.partner para clientes atendidos por fuerza de ventas.
Agrega información operativa de ubicación (vereda/barrio, GPS y observaciones).
No aplica para proveedores.
No afecta contabilidad, impuestos ni localización.
    """,
    "category": "ECO/Partners",
    "author": "ECO",
    "license": "LGPL-3",
    "depends": [
        "base",
        "contacts",
    ],
    "data": [
        "views/res_partner_view.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}

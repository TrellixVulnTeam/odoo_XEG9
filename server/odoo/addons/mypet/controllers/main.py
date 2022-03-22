import odoo
import logging
_logger = logging.getLogger(__name__)

class MyPetAPI(odoo.http.Controller):
    @odoo.http.route('/foo', auth='public')
    def foo_handler(self):
        return "Welcome to 'foo' API!"
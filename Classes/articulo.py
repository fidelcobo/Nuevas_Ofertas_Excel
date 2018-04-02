class Articulo:

    def __init__(self, unit= 0, tech='', manufacturer='', code='', descripcion_prod= '', list_price = '',
                 coste_prod=0.0, venta_prod=0.0, maintenance= False, init_date='', end_date='', durac=0,
                 sku_uptime='', descr_uptime='', backout_name='', list_price_back=0.0,
                 coste_unit_back=0.0, uplift=0.0, cost_unit_manten=0.0, margen_mant=0.0, venta_mant=0.0):

        self.unit = unit
        self.tech = tech
        self.manufacturer = manufacturer
        self.code = code
        self.descripcion_prod = descripcion_prod
        self.list_price = list_price
        self.coste_prod = float(coste_prod)
        self.venta_prod = venta_prod
        self.maintenance = maintenance
        self.init_date = init_date
        self.end_date = end_date
        self.durac = int(durac)
        self.sku_uptime = sku_uptime
        self.descr_uptime = descr_uptime
        self.backout_name = backout_name
        self.list_price_back = float(list_price_back)
        self.coste_unit_back = float(coste_unit_back)
        self.uplift = float(uplift)
        self.cost_unit_manten = float(cost_unit_manten)
        self.margen_mant = float(margen_mant)
        self.venta_mant = float(venta_mant)

    @staticmethod
    def fill(*args):
        unit = args[0]
        tech = args[1]
        manufacturer = args[2]
        code = args[3]
        descr_prod = args[4]
        list_price_prod = args[5]
        coste_prod = args[6]
        venta_prod = args[7]
        manten = args[8]
        init_date = args[9]
        end_date = args[10]
        durac = args[11]
        sku_uptime = args[12]
        descr_uptime = args[13]
        backout_name = args[14]
        list_price_back = args[15]
        coste_unit_back = args[16]
        uplift = args[17]
        cost_unit_manten = args[18]
        margen_mant = args[19]
        venta_mant = args[20]
        return Articulo(unit, tech, manufacturer, code, descr_prod, list_price_prod, coste_prod, venta_prod, manten, init_date,
                        end_date, durac, sku_uptime, descr_uptime, backout_name, list_price_back, coste_unit_back,
                        uplift, cost_unit_manten, margen_mant, venta_mant)

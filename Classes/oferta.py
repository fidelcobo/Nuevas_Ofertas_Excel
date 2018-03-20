from PyQt5 import QtWidgets
from Classes.offer_screen import Ui_Dialog
from Classes.articulo import Articulo
from auxiliar import get_ultima_fila, busca_columnas, clasificar_articulos, hacer_oferta

import openpyxl
import os


class Offer(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Definiciones de listas de ítems por fabricante
        self.lista_checkpoint = []
        self.lista_fortinet = []
        self.lista_hp = []
        self.lista_aruba = []
        self.lista_f5 = []
        self.lista_cisco = []
        self.lista_alcatel = []
        self.lista_paloalto = []
        self.lista_juniper = []
        self.lista_bluecoat = []
        self.lista_brocade = []

        # Operaciones de pulsación de botones
        self.browse_Button.clicked.connect(self.buscar_fichero_oferta)
        self.ok_button.clicked.connect(self.procesar_oferta)

    def buscar_fichero_oferta(self):

        # Abre el explorador Windows para que el usuario seleccione la oferta
        direct = QtWidgets.QFileDialog.getOpenFileName(self, "Elegir archivo de oferta")
        print(direct[0])
        self.fichero_oferta.setText(direct[0])

    def extraer_articulos(self, file_offer):
        """
        Abre el fichero de oferta y extrae los datos en una lista de objetos Articulo
        :param file_offer:
        :return: lista_articulos .Lista de objetos clase Articulo
        """
        try:
            libro_oferta = openpyxl.load_workbook(file_offer, data_only=True)
            sheet = libro_oferta.get_sheet_by_name('Detalle')

        except:
            QtWidgets.QMessageBox.critical(self, "Error",
                                           "Imposible abrir fichero de oferta")
            return None

        lista_busqueda = ['Unid', 'Tech', 'Manufacturer', 'Part Number real (*)', 'Coste de producto',
                          'Venta de producto', '¿Mantenimiento?', 'Fecha inicio',
                          'Fecha fin', 'Duración (años)', 'Entitlement Uptime', 'Description Entitlement Uptime',
                          'Nombre de Backout', 'Precio de lista Backout Unitario (EUR) - ANUAL',
                          'Coste Backout Unitario (EUR) - ANUAL','Uplift', 'Coste anual mantenimiento(EUR)',
                          'Margen mantenimiento', 'Venta mantenimiento (EUR)', 'Descripción', 'Precio_lista']

        headers_row = str(10)
        first_row = str(11)

        ok, lista_columnas = busca_columnas(sheet, lista_busqueda, headers_row)
        lista_articulos = []

        if ok:
            unid_col, tech_col, manuf_col, code_col, cost_prod_col, venta_prod_col = lista_columnas[0:6]
            manten_col, init_date_col, end_date_col, durac_col, uptime_cod_col, descr_upt_col = lista_columnas[6:12]
            back_name_col, list_back_col, cost_back_col, uplift_col = lista_columnas[12:16]
            cost_mant_col, margen_mant_col, venta_mant_col, descr_prod_col, list_price_prod_col = lista_columnas[16:21]

            last_row = get_ultima_fila(sheet, code_col)
            print(last_row)

            for x in range(int(first_row), int(last_row) + 1):
                unid = sheet[unid_col + str(x)].value
                tech = sheet[tech_col + str(x)].value
                manuf = sheet[manuf_col + str(x)].value
                code = sheet[code_col + str(x)].value
                descr_prod = sheet[descr_prod_col + str(x)].value
                list_price_prod = sheet[list_price_prod_col + str(x)].value
                cost_prod = sheet[cost_prod_col + str(x)].value
                venta_prod = sheet[venta_prod_col + str(x)].value
                manten = sheet[manten_col + str(x)].value
                init_date = sheet[init_date_col + str(x)].value
                end_date = sheet[end_date_col + str(x)].value
                durac = sheet[durac_col + str(x)].value
                uptime_cod = sheet[uptime_cod_col + str(x)].value
                descr_upt = sheet[descr_upt_col + str(x)].value
                back_name = sheet[back_name_col + str(x)].value
                list_back = sheet[list_back_col + str(x)].value
                cost_back = sheet[cost_back_col + str(x)].value
                uplift = sheet[uplift_col + str(x)].value
                cost_mant = sheet[cost_mant_col + str(x)].value
                margen_mant = sheet[margen_mant_col + str(x)].value
                venta_mant = sheet[venta_mant_col + str(x)].value
                lista_articulos.append(Articulo.fill(unid, tech, manuf, code, descr_prod, list_price_prod, cost_prod,
                                                     venta_prod, manten, init_date, end_date, durac, uptime_cod,
                                                     descr_upt, back_name, list_back, cost_back, uplift, cost_mant,
                                                     margen_mant, venta_mant))
                pass
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "El fichero de oferta tiene formato incorrecto \n "
                                                 "Por favor, seleccione otro")
            return

        return lista_articulos

    def procesar_oferta(self):

        file_offer = self.fichero_oferta.text()
        offer_dir, name = os.path.split(file_offer)

        if file_offer:

            lista_items = self.extraer_articulos(file_offer)
            if not lista_items:
                return

            clasificar_articulos(lista_items, self)
            hacer_oferta(offer_dir, self)
            # hacer_oferta_ms(lista_items, offer_dir, self)
            QtWidgets.QMessageBox.information(self, "OK", "Parece que todo ha ido bien. "
                                                    "\n Ficheros de oferta generados")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, seleccione un fichero de oferta")


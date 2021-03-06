# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 TRESCloud (<http://www.trescloud.com>)
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    "name" : "Remove create and easy_create in many2one related",
    "version" : "0.1",
    "description" : """
    Authors:
    Pablo Vizhnay
        """,
    "author" : "TRESCloud Cia. Ltda.",
    "website" : "http://www.trescloud.com",
    "depends" : ['base','sale','account','web_m2x_options'],
    "category" : "Custom Modules",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
        'views/sale_purchase_order.xml',
        'views/account_invoice.xml',
    ],
    "auto_install": False,
    "installable": True,
}

# -*- coding: utf-8 -*-

{
    'name': 'QAQC Analyzer',
    'version': '1.0',
    'author': 'Technoindo.com',
    'category': 'Mining Management',
    'depends': [
        'mining_qaqc',
    ],
    'data': [
        'views/menu.xml',
        "wizard/qaqc_analyzer_pile_compute.xml",
    ],
    'qweb': [
        # 'static/src/xml/cashback_templates.xml',
    ],
    'demo': [
        # 'demo/sale_agent_demo.xml',
    ],
    "installable": True,
	"auto_instal": False,
	"application": False,
}

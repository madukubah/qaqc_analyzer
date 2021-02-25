# -*- coding: utf-8 -*-

{
    'name': 'Mining Analyzer',
    'version': '1.0',
    'author': 'Technoindo.com',
    'category': 'Mining Management',
    'depends': [
        'mining_production',
    ],
    'data': [
        'views/menu.xml',
        'wizard/mining_analyzer_ritase.xml',
        "wizard/mining_analyzer_hourmeter.xml",
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

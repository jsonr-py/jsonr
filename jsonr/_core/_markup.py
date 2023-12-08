import html
import html.parser
import html.entities
import xml
import xml.etree.ElementTree
import xml.dom
import xml.dom.minidom
import xml.dom.pulldom
import xml.sax
import xml.sax.handler
import xml.sax.saxutils
import xml.sax.xmlreader
import xml.parsers.expat

class Markup:
    def __init__(self):
        self.html: object = html
        self.html_parser: object = html.parser
        self.html_entities: object = html.entities
        self.xml: object = xml
        self.xml_etree: object = xml.etree.ElementTree
        self.xml_dom: object = xml.dom
        self.xml_dom_minidom: object = xml.dom.minidom
        self.xml_dom_pulldom: object = xml.dom.pulldom
        self.xml_sax: object = xml.sax
        self.xml_sax_handler: object = xml.sax.handler
        self.xml_sax_saxutils: object = xml.sax.saxutils
        self.xml_sax_xmlreader: object = xml.sax.xmlreader
        self.xml_parsers_expat: object = xml.parsers.expat

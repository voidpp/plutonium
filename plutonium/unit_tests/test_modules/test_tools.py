import unittest
from lxml import etree

from tools import *

class TestTools(unittest.TestCase):

    def test_xml_element_to_storage(self):

        res = Storage(
            guid = 'someguid',
            link = 'somelink',
            title = 'sometitle'
        )

        root = etree.Element("root")
        item = etree.SubElement(root, "item")
        etree.SubElement(item, "guid").text = res.guid
        etree.SubElement(item, "link").text = res.link
        etree.SubElement(item, "title").text = res.title

        self.assertEqual(res, xml_element_to_storage(item))



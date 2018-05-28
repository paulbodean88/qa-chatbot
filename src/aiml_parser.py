"""
Parser of the standard startup file and also of the aiml ones
"""

import xml.etree.ElementTree as ET
import os


class AIMLParser:
    def __init__(self):
        self._public_path = os.getcwd().split("src")[0] + "/public/"

    def get_root(self, file_name):
        tree = ET.parse(self._public_path + file_name)
        return tree.getroot()

    def get_aiml_content(self, aiml_file):
        all_text = []
        root = self.get_root("aiml_files/" + aiml_file + ".aiml")
        for category in root:
            for child in range(len(category) - 1):
                all_text.append(dict(user=category[child].text.strip(),
                                     bot=category[child + 1].text.strip()))
        return all_text

    def get_patterns(self, xml_object="std-startup"):
        root = self.get_root(xml_object + ".xml")

        patterns = []
        for category in root:
            for pattern in category:
                if pattern.tag == "pattern":
                    patterns.append(pattern.text)

        return patterns

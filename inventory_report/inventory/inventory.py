import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        data = cls.reports(path)
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)
        return TypeError("typeNotFound")

    @classmethod
    def reports(cls, path):
        if path.endswith('csv'):
            with open(path) as file:
                _list = list(csv.DictReader(file))
            return _list
        elif path.endswith('json'):
            with open(path) as file:
                return json.loads(file.read())
        elif path.endswith('xml'):
            with open(path) as file:
                return xmltodict.parse(file.read())["dataset"]["record"]

import csv
import json
# import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def import_csv(path, type):
    with open(path) as file:
        reader = csv.DictReader(file)
        _list = list(reader)
        if type == "simples":
            return SimpleReport.generate(_list)
        return CompleteReport.generate(_list)


def import_json(path, type):
    with open(path) as file:
        _list = json.load(file)
        if type == "simples":
            return SimpleReport.generate(_list)
        return CompleteReport.generate(_list)


""" def import_xml(path, type):
    with open(path) as file:
        _list = xmltodict.parse(file.read())["dataset"]["record"]
        if type == "simples":
            return SimpleReport.generate(_list)
        return CompleteReport.generate(_list)
 """


class Inventory():
    def import_data(path, type):
        if ".csv" in path:
            return import_csv(path, type)
        elif ".json" in path:
            return import_json(path, type)
    """        elif ".xml" in path:
            return import_xml(path, type)
        else:
            return TypeError """

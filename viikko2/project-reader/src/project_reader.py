from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        #dict raakadatalle, ja pienenmpi dict tarpeelliselle datalle
        x = toml.loads(content)
        n = x['tool']['poetry']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(n['name'], n['description'], n['license'], n['dependencies'], n['group']['dev']['dependencies'], n['authors'])

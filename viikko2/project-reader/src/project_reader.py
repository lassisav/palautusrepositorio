from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        #print("väli")

        x = toml.loads(content)
        n = x['tool']['poetry']
        #print(x)
        #print("väli")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(n['name'], n['description'], n['dependencies'], n['group']['dev']['dependencies'])

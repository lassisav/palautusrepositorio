class Project:
    def __init__(self, name, description, license, dependencies, dev_dependencies, authors):
        self.name = name
        self.description = description
        self.license = license
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        auth = ""
        for a in self.authors:
            auth += " - " + a + "\n"
        dep = ""
        for b in self.dependencies:
            dep += " - " + b + "\n"
        dd = ""
        for c in self.dev_dependencies:
            dd += "\n - " + c
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n"
            f"\nAuthors:"
            f"\n{auth or '-'}"
            f"\nDependencies:"
            f"\n{dep or '-'}"
            f"\nDevelopment dependencies:"
            f"{dd or '-'}"
        )

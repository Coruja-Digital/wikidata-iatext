# Script to export all the worked items from Wikidata to RDF/Turtle (.ttl)

from exporter import utils

class Exporter:
    def __init__(self):
            utils.checkCommand("npm")
            utils.checkCommand("wd", commandName="wikidata-cli")

    def run(self):
        # Command example of wikidata-cli: wd data --format ttl Q123 Q3548931 Q515168
        # utils.runCommand("wd", "data", "--format", "ttl", "Q123")
        utils.runCommand("wd", "sparql", "researchers/researchers.rq", outputfile="researchers/researchers")
        utils.runCommand("wd", "data", "--format", "ttl", inputfile="researchers/researchers", outputfile="researchers/researchers.ttl")


utils = utils.Utils()

# To test
exporter = Exporter()
exporter.run()

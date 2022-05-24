import sys

print("BUILDING ENERPAC IMPORT!")

from configuration import config

from importers.EnerpacImporter import EnerpacImporter
from transformers.EnerpacTransformer import EnerpacTransformer
from validators.EnerpacValidator import EnerpacValidator
from loaders.PrintFileLoader import PrintFileLoader

configs = config

validator = EnerpacValidator()
transformer = EnerpacImporter()
loader = PrintFileLoader()

importer = EnerpacImporter(validator, transformer, loader, configs)

importer.run()

print("ENERPAC IMPORT BUILT!")
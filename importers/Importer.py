import csv

from ..maps.NewDataFileMap import NewDataFileMap
from ..maps.ExistingDataFileMap import ExistingDataFileMap
from ..maps.OutputFileMap import OutputFileMap

class Importer:

    def __init__(self, validator, transformer, loader, configs):
        self.validator=validator
        self.transformer=transformer
        self.loader=loader

        self.setupConfigs(configs)

    def setupConfigs(self, configs):
        self.newDataFileLocation = configs["newDataFileLocation"]
        self.existingDataFileLocation = configs["existingDataFileLocation"]
        self.outputFileLocation = configs["outputFileLocation"]

        self.newDataFileMap = NewDataFileMap
        self.existingDataFileMap = ExistingDataFileMap
        self.outputDataFileMap = OutputFileMap

        self.outputDataFileName = configs["outputFileName"]

        self.newDataFilePrimaryKeyIndex = configs["newDataFilePrimaryKeyIndex"]
        self.outputDataFilePrimaryKeyIndex = configs["outputDataFilePrimaryKeyIndex"]

    def run(self):
        self.newDataFile = self.getCSVFileContents(self.newDataFileLocation)
        self.existingDataFile = self.getCSVFileContents(self.existingDataFileLocation)
        outputFile = self.getOutputFile()

        outputFile = self.transformer.mergeExistingDataIntoOutputFile(self.existingDataFile, outputFile)
        outputFile = self.transformer.mergeNewDataIntoOutputFile(self.newDataFile, outputFile)
        outputFile = self.transformer.formatOutputFile

        [isValidOutputFile, message] = self.validator.isValidFile(self.newDataFile, self.existingDataFile, outputFile)
        if not isValidOutputFile:
            print("Validation Failed: " + message)
            return

        self.loader.load(outputFile)

    def getCSVFileContents(self, fileLocation):
        contents=[]
        with open(fileLocation) as csvFile:
            reader = csv.reader(csvFile)
            next(reader, None)  # skip the headers

            rowNumber=0
            for row in reader:

                isValid = self.validateRow(row, rowNumber)
                if isValid:
                    contents.append(row)

                rowNumber+=1

        return contents

    def getOutputFile(self):
        outputFileColumns = []
        for key in self.outputDataFileMap:
            outputFileColumns.append(key)
            
        outputFile = []
        outputFile.append(outputFileColumns)

        return outputFile



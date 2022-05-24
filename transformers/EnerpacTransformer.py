from Transformer import Transformer

class EnerpacTransformer(Transformer):
    def transform(self, data):
        pass
    
    def putExistingDataInOutputFile(self, outputFile, existingDataFile):
        for row in existingDataFile:
            newOutputFileRow=[]

            for columnName in self.outputDataFileMap:

                isInExistingDataFile = columnName in self.existingDataFileMap.keys()
                if isInExistingDataFile:
                    existingFileIndex=self.existingDataFileMap[columnName]
                    column=row[existingFileIndex]
                else:
                    column=self.getColumnValue(columnName)

                newOutputFileRow.append(column)

            outputFile.append(newOutputFileRow)
        return outputFile

    def getColumnValue(self, columnName):
        options={
            "Default":"",
            "X":"X",
            "ProdStockType":"S",
            "ProdStatus":"A",
            "ProdWeight":"0",
            "SupplierDiscountFlag":"%",
            "SupplierDiscountPercent":"0",
            "MainWhs":"01",
            "SupplierId":"EPAC",
            "StockUOM":"EA",
            "PurchaseUOM":"E5",
            "Discount":"1"
        }

        if columnName in options.keys():
            return options[columnName]
        else:
            return options["Default"]


    def putNewDataInOutputFile(self, outputFile, newDataFile):
        for i in range(1, len(outputFile)):
            row = outputFile[i]
            rowPrimaryKey = row[self.outputFilePrimaryKey]

            rowExistsInNewDataFile=False
            newDataFileRow=0
            for newDataFileRow in newDataFile:
                newDataFileRowPk = newDataFileRow[self.newDataFilePrimaryKey]
                if rowPrimaryKey==newDataFileRowPk:
                    rowExistsInNewDataFile=True
                    break

                # does pk exist in new data?

            for colIndex in range(len(row)):
                columnValue=row[colIndex]

                # is this value in newData
                

        return outputFile
    
    def validateRow(self, row, rowNumber):
        if len(row) == 0:
            print(f'Row #{rowNumber} is empty: ')
            print(row)
            return False

        if row[0] == "":
            print(f'First item in row #{rowNumber} is empty: ')
            print(row)
            return False

        return True
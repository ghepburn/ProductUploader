import os

projectPath = os.path.dirname(os.path.abspath(__file__))

config={
    "newDataFileLocation":projectPath + '/inputs/testFiles/newDataTestFile.csv',
    "existingDataFileLocation":projectPath + '/inputs/testFiles/existingDataTestFile.csv',
    "outputFileLocation":projectPath,

    "outputFileName":"GregOutputFile",

    "newDataFilePrimaryKeyIndex":0,
    "outputFilePrimaryKeyIndex":1
}
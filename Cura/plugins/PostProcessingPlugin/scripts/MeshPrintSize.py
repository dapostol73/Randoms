import re #To perform the search and replace.

from ..Script import Script


class MeshPrintSize(Script):

    def getSettingDataString(self):
        return """{
            "name": "Mesh Print Size",
            "key": "MeshPrintSize",
            "metadata": {},
            "version": 2,
            "settings":{}
        }"""

    def execute(self, data):
            minMaxXY = {'MAXY':0,'MAXX':0, 'MINY':0,'MINX':0}
            lineData = ''

            for layer_number, layer in enumerate(data):
                for k,v in minMaxXY.items():
                    result = re.search(str(k)+":(\d*\.?\d*)",layer)
                    if result is not None:
                        minMaxXY[k] = result.group(1)

                if re.search('START_PRINT.*', layer) is not None:
                    lineData = layer
                    for k, v in minMaxXY.items():
                        pattern = re.compile('START_PRINT ')
                        replace = 'START_PRINT {variable}={value} '.format(variable = k, value = v)
                        lineData = re.sub(pattern, replace, lineData)

                    data[layer_number] = lineData

            return data
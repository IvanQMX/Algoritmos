from typing import List

def parse_array(path: str):
    output: List[int] = []
    file = open(path, 'r')
    content = file.read()
    for item in content.split(','):
        try:
            value = int(item)
            output.append(value)
        except ValueError:
            print('Archivo con contenido inválido')
            return None
    return output
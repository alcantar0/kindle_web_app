"""Funções relacionadas ao tratamento de strings, listas e datas"""
dia_da_semana = {
    "Sunday": "Dom",
    "Monday": "Seg",
    "Tuesday": "Ter",
    "Wednesday": "Qua",
    "Thursday": "Qui",
    "Friday": "Sex",
    "Saturday": "Sáb",
}
meses = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}


def transform_to_list(*args):
    """Tranforma em lista um string"""
    string = args[0]
    string = string.replace(",", "")
    lista = string.split()
    return lista


def convert_to_string(*args):
    """Transform um lista em string (data)"""
    lista = args
    string = ""
    string += dia_da_semana[lista[0]]
    string += ", "
    string += meses[f"{lista[1]}"]
    string += "/"
    string += lista[2]
    string += "/"
    string += lista[3]

    return string

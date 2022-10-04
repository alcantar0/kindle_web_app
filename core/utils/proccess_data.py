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


def transform_to_list(string):
    """Tranforma em lista um string"""
    string = string.replace(",", "")
    lista = string.split()
    return lista


def convert_to_string(*args):
    """Transform um lista em string (data)"""
    string = ""

    string += dia_da_semana[f"{args[0]}"]
    string += ", "
    string += meses[f"{args[1]}"]
    string += "/"
    string += args[2]
    string += "/"
    string += args[3]

    return string

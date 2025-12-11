# Жүйенің ерекше жағдай (қате) кластарын сипаттайтын модуль.


class AirQualityError(Exception):
    
    # Ауа сапасын бақылау жүйесі үшін базалық қате класы.
    
    pass


class AirQualityApiError(AirQualityError):
    
    #Сыртқы ауа сапасы API-мен жұмыс істеу кезінде туындайтын қателер.
    
    pass

class ApiError(Exception):
    pass

class ParserError(Exception):
    pass
import pandas
import time
from CenturionApi.models import State, City, PostalCode, Settlement

tiempo_inicio = time.time()

url = 'static/locations/settlements.xls'


def create_(data_url, sheet_name):
    
    data = pandas.read_excel(data_url, sheet_name)
    state_name = data['d_estado'].unique()
    cities = data['D_mnpio'].unique()
    postal_codes = data['d_codigo'].unique()

    # CREAR LA ENTIDAD FEDERTIVA EN LA DB
    state, created = State.objects.get_or_create(number=sheet_name, name=state_name[0])
    if created:
        state.save()
        print(f'Estado {sheet_name}, {state_name[0]}: creado con exito...')
    else:
        print(f'{state_name[0]} ya existe...')

    # CREAR MUNICIPIOS, ITERAR LOS MUNICIPIOS UNICOS Y AGREGARLOS A LA DB
    counter = 0
    for city_name in cities:
        city, created = City.objects.get_or_create(state=state, name=city_name)
        if created:
            city.save()
            counter += 1
    print(f'Se han creado {counter} municipios para {state_name[0]}')

    # CREAR LOS CODIGOS POSTALES
    print(f'{len(postal_codes)} codigos para {state_name[0]}')
    for code in postal_codes:
        code_to_search = data.loc[data['d_codigo'] == code]

        for indexer, row in code_to_search .iterrows():
            code_city = row['D_mnpio']
            settlement_name = row['d_asenta']
            settlement_type = row['d_tipo_asenta']

            assign_city = City.objects.get(state=state, name=code_city)
            try:
                postal_code = PostalCode.objects.get(city=assign_city, code=code)
                created_postal_code = False
            except:
                postal_code = PostalCode(city=assign_city, code=code)
                created_postal_code = True
            
            if created_postal_code:
                postal_code.save()
            
            settlement, created = Settlement.objects.get_or_create(postal_code=postal_code, name=settlement_name, settlement_type=settlement_type)
            if created:
                settlement.save()
            else:
                print(f'{settlement.postal_code.city.state.name}, {settlement.postal_code.city.name}, {settlement.settlement_type} {settlement.name} CP{settlement.postal_code} , ya registrado previamente...')



try:
    State.objects.get(number=32)
    objects_in_state = True
except:
    objects_in_state =False


if objects_in_state:

    print("Ya existen datos dentro de la Tabla Estados")

else:

    for index in range(1,33):
        create_(url, index)
        
    
    # Registra el tiempo de finalización
    tiempo_fin = time.time()

    # Calcula el tiempo transcurrido
    tiempo_transcurrido = (tiempo_fin - tiempo_inicio)
    if tiempo_transcurrido >= 60:
        print(f"Tiempo transcurrido: {tiempo_transcurrido/60} minutos")
    else:
        print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")
import datetime


class CreatePayPromises:


    def __init__(self, data):

        self.months = {
            1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo',
            6: 'junio', 7: 'julio', 8: 'agosto', 9: 'septiembre',
            10: 'octubre', 11: 'noviembre', 12: 'diciembre',
            }
        self.index_months = list(self.months.keys())
        self.promises = 11
        self.contract_date = data['date']

        self.contract_day = int(data['date'].strftime('%d'))
        self.contract_month = int(data['date'].strftime('%m'))
        self.contract_year = int(data['date'].strftime('%Y'))

        self.date_tupple = (self.contract_year, self.contract_month, self.contract_day)
        self.month_n_day_list = [self.contract_month, self.contract_day]
        self.pay_days = []
    



    # ARROJA EL LUNES PROXIMO SI SE ATRAVIESA FIN DE SEMANA
    def pay_only_business_days(self, date):

        # RECIBE UNA FECHA Y TRABAJA CON ELLA PARA SABER SI ES
            week_day = date.weekday()

            if week_day == 5 or week_day == 6:

                # ES SABADO
                if week_day == 5:
                    next_monday = date + datetime.timedelta(days=2)
                
                # Es domingo
                elif week_day == 6:
                    next_monday = date + datetime.timedelta(days=1)
                return next_monday

            else:
                return date


    # VAMOS A SALTAR DIAS FESTIVOS
    def skip_holidays(self, date):

        mandatory_holidays_list = [
                (1, 1), # Año Nuevo
                (2, 5), # Día de la Constitución Mexicana
                (3, 18), # Conmemoración del natalicio de Benito Juárez
                (5, 1), # Día del Trabajo
                (9, 16), # Día de la Independencia de México
                (11, 18), # Conmemoración del inicio de la Revolución mexicana
                (12, 25),  # Navidad
            ]

        unofficial_holidays_list = [
                (3, 28), # Días “santos”
                (3, 29), # Días “santos”
                (5, 5), # Batalla de Puebla
                (10, 12), # Día de la Raza
                (10, 31), # All Hallows Eve
                (11, 1), # Día de las Almas
                (11, 2), # Día de las Almas
                (12, 12), # Día del banquero
            ]

        #Agragara +1 al dia hasta que salga de ambas listas.
        while True:

            month = int(date.strftime('%m'))
            day = int(date.strftime('%d'))
            week_day = date.weekday()
            veryfy_day = (month, day)

            print(veryfy_day)

            if veryfy_day not in mandatory_holidays_list and veryfy_day not in unofficial_holidays_list:
                skip_weekend = self.pay_only_business_days(date)
                date = skip_weekend
                return date
            
            else:
                if veryfy_day in mandatory_holidays_list:

                    if week_day == 0 or week_day == 1 or week_day == 2 or week_day == 4:
                        date += datetime.timedelta(days=1)

                    elif week_day == 3:
                        date += datetime.timedelta(days=2)
                    
                    elif week_day == 5 or week_day == 6:
                        print("Es fin de semana")
                        skip_weekend = self.pay_only_business_days(date)
                        date = skip_weekend
                else:
                    date += datetime.timedelta(days=1)


    # AGREGA DIAS DE A LA LISTA Y SE APOYA DE business_days PARA ASEGURAR QUE SEAN HABILES
    def add_pay_days(self, pays):

        month = self.month_n_day_list[0]
        day = self.month_n_day_list[1]
        year = self.contract_year

        self.promises = pays

        while self.promises > 0:
            month += 1

            if month > 12:
                month = 1
                year += 1
            

            try:
                scheduled_day = datetime.datetime(year=year, month=month, day=day)
            except ValueError:
                # Si la fecha no es válida, ajustamos al último día del mes
                month -= 1
                scheduled_day = datetime.datetime(year=year, month=month, day=day) + datetime.timedelta(days=30)
                month += 1
            
            # Si es fin de semana pasamos al dia siguinte Habil
            is_business_day = self.pay_only_business_days(date=scheduled_day)
            # Comprobamos si es festivo 
            is_not_holiday = self.skip_holidays(date=is_business_day)
            
            pay_day = is_not_holiday
            
            self.pay_days.append(pay_day)
            self.promises -= 1
        
        self.promises = 11

        return self.pay_days
    
    # TRADUCE LA FECHA
    def humanize_date(self):

        formatted_dates = []

        for date in self.pay_days:
            # Extraer día, mes y año
            day = date.day
            month_number = date.month
            year = date.year

            # Obtener el nombre del mes a partir del número
            month_name = self.months[month_number]

            # Formatear la fecha en una cadena legible
            formatted_date = f"{day} de {month_name} de {year}"
            formatted_dates.append(formatted_date)

        return print(formatted_dates)
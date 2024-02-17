from data import connection, engine
from models.models import Base, Employees, Clients, Providers, Deliveries, Products, Orders


def create_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert_table():
    with connection() as conn:
        empl1 = Employees(
            last_name='Петрушкин',
            first_name='Валентин',
            patronymic='Иванович',
            position='Директор',
            address='ул. Стартовая, 17к3, 8',
            phone_number=9119523472,
            DOB='1978-12-26'
        )

        empl2 = Employees(
            last_name='Иванов',
            first_name='Александр',
            patronymic='Васильевич',
            position='Инженер',
            address='Глухой пер., 34, 52',
            phone_number=9067329088,
            DOB='1984-08-01'
        )

        empl3 = Employees(
            last_name='Петрова',
            first_name='Вероника',
            patronymic='Павловна',
            position='Менеджер по закупкам',
            address='г. Никольское, ул. Старая, 4, 56',
            phone_number=9048883401,
            DOB='1995-02-21'
        )

        empl4 = Employees(
            last_name='Пупкина',
            first_name='Адель',
            position='Менеджер по рекламе',
            address='1-й Верхний п-д, 8к4, 154',
            phone_number=9213057823,
            DOB='1994-01-20'
        )

        empl5 = Employees(
            last_name='Игольников',
            first_name='Вениамин',
            patronymic='Сидорович',
            position='Менеджер по продажам',
            address='Дачный пр., 35, 12',
            phone_number=9069131531,
            DOB='1993-04-12'
        )

        empl6 = Employees(
            last_name='Галицкая',
            first_name='Ольга',
            patronymic='Аркадиевна',
            position='Консультант',
            address='ул. Старорусская, 42к2, 71',
            phone_number=9115667393,
            DOB='2001-06-04'
        )

        empl7 = Employees(
            last_name='Вербицкая',
            first_name='Светлана',
            patronymic='Алексеевна',
            position='Консультант',
            address='Г. Стрельна, Санкт-Петербургсое ш., 214, 53',
            phone_number=9218769394,
            DOB='2003-04-12'
        )

        empl8 = Employees(
            last_name='Отверткин',
            first_name='Степан',
            patronymic='Васильевич',
            position='Сборщик',
            address='д. Новая, ул. Центральная, 2',
            phone_number=9813820190,
            DOB='1976-06-27'
        )

        empl9 = Employees(
            last_name='Новицкий',
            first_name='Игорь',
            patronymic='Александрович',
            position='Водитель',
            address='пр. Просвещения, 69, 61',
            phone_number=9516339123,
            DOB='1991-11-30'
        )

        empl10 = Employees(
            last_name='Отверткин',
            first_name='Геннадий',
            patronymic='Васильевич',
            position='Водитель',
            address='д. Новая, ул. Центральная, 2',
            phone_number=9814912498,
            DOB='1994-05-03'
        )

        conn.add_all([empl1, empl2, empl3, empl4, empl5, empl6, empl7, empl8, empl9, empl10])

        clnt1 = Clients(
            full_name='Тучин Александр Петрович',
            address='ул. Мечникова, 11, кв 21',
            phone_number=9118988822
        )

        clnt2 = Clients(
            full_name='Агарина Марина Геннадиевна',
            address='г. Кудрово, ул. Областная, 1, кв 218',
            phone_number=9058378488
        )

        clnt3 = Clients(
            full_name='Ситкина Вероника Павловна',
            address='пр. Ириновский, 27к 1, кв 69',
            phone_number=9213606054
        )

        clnt4 = Clients(
            full_name='Васницов Егор Александрович',
            address='ул. Жуковского 20, кв 8',
            phone_number=9214568743
        )

        clnt5 = Clients(
            full_name='Ручкин Арсений Валентинович',
            address='пр. Луначарского, 62 к 4, кв 219',
            phone_number=9815223487
        )

        conn.add_all([clnt1, clnt2, clnt3, clnt4, clnt5])

        prov1 = Providers(
            company_name='ООО ВудВоркс',
            contact_person='Александр Парин',
            phone_number=9213561111,
            address='Белозерская, 13д'
        )

        prov2 = Providers(
            company_name='ООО Импорт трейд',
            contact_person='Константин Верин',
            phone_number=9213765442,
            address='д. Дымки, Крайняя, 7'
        )

        prov3 = Providers(
            company_name='ООО Комфорт',
            contact_person='Арина Разумовская',
            phone_number=9311729000,
            address='Набережная Обводного канала, 153к17'
        )

        prov4 = Providers(
            company_name='ООО Синдикат',
            contact_person='Андрей Степанов',
            phone_number=9533656565,
            address='г. Смоленск, Ленина, 13'
        )

        prov5 = Providers(
            company_name='ООО ПластМеталл',
            contact_person='Елена Куницина',
            phone_number=9177321648,
            address='г. Курск, Вернадского, 15/6'
        )


        conn.add_all([prov1, prov2, prov3, prov4, prov5])

        dlvr1 = Deliveries(
            provider_id=2,
            date='2023-12-28'
        )

        dlvr2 = Deliveries(
            provider_id=1,
            date='2024-01-02'
        )

        dlvr3 = Deliveries(
            provider_id=5,
            date='2024-01-04'
        )

        dlvr4 = Deliveries(
            provider_id=4,
            date='2024-01-05'
        )

        dlvr5 = Deliveries(
            provider_id=3,
            date='2024-01-06'
        )

        conn.add_all([dlvr1, dlvr2, dlvr3, dlvr4, dlvr5])

        product1 = Products(
            supply_id=1,
            product_name='Петля мебельная',
            specifications='90',
            description='такая себе петля, но покупают',
            picture='',
            purchase_price=100,
            availability_in_stock=300,
            quantity=300,
            retail_price=150
        )

        product2 = Products(
            supply_id=2,
            product_name='Каркас кресла',
            specifications='каркас из бука',
            description='с виду ничего, но я бы подумал',
            picture='',
            purchase_price=1500,
            availability_in_stock=50,
            quantity=50,
            retail_price=2500
        )

        product3 = Products(
            supply_id=3,
            product_name='Декоративный элемент',
            specifications='30x32x16',
            description='можно дырку в мебели прикрыть',
            picture='',
            purchase_price=30,
            availability_in_stock=300,
            quantity=300,
            retail_price=70
        )

        product4 = Products(
            supply_id=4,
            product_name='Ткань мебельная',
            specifications='ткань мебельная',
            description='выглядит богато',
            picture='',
            purchase_price=70,
            availability_in_stock=20,
            quantity=20,
            retail_price=100
        )

        product5 = Products(
            supply_id=5,
            product_name='Стул',
            specifications='стул барный',
            description='как в Икее',
            picture='',
            purchase_price=1200,
            availability_in_stock=20,
            quantity=20,
            retail_price=2000
        )

        conn.add_all([product1, product2, product3, product4, product5])

        ordr1 = Orders(
            worker_id=6,
            product_id=5,
            order_placement_date='2024-01-15',
            order_execution_date='2024-01-15',
            client_id=1
        )

        ordr2 = Orders(
            worker_id=6,
            product_id=1,
            order_placement_date='2024-01-15',
            order_execution_date='2024-01-15',
            client_id=1
        )

        ordr3 = Orders(
            worker_id=7,
            product_id=2,
            order_placement_date='2024-01-17',
            order_execution_date='2024-01-17',
            client_id=2
        )

        ordr4 = Orders(
            worker_id=7,
            product_id=4,
            order_placement_date='2024-01-18',
            order_execution_date='2024-01-18',
            client_id=3
        )

        ordr5 = Orders(
            worker_id=6,
            product_id=3,
            order_placement_date='2024-01-20',
            order_execution_date='2024-01-20',
            client_id=4
        )

        conn.add_all([ordr1, ordr2, ordr3, ordr4, ordr5])
        conn.commit()

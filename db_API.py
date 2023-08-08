import sqlite3
import time


class Database(object):
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def execute(self, query):
        try:
            res = self.cursor.execute(query)
            self.connection.commit()
            if res:
                return res.fetchall()
        except Exception as e:
            print(f'err: {e}')


    def create_tables(self):
        query = '''CREATE TABLE IF NOT EXISTS persons(
        profile_ID CHAR(10) PRIMARY KEY,
        surname VARCHAR(64),
        name VARCHAR(32),
        patr VARCHAR(32),
        birthday TIMESTAMP,
        place_of_birth VARCHAR(64),
        nation VARCHAR(64),
        family_status VARCHAR(64),
        gender VARCHAR(64),
        division VARCHAR(10),
        position VARCHAR(32),
        mobile_number VARCHAR(24),
        phone_number VARCHAR(10),
        personal_business VARCHAR(10))      
        '''
        self.execute(query)

    def get_data(self, person_ID):
        data = self.execute(f"SELECT * FROM persons WHERE profile_ID = '{person_ID}'")
        return data

    def insert(self, data):
        query = f'''INSERT INTO persons VALUES(
        '{data['person_ID']}',
        '{data['surname']}',
        '{data['name']}',
        '{data['patr']}',
        {data['birthday']},
        '{data['place_of_birth']}',
        '{data['nation']}',
        '{data['family_status']}',
        '{data['gender']}',
        '{data['division']}',
        '{data['position']}',
        '{data['mobile_number']}',
        '{data['phone_number']}',
        '{data['personal_business']}'        
        )'''
        self.execute(query)


if __name__ == '__main__':
    database = Database('db.db')

    data = dict()
    data['rank'] = '<b>Лейтенант</b>'
    data['surname'] = '<b>ИВАНОВ</b>'
    data['name'] = '<b>Иван</b>'
    data['patr'] = '<b>Иванович</b>'
    data['person_ID'] = 'A-00000'
    data['birthday'] = time.time()
    data['place_of_birth'] = 'г. Москва'
    data['nation'] = 'русский'
    data['family_status'] = 'женат'
    data['gender'] = 'Мужской'
    data['division'] = 'в/ч 00001'
    data['position'] = 'Офицер отдела'
    data['mobile_number'] = '+7(999)199-77-55'
    data['phone_number'] = '13-37'
    data['personal_business'] = '1523'
    data["date_of_join"] = '2018'
    data['contract_from'] = '25.06.2019'
    data['contract_type'] = 'на 5 лет'
    data['contract_order'] = 'МО №625'
    data['contract_ord_data'] = '29.06.2019'
    data['allowance_form'] = 'Первая'
    data['allowance_num'] = 'Ю/55/6414'
    data['allowance_data'] = '24.09.18'

    database.insert(data)
    print(database.get_data('A-00000'))


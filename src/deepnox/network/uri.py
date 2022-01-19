

import re


def get_pgsql_datasource_from_springboot_settings(data: dict = None):
    if data is None:
        raise Exception('Any data')

    datasource = data.get('spring').get('datasource')
    DB_USER = datasource.get('username')
    DB_PASSWORD = datasource.get('password')

    DB_URI = datasource.get('url')  # jdbc:postgresql://pzbdacdh02.postgres.database.azure.com:5432/bacd00
    DB_HOST, DB_PORT, DB_NAME = re.match('jdbc:postgresql://(.*?):(.*?)/(.*)', DB_URI).groups()
    return DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
'''Indentify user'''

import database

def is_user_exists(db: database.DataBase, login) -> bool:
    '''Check if user exists.'''
    cursor = db.cursor()
    cursor.execute(f'SELECT count(*) FROM Users WHERE login = "{login}"')
    result = cursor.fetchall()[0][0]
    cursor.close()

    return result

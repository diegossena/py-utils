from inspect import getmembers
from typing import TypedDict, Union
# Utils


def getmember(obj, name):
    for _name, member in getmembers(obj):
        if name == _name:
            return member


def boolean(val):
    if isinstance(val, list) or isinstance(val, dict):
        return True
    return bool(val)  # (val in [0, None, False, '']) == False


def lodash_compact(array: list):
    return filter(boolean, array)


def lodash_groupBy(array: list, prop: str):
    result: dict[str, list] = {}
    for item in array:
        key = item[prop]
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result
#

class QueryBuilder_Select_OrderBy:
    def __init__(
        self,
        field: str,
        direction: str
    ):
        self.field = field
        self.direction = direction

class QueryBuilder_Select:
    def __init__(
        self,
        columns: list[str] = [],
        tables: list[str] = [],
        where: list[str] = [],
        orderBy: list[str] = [],
        limit=0,
    ):
        self.columns = columns
        self.tables = tables
        self.where = where
        self.orderBy = orderBy
        self.limit = limit

    def toSQL(self):
        return (
            # SELECT
            'SELECT '
            + ', '.join(self.columns)
            # FROM
            + ' FROM ' + ', '.join(self.tables)
            if len(self.tables)
            else ''
            # WHERE
            + ' WHERE' + ' '.join(self.where)
            if len(self.where)
            else ''
            # ORDER BY
            + ' ORDER BY ' + ', '.join(self.orderBy)
            if len(self.orderBy)
            else ''
            # LIMIT
            + ' LIMIT' + str(self.limit)
            if self.limit
            else ''
        )


def single(value: Union[str, QueryBuilder_Select], alias: str = None):
    return '{}{}'.format(
        '({})'.format(value.toSQL())
        if isinstance(value, QueryBuilder_Select)
        else (
            '*' if value == '*'
            else ''.join(['`', value.replace(r'/`/g', ''), '`'])
        ),
        '' if alias == None
        else ' AS ' + alias
    )


def where(
    field: str,
    operator: str,
    value: Union[str, int, QueryBuilder_Select]
):
    return ' '.join([
        single(field),
        operator,
        value
    ])


def join(
    table: str,
    on: list[where]
):
    return ''


class QueryBuilder:
    __query: QueryBuilder_Select

    def __init__(self, db_cursor, tableName: str):
        self.__db_cursor = db_cursor
        self.__query = QueryBuilder_Select(
            columns=['*'],
            tables=[single(value=tableName)],
        )

    def select(self, *columns: Union[str, QueryBuilder_Select]):
        self.__query.columns = [
            single(value=column)
            for column in columns
        ]
        return self

    def where(self, *statements: Union[str, list[str]]):
        expect_condition_bool = False
        for statement in statements:
            if isinstance(statement, list):
                if expect_condition_bool:
                    self.__query.where.append('AND')
                statement_length = len(statement)
                if not statement_length:
                    continue
                if statement_length > 1:
                    for i, stmt in enumerate(statement):
                        if isinstance(stmt, str) and stmt not in ['AND', 'OR', '(', 'LIKE']:
                            statement[i] = single(stmt)
                    if statement_length == 2:
                        statement = [statement[0], '=', statement[1]]
                    if self.__query.where != [] and self.__query.where[-1] not in ['AND', 'OR', '(']:
                        self.__query.where.append('AND')
                    self.__query.where.append(' '.join(statement))
                    continue
                statement = statement[0]
            statement = statement.upper()
            self.__query.where.append(statement)
        return self

    def orderBy(self, field: str, direction='ASC'):
        self.__query.orderBy.append(
            ' '.join([single(field), direction])
        )
        return self

    def first(self):
        self.__query.limit = 1
        return self

    def toSQL(self):
        return self.__query.toSQL()

    def __setRow(self, row):
        return dict(
            [
                (self.__db_cursor.column_names[i], value)
                for i, value in enumerate(row)
            ]
        )

    def __setRows(self, rows):
        return [
            self.__setRow(row)
            for row in rows
        ]

    def execute(self):
        sql = self.__query.toSQL()
        self.__db_cursor.execute(sql)
        if self.__query.limit == 1:
            result = self.__db_cursor.fetchone()
            return self.__setRow(result)
        result = self.__db_cursor.fetchall()
        return self.__setRows(result)


class ConnectionConfig(TypedDict):
    host: str
    user: str
    password: str
    database: str


class Config(TypedDict):
    client: str
    connection: ConnectionConfig


class Database:
    def __init__(self, config: Config):
        if 'client' not in config:
            raise Exception(
                "Required configuration option 'client' is missing."
            )
        if(config['client'] == 'mysql'):
            if('connection' in config):
                from mysql.connector import connect as mysql_connect
                self.__db_conn = mysql_connect(
                    host=config['connection']['host'],
                    user=config['connection']['user'],
                    password=config['connection']['password'],
                    database=config['connection']['database']
                )
                self.__db_cursor = self.__db_conn.cursor()
        else:
            raise Exception(
                "Invalid clientName given: {}".format(config['client']))

    def __call__(self, tableName: str):
        return QueryBuilder(self.__db_cursor, tableName)
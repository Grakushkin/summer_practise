# from psycopg2 import connect, Error
#
# connection = connect(
#             host="localhost",
#             user="postgres",
#             password="...",
#             database="postgres"
#             )
#
# def connect_to_n():
#     try:
#         connection.autocommit = True
#             #connection.autocommit = True
#        # with connection.cursor() as cursor:
#            # cursor.execute(
#             #    """CREATE TABLE sales_info(
#               #  sale_id serial,
#               #  product_id varchar(4),
#               #  product_price real,
#                # buyer_id varchar(4)
#                # )""")
#        # with connection.cursor() as cursor:
#             #cursor.execute(
#                # """INSERT INTO sales_info(
#                # sale_id,
#                # product_id,
#                # product_price,
#                 #buyer_id
#                 #)
#                 #VALUES
#                 #(default,1,100,1),
#                 #(default,1,100,2),
#                 #(default,2,200,1),
#                 #(default,2,200,2),
#                # (default,1,100,1),
#                # (default,1,100,1);
#                 #"""
#                # )
#
#     except Error as er:
#         print("Проблема с PostgreSQL,", er)
#     finally:
#         pass
# def connection_close():
#     connection = connect(
#         host="localhost",
#         user="postgres",
#         password="10A0403g_",
#         database="postgres"
#     )
#     if connection:
#         connection.close()





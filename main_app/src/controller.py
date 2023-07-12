import matplotlib.pyplot as plt
from db.connect import *
from psycopg2 import *

connection = connect(
             host="localhost",
             user="postgres",
             password="postgres",
             database="postgres"
            )

def linear_diagram():
    #Проверка соответствия длин списков
    with connection.cursor() as cursor:
        query = '''
                 SELECT product_name, count(sale_id),sale_year
                 FROM sales_info
                 GROUP BY sale_year,product_name
                '''
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        product_name = []
        product_count = []
        date = []
        for row in results:
            product_name.append(row[0])
            product_count.append(row[1])
            date.append(row[2])
        date = sorted(date)
        plt.plot(date, product_count)
        plt.xlabel('Dates')
        plt.ylabel('Product Counts')
        plt.title('Product Counts Over Time')
        plt.xticks(rotation=45)
        plt.grid()

        plt.show()

def pie_diagram() -> None:
    with connection.cursor() as cursor:
        query = '''
                SELECT product_name, SUM(product_price)
                FROM sales_info
                GROUP BY product_name
                '''
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()


        product_names = []
        product_prices = []
        for row in results:
            product_names.append(row[0])
            product_prices.append(row[1])

        # Создание круговой диаграммы
        plt.pie(product_prices, labels=product_names, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('Product sales by name')

        plt.show()
def bar_diagram() -> None:
    with connection.cursor() as cursor:
        query = '''
                    SELECT product_name, SUM(product_price)
                    FROM sales_info
                    GROUP BY product_name
                    '''
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        product_names = []
        product_prices = []
        for row in results:
            product_names.append(row[0])
            product_prices.append(row[1])

    plt.bar(product_names, product_prices)
    plt.xlabel('Product names')
    plt.ylabel('Product Prices')
    plt.title('Product sales by name')
    plt.show()







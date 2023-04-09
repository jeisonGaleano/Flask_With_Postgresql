from database.db import get_connection
from .entities.Chevrolet import Chevrolet
from .entities.Login import Login


class ChevroletModel():
    
    @classmethod
    def get_data_chevrolet(self):
        try:
            connection = get_connection()
            chevroletList = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT webscraperorder, webscraperstarturl, link, linkhref, precio, color, marca, modelo, ano FROM public.chevrolet")
                resultset = cursor.fetchall()

                for row in resultset:
                    movie = Chevrolet(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    chevroletList.append(movie.to_JSON())

            connection.close()
            return chevroletList
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_data_chevrolet(self, chevrolet):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public.chevrolet
                                (webscraperorder, webscraperstarturl, link, linkhref, precio, color, marca, modelo, ano)
                                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (chevrolet.web_scrapet_order, chevrolet.web_scrapet_start_url, chevrolet.link, chevrolet.link_href
                                                                                , chevrolet.precio, chevrolet.color, chevrolet.marca, chevrolet.modelo, chevrolet.ano))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_chevrolet(self, chevrolet):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM chevrolet WHERE webscraperorder = %s", (chevrolet.web_scraper_order,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def login_chevrolet(self, user, contrasena):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT usuario, contrasena FROM login WHERE usuario = %s and contrasena = %s ", (user, contrasena,))
                row = cursor.fetchone()

                movie = None
                if row != None:
                    movie = Login(row[0], row[1])
                    movie = movie.to_JSON()

            connection.close()
            return movie
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def create_user(self, login):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""
                               INSERT INTO public.login
                                (usuario, contrasena)
                                VALUES(%s, %s)""", (login.usuario, login.contrasena))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_data_chevrolet(self, chevrolet, webscraperorder):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public.chevrolet
                                (webscraperorder, webscraperstarturl, link, linkhref, precio, color, marca, modelo, ano)
                                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (chevrolet.web_scrapet_order, chevrolet.web_scrapet_start_url, chevrolet.link, chevrolet.link_href
                                                                                , chevrolet.precio, chevrolet.color, chevrolet.marca, chevrolet.modelo, chevrolet.ano))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
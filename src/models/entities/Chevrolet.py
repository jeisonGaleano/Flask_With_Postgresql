class Chevrolet():

    def __init__(self, web_scraper_order, web_scraper_start_url=None, link=None, link_href=None
                 , precio=None, color=None, marca=None, modelo=None, ano=None) -> None:
        self.web_scraper_order = web_scraper_order
        self.web_scraper_start_url = web_scraper_start_url
        self.link = link
        self.link_href = link_href
        self.precio = precio
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def __init__(self, precio=None, color=None, marca=None, modelo=None, ano=None) -> None:

        self.precio = precio
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def to_JSON(self):
        return {
            'web_scraper_order': self.web_scraper_order,
            'web_scraper_start_url': self.web_scraper_start_url,
            'link': self.link,
            'link_href': self.link_href,
            'precio': self.precio,
            'color': self.color,
            'marca': self.marca,
            'modelo': self.modelo,
            'ano': self.ano
        }
        
        
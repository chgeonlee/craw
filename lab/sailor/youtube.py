import os, time, random, json
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class Youtube():
    def __init__ ( self ):
        self.root = 'https://www.youtube.com'
    
    def path( self, node ="", leaf="" ):
        return os.path.join( self.root, node, leaf)

    def sleep( self ):
        time.sleep( random.uniform(1,3) )
    

    # parse rule 1
    def related_search_terms(self, driver, resources = [] , prefix = ""):
        resp = dict( data = [] )
        p = self.path()
        driver.get( p )
        el = driver.find_element( "name", "search_query" )
        
        for idx, obj in enumerate( resources ):
            pack = dict( uuid = obj[ 'id' ], response = [] )
            el.click() #for focus
            self.sleep()
            el.send_keys(obj['name'] + " " )
            self.sleep()
            for row in driver.find_elements( By.CLASS_NAME, 'sbsb_c' ):
                soup = BeautifulSoup( row.get_attribute("innerHTML" ) , 'html.parser',from_encoding='cp949' )                
                for n in soup.select( ".sbqs_c" ):
                    pack[ 'response' ].append( n.text )
                    print( 'append', n.text )

            resp['data'].append( pack )
            el.clear()
            self.sleep()

        with open( os.path.join( "/".join(os.path.realpath( __file__ ).split( "/")[: -1]), 'output', 'related_search_terms_{}.json'.format(prefix) ), 'w', encoding = 'UTF-8' ) as f:
            json.dump( resp, f, ensure_ascii = False )


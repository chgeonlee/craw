from selenium import webdriver
import requests, os, csv, argparse
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from youtube import Youtube
from selenium.webdriver.chrome.options import Options

class Scrap():

    def __init__(self):
        
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  

        self.driver = webdriver.Chrome( service = Service(ChromeDriverManager().install() ), options = options)        
        pass

    def parse( self, html ):
        pass

    def test( self ) :
        pass

    def youtube_related_search_terms( self, indexing = 0 ):
        unit = 100
        
        path = os.path.join( "/".join(os.path.realpath( __file__ ).split( "/")[: -1]))
        tot = 0
        disk = []
        with open( os.path.join( path, 'resources', 'test.tsv' ), 'r', newline ='' ) as f:
            nset = [ x for x in csv.reader(f, delimiter='\t', quotechar='|') ]
            for row in nset[ 1: ]:
                if row[ 3 ] === '1차 통합 완료':
                    game_id = row[ 1 ]
                    game_name = row[ 2 ]
                    disk.append( dict( id = game_id, name = game_name ))
        
        print( '{} - {} \t\t totle: {}'.format( indexing * unit, (indexing + 1)*unit, len( nset ) ) )

        Youtube().related_search_terms( driver = self.driver, resources = disk[ indexing * 100: 100* (indexing + 1) ], prefix = str( indexing ) )




def main():

    parser = argparse.ArgumentParser( description = "")
    parser.add_argument( '-i', help="index" )
    args = parser.parse_args()
    print( args.i )
    
    scrap = Scrap()
    scrap.youtube_related_search_terms(args.i)

if __name__ == '__main__':
    main()
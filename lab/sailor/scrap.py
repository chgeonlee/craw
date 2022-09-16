from selenium import webdriver
import requests, os, csv
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

    def youtube_related_search_terms( self ):
        path = os.path.join( "/".join(os.path.realpath( __file__ ).split( "/")[: -1]))
        tot = 0
        with open( os.path.join( path, 'resources', 'test.tsv' ), 'r', newline ='' ) as f:
            nset = [ x for x in csv.reader(f, delimiter='\t', quotechar='|') ]
            for row in nset[ 1: ]:
                #print(', '.join(row))
                game_id = row[ 1 ]
                game_name = row[ 2 ]

                if( row[ 3 ]) == '3차 작업 대상':
                    
                    tot += 1
        
        


        # test = [ dict( id = "game_id", name = "엘든링"),
        #     dict( id = "game_id", name = "대항해시대2" )]
        # Youtube().related_search_terms( driver = self.driver, resources = test, prefix = '1' )
        pass





def main():
    scrap = Scrap()
    scrap.youtube_related_search_terms()

if __name__ == '__main__':
    main()
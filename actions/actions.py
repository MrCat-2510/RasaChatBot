# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests 
from bs4 import BeautifulSoup


class ActionReadNews(Action):

    def name(self) -> Text:
        return "action_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            URL = 'https://www.bbc.com/news'
            website = requests.get(URL)
            results = BeautifulSoup(website.content, 'html.parser')
            top_news = results.find("a", class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor", href=True)
            top_new_url = "https://www.bbc.com"+top_news["href"]

            dispatcher.utter_message(text="Tôi có tin tức nổi bật hôm nay cho bạn: ")
            dispatcher.utter_message(text=top_new_url)
        except:
            dispatcher.utter_message(text="Xin lỗi, hôm nay không có tin tức cho bạn: ")
            
        return []

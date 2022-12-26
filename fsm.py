from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message, push_message, send_movie_info, send_movie_detail, send_movie_rank, send_movie_theater, send_movie_theaterarea, send_image_url, send_image_carousel
import pandas as pd


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        
    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() != "more"

    def is_going_to_movieinfo(self, event):
        text = event.message.text
        return text.lower() == "movieinfo"

    def is_going_to_detail(self, event):
        text = event.message.text
        return True
    
    def is_going_to_rank(self, event):
        text = event.message.text
        return text.lower() == "rank"
    
    def is_going_to_theater(self, event):
        text = event.message.text
        return text.lower() == "theater"
    
    def is_going_to_theaterdetail(self, event):
        text = event.message.text
        return True
    
    def is_going_to_backtomenu(self, event):
        text = event.message.text
        return text.lower() == "menu"
    
    def is_going_to_meme(self, event):
        text = event.message.text
        return text.lower() == "more"

    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        userid = event.source.user_id

        img = 'https://www.syracuse.com/resizer/Cj7sp4D9A2b_4IW--YiyJgJKUiQ=/1280x0/smart/cloudfront-us-east-1.images.arcpublishing.com/advancelocal/Z4JXG2AZEZB55IGXLKTBGGXTDQ.jpeg'
        title = 'FilmFinder'
        uptext = 'What information are you looking for ?'
        labels = ['Rank', 'Films This Week', 'Theater']
        texts = ['rank', 'movieinfo', 'theater']
        send_button_message(userid, img, title, uptext, labels, texts)
        
    
    def on_enter_movieinfo(self, event):
        print("I'm entering movieinfo")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_movie_info(reply_token, userid)
            
        msg = "Please enter the film number you want to know about."
        push_message(userid, msg)
        
    def on_enter_detail(self, event):
        print("I'm entering detail")

        reply_token = event.reply_token
        userid = event.source.user_id
        movie_num = event.message.text
        try:
            movie_num = int(movie_num)
            send_movie_detail(reply_token, userid, movie_num)
            img = 'https://cdn.vox-cdn.com/thumbor/GI06H-weKLFDuWTOgF_2TTK52Ck=/0x0:6720x4480/1820x1213/filters:focal(2717x1620:3791x2694):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/60141553/shutterstock_1068876371.0.jpg'
            title = 'Find more'
            uptext = 'Find more films\' information or go back to menu'
            labels = ['Films This Week', 'Back to Menu']
            texts = ['movieinfo', 'menu']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message(userid, "Wrong format. Please try again")
            print("I'm leaving detail")
            self.go_back(event)

    def on_enter_rank(self, event):
        print("I'm entering rank")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_movie_rank(reply_token, userid)
        
        self.go_back(event)


    def on_enter_theater(self, event):
        print("I'm entering theater")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_movie_theaterarea(reply_token, userid)
        
        msg = "Please enter the areaID your theater in."
        push_message(userid, msg)
            
    def on_enter_theaterdetail(self, event):
        print("I'm entering theaterdetail")

        reply_token = event.reply_token
        userid = event.source.user_id
        area_num = event.message.text
        try:
            send_movie_theater(reply_token, userid, area_num)
            self.go_back(event)
        except:
            push_message(userid, "Wrong format. Please try again")
            print("I'm leaving theaterdetail")
            event.message.text = "theater"
            self.advance(event)
            
    def on_enter_meme(self, event):
        print("I'm entering meme")

        reply_token = event.reply_token
        userid = event.source.user_id
        img = 'https://a.pinatafarm.com/1920x950/fce2488035/kylo-ren-more.jpg'
        send_image_url(reply_token, img)
        
        self.go_back(event)

        

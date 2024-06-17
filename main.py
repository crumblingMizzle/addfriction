from manim import *
from manim_slides import Slide

FONT_SIZE_HEADER = 36
FONT_SIZE_BODY = 48
HEADER_LOCATION = UP * 3.5
IMAGE_HEIGHT = 3

class MainScene(Slide):
    def set_header(self, content, centered=False):
        new_header = Text(content, font_size=FONT_SIZE_HEADER)
        if not centered:
            new_header.move_to(HEADER_LOCATION)
        if hasattr(self, "header_text"):
            self.play(Transform(self.header_text, new_header))
        else:
            self.play(Write(new_header))
            self.header_text = new_header
    
    def set_image(self, filename, height=IMAGE_HEIGHT):
        if filename is None or (hasattr(self, "img") and self.img is not None):
            self.play(FadeOut(self.img))
            self.img = None
        if filename is not None:
            new_image = ImageMobject(filename)
            new_image.height = height
            self.img = new_image
            self.play(FadeIn(self.img))
    
    def set_bullet(self, content, position=[0,0,0]):
        if not hasattr(self, "blist") or self.blist is None:
            new_blist = BulletedList(content, font_size=FONT_SIZE_BODY)
            new_blist.move_to(position)
            self.play(Write(new_blist))
            self.blist = VGroup(new_blist)
            self.blist.arrange(DOWN, center=False, aligned_edge=LEFT)
        elif content is not None:
            new_blist = BulletedList(content, font_size=FONT_SIZE_BODY)
            self.blist.add(new_blist)
            self.blist.arrange(DOWN, center=False, aligned_edge=LEFT)
            self.play(Write(new_blist))
        else:
            self.play(FadeOut(self.blist))
            self.blist = None
    
    
    def slide_title(self):
        if self.slide_state == 0:
            self.set_header("Game Design & Addiction", True)
            self.subtitle = Text("Katie M", font_size=FONT_SIZE_HEADER-4)
            self.subtitle.move_to(DOWN)
            self.play(Write(self.subtitle))
        else:
            self.play(FadeOut(self.subtitle))
            return True
        self.slide_state += 1
        return False

    def slide_gamification(self):
        IMAGE_HEIGHT = 2
        if self.slide_state == 0:
            self.set_header("\"Gamification\" has breached containment...")
        elif self.slide_state == 1:
            self.set_image("images/duolingo.png")
        elif self.slide_state == 2:
            self.set_image("images/applefitness.png")
        elif self.slide_state == 3:
            self.set_image("images/sbux.png")
        elif self.slide_state == 4:
            self.set_image("images/likes.png")
        else:
            self.set_image(None)
            return True
        self.slide_state += 1
        return False
    
    def slide_games_are_jobs(self):
        if self.slide_state == 0:
            self.set_header("...and come back around full circle")
        elif self.slide_state == 1:
            self.set_bullet("At some point, games became jobs", LEFT * 2.9 + UP * 1)
        elif self.slide_state == 2:
            self.set_bullet("How many people do you know who ritualistically log on to\n\ngames they don't really enjoy?")
        elif self.slide_state == 3:
            self.set_bullet("Does it really stop there?")
        else:
            self.set_bullet(None)
            return True
        self.slide_state += 1
        return False
    
    def slide_engagement(self):
        if self.slide_state == 0:
            self.set_header("What do players want in a game?")
        elif self.slide_state == 1:
            self.set_bullet("Players are principally searching for engagement", LEFT * 1.5 + UP * 2)
        elif self.slide_state == 2:
            self.set_bullet("You can get your players engaged in many ways")
        elif self.slide_state == 3:
            self.set_bullet("To keep them engaged, the game must be well designed")
        else:
            self.set_bullet(None)
            return True
        self.slide_state += 1
        return False
    
    def slide_psychology(self):
        if self.slide_state == 0:
            self.set_header("Shortcut solution")
        elif self.slide_state == 1:
            self.set_bullet("Making a game engaging on its own merits is difficult!", LEFT * 0.9 + UP * 1)
        elif self.slide_state == 2:
            self.set_bullet("Games created by corporations tend to short-circuit this\n\n issue by weaponizing their players' psychology")
        elif self.slide_state == 3:
            self.set_bullet("The human animal will clamor and scramble for any scrap\n\n of dopamine available from \"number go up\"")
        else:
            self.set_bullet(None)
            return True
        self.slide_state += 1
        return False
    
    def slide_dev_boon(self):
        if self.slide_state == 0:
            self.set_header("Addictive to play, addictive to create")
        elif self.slide_state == 1:
            self.set_bullet("You're making the player \"feel good\"", LEFT * 2.7 + UP * 1.5)
        elif self.slide_state == 2:
            self.set_bullet("Addiction can help your player push through tough times")
        elif self.slide_state == 3:
            self.set_bullet("Craving the established addiction can bring them back\n\nfor more play sessions")
        elif self.slide_state == 4:
            self.set_bullet("Staying engaged with the game longer will increase the\n\nchances they end up seeing more of the game")
        else:
            self.set_bullet(None)
            return True
        self.slide_state += 1
        return False
    
    def slide_journos(self):
        if self.slide_state == 0:
            self.set_header("The critics agree!")
        elif self.slide_state == 1:
            self.set_image("images/catcafe.png")
        elif self.slide_state == 2:
            self.set_image("images/genshin.png")
        elif self.slide_state == 3:
            self.set_image("images/re3.png")
        elif self.slide_state == 4:
            self.set_image("images/rf5.png")
        else:
            self.set_image(None)
            return True
        self.slide_state += 1
        return False
    
    def slide_define_bad(self):
        if self.slide_state == 0:
            self.set_header("Where to draw the mechanical line?")
        elif self.slide_state == 1:
            self.set_bullet("There is consensus on the damaging effects of gambling/\n\nlootboxes, even some legal pushback", LEFT * 0.7 + UP * 1.5)
        elif self.slide_state == 2:
            self.set_bullet("But what about the thousands of human lives spent doing\n\ndailies?")
        elif self.slide_state == 3:
            self.set_bullet("Consider a JRPG with dozens hours of grinding out\n\nexperience points and skill trees")
        elif self.slide_state == 4:
            self.set_bullet("Or an open-world collectathon game with an obscene number\n\nof sidequests and achievements")
        else:
            self.set_bullet(None)
            return True
        self.slide_state += 1
        return False
    
    def slide_conclusion(self):
        if self.slide_state == 0:
            self.set_header("To be clear: this is not a judgement")
        elif self.slide_state == 1:
            self.set_bullet("It's not fair to call a game, a studio, or an individual\n\n\"bad\" or \"immoral\" for one mechanic", LEFT * 1 + UP * 1)
        elif self.slide_state == 2:
            self.set_bullet("Ultimately you need to respect your players and treat them\n\nas people rather than a bunch of chemicals to exploit")
        elif self.slide_state == 3:
            self.set_bullet("Remember: engagement != fun, but fun = engagement!")
        else:
            self.set_bullet(None)
            return True
        self.slide_state += 1
        return False

    def slide_thanks(self):
        if self.slide_state == 0:
            self.set_header("Thank you!", True)
            self.subtitle = Text("Slides: https://crumblingmizzle.github.io/addfriction/\n\nSource code: https://github.com/crumblingMizzle/addfriction", font_size=FONT_SIZE_HEADER-12, line_spacing=0)
            self.subtitle.move_to(DOWN * 3)
            self.play(Write(self.subtitle))
        else:
            self.play(FadeOut(self.subtitle, self.header_text))
            return True
        self.slide_state += 1
        return False
    

    def construct(self):
        self.slides = [
            self.slide_title,
            self.slide_gamification,
            self.slide_games_are_jobs,
            self.slide_engagement,
            self.slide_psychology,
            self.slide_dev_boon,
            self.slide_journos,
            self.slide_define_bad,
            self.slide_conclusion,
            self.slide_thanks,
        ]
        self.current_slide = 0
        self.slide_state = 0
        self.should_loop = False

        self.next_slide(loop=self.should_loop)
        for slide in self.slides:
            while not slide():
                self.next_slide(loop=self.should_loop)
            self.current_slide += 1
            self.slide_state = 0

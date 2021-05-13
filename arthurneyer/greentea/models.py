from django.db import models

# Create your models here.
class ArtisticIp(models.Model):

    lay_a = models.CharField(max_length=3)
    lay_b = models.CharField(max_length=3)
    lay_c = models.CharField(max_length=3)
    lay_d = models.CharField(max_length=3)

    def color(self):
        return self.lay_a_color()

    def lay_a_color(self):
        number = int(self.lay_a)
        if int(number)*3 <= 255:
            primary = 'RED'
        elif int(number)*3 <= 255*2:
            primary = 'GREEN'
        else:
            primary = 'BLUE'


        if primary == 'RED':
            others = ['GREEN', 'BLUE']

            RED = number*3%255
            GREEN = (7*255)/(abs(number%255 -256))
            BLUE = (7*255)/((number%255)+1)

        elif primary == 'GREEN':
            others = ['BLUE', 'RED']

            GREEN = number*1.5%255
            BLUE = (7*255)/(abs(number%255 -256))
            RED = (7*255)/((number%255)+1)

        else:
            others = ['RED', 'GREEN']

            BLUE = number%255
            RED = (7*255)/(abs(number%255 -256))
            GREEN = (7*255)/((number%255)+1)

        if RED > 255:
            RED= 255
        if GREEN > 255:
            GREEN= 255
        if BLUE > 255:
            BLUE= 255

        class Color:
            def __init__(self, RED, GREEN, BLUE):
                self.RED = RED
                self.GREEN = GREEN
                self.BLUE = BLUE

        return Color(RED, GREEN, BLUE)


    def dict(self):
        return {
            'lay_a': self.lay_a,
            'lay_b': self.lay_b,
            'lay_c': self.lay_c,
            'lay_d': self.lay_d,
        }

    def json(self):
        return str(self.dict())

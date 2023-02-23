from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen 
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
import random
from kivy.clock import Clock
from time import strftime
from kivy.uix.checkbox import CheckBox
import re
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

Window.size = (375,700)
#sports tabbedpanel
class OneAbove(TabbedPanel):
    def resetdrill(self):
        #resets from the drills
        FourWay.oneon = False
        SquareDrill.oneon = False
        CODDrill.oneon = False
        FourWay.oneon = False
        HipFlip.oneon = False
        #timersstopper
        StopWatch.oneon = True
        IntervalTimer.oneon = True
        TabataTimer.oneon = True
        DingTimer.oneon = True
        ProgTimer.oneon = True
        LineTimer.oneon = True
        #condistopper
        BeepTest.oneon = True
        #visualstoppere
        ColorTimer.oneon = True
        OneClrTimer.oneon = True

    def timersreset(self):
        #drillsstopper
        SquareDrill.oneon = True
        CODDrill.oneon = True
        FourWay.oneon = True
        HipFlip.oneon = True
        #condistopper
        BeepTest.oneon = True
        #timersseter
        StopWatch.oneon = False
        IntervalTimer.oneon = False
        TabataTimer.oneon = False
        DingTimer.oneon = False
        ProgTimer.oneon = False
        LineTimer.oneon = False
        #visualstoppere
        ColorTimer.oneon = True
        OneClrTimer.oneon = True


    def condireset(self):
        #drillstoppers
        SquareDrill.oneon = True
        CODDrill.oneon = True
        FourWay.oneon = True
        HipFlip.oneon = True
        #timerstoppers
        StopWatch.oneon = True
        IntervalTimer.oneon = True
        TabataTimer.oneon = True
        DingTimer.oneon = True
        ProgTimer.oneon = True
        LineTimer.oneon = True
        #condireseter¨
        BeepTest.oneon = False
        #visualstoppere
        ColorTimer.oneon = True
        OneClrTimer.oneon = True

    def visualreset(self):
        #drillstoppere
        SquareDrill.oneon = True
        CODDrill.oneon = True
        FourWay.oneon = True
        HipFlip.oneon = True
        #timerstoppers
        StopWatch.oneon = True
        IntervalTimer.oneon = True
        TabataTimer.oneon = True
        DingTimer.oneon = True
        ProgTimer.oneon = True
        LineTimer.oneon = True
        #condistopper
        BeepTest.oneon = True
        #visualresetere
        ColorTimer.oneon = False
        OneClrTimer.oneon = False

class MainScreen(Screen):
    pass

class SquareDrill(Screen):
    sqdon = True
    img_src = "images/squaredrill.png"
    sqd1 = "images/squaredrill1.png"
    sqd2 = "images/squaredrill2.png"
    sqd3 = "images/squaredrill3.png"
    sqd4 = "images/squaredrill4.png"
    #squaredrill
    oneon = False

    def toggle(self, *args):
        #stringformatting main cd
        nl = checker(self.ids.text_input.text)
        il = checker(self.ids.interval.text)
        tl = checker(self.ids.sqdintervalto.text)
        if tl and il and nl: #checker to
            if self.ids.text_input.text != "00:00" and self.ids.text_input.text != "Enter Time":
                if self.ids.button.text == "start":
    
                    self.t = self.ids.interval.text
                    self.t = int(self.t)

                    self.z = self.ids.sqdintervalto.text
                    self.z = int(self.z)

                    if self.ids.interval.text =="":
                        self.ids.interval.text = "1"
                        self.t = 1
                    if self.ids.sqdintervalto.text == "":
                        self.ids.sqdintervalto.text = "1"
                        self.z = 1

                    if self.t > self.z:
                        on = False
                    elif self.t == self.z:
                        i = self.t 
                        on = True

                    elif self.t != self.z:
                        
                        on = True
                        
                        i = random.randint(self.t,self.z)
                        i = int(i)

                    if on:
                        self.ids.button.text = "pause"
                        if self.ids.text_input.text != "00:00":
                            Clock.schedule_interval(self.start, 1)
                            Clock.schedule_once(self.playsound)

                            yy = (splitter(self.ids.text_input.text))
                            self.sqdfull_seconds= int(yy)
                        

                elif self.ids.button.text == "pause":
                    self.sqdon = False
                    self.ids.button.text ="resume"

                elif self.ids.button.text == "resume":
                    self.ids.button.text = "pause"
                    self.sqdon = True
            elif self.ids.text_input.text == "00:00":
                self.ids.text_input.text = "Enter Time"
                self.ids.text_input.font_size = 50

        else:#her er den checker
            self.ids.text_input.text = "00:00"
            self.ids.interval.text = "1"
            self.ids.sqdintervalto.text = "1"
                    
            
    def refereshsqd(self, *args): #sets the time back to 00:00 when entertime
        if self.ids.text_input.text == "Enter Time":
            self.ids.text_input.text = "00:00"##problem area
            self.ids.text_input.font_size = 100

    def thesch(self, *args):
        i = random.randint(self.t,self.z)
        Clock.schedule_interval(self.playsound, i)

    def start(self, *args):
        #countdown
        if self.sqdon:
            self.sqdfull_seconds -= 1
            minutes, seconds = divmod(self.sqdfull_seconds, 60)
            sqdshow=(f"{minutes:02d}:{seconds:02d}")
            self.ids.text_input.text = sqdshow
            if self.oneon:
                self.reset()

            if self.sqdfull_seconds == 0:
                myapp.goodjobs.play()
                self.reset()
                self.ids.text_input = self.sqi 
                
    #sqdreset
    def reset(self, *args):
        Clock.unschedule(self.start)
        Clock.unschedule(self.playsound)
        Clock.unschedule(self.thesch)
        self.ids.button.text = "start"
        self.ids.text_input.text = "00:00"
        self.i = self.ids.interval.text
        self.ids.interval.text = "1"
        self.ids.sqdintervalto.text = "1"
        self.ids.bongbong.source = self.img_src
        self.run_once = True
        self.running = False
        
        
    sounds = [1,2,3,4]
    
    def playsound(self, *args):
        Clock.unschedule(self.playsound)
        Clock.schedule_once(self.thesch)
        if self.sqdon:
            t = random.randrange(len(self.sounds)-1)
            self.sounds.append(self.sounds.pop(t)) 
            x = (self.sounds[-1])     
            if x == 1:
                myapp.en.play()
                self.ids.bongbong.source = self.sqd1
            elif x == 2:
                myapp.to.play()
                self.ids.bongbong.source = self.sqd2
            elif x == 3:
                myapp.tre.play()
                self.ids.bongbong.source = self.sqd3
            elif x == 4:
                myapp.fire.play()
                self.ids.bongbong.source = self.sqd4



class CODDrill(Screen):
    oneon = False
    numbers = "images/lipdrillnumbers.png"
    hipimgsrc = "images/lipdrill.png"
    flipdrill1 = "images/lipdrill1.png"
    flipdrill2 = "images/lipdrill2.png"
    flipdrill3 = "images/lipdrill3.png"
    flipdrill4 = "images/lipdrill4.png"
    flipdrill5 = "images/lipdrill5.png"
    flipdrill6 = "images/lipdrill6.png"
    flipdrill7 = "images/lipdrill7.png"
    flipdrill8 = "images/lipdrill8.png"
    run_oncehip = True
    def flipchooser(self, valuee, *args):
        if valuee == "Direction":
            self.flipdirection = True
            self.flipnumbers = False
            self.ids.hipimage.source = self.hipimgsrc

        elif valuee == "Numbers":
            self.flipnumbers = True
            self.flipdirection = False
            self.ids.hipimage.source = self.numbers
            
    hipon = True
    def hiptoggle(self, *args):
        nl = checker(self.ids.hipinput.text)
        il = checker(self.ids.hipinterval.text)
        tl = checker(self.ids.hipintervalto.text)
        if tl and il and nl: #checker to
            if self.ids.hipinput.text != "00:00" and self.ids.flipspinner.text !="mode":
                if self.ids.hipbutton.text == "start":
                    self.t = self.ids.hipinterval.text
                    self.t = int(self.t)

                    self.z = self.ids.hipintervalto.text
                    self.z = int(self.z)

                    if self.ids.hipinterval.text =="":
                        self.ids.hipinterval.text = "1"
                        self.t = 1
                    if self.ids.hipintervalto.text == "":
                        self.ids.hipintervalto.text = "1"
                        self.z = 1

                    if self.t > self.z:
                        on = False
                    elif self.t == self.z:
                        i = self.t 
                        on = True

                    elif self.t != self.z:
                        i = random.randint(self.t,self.z)
                        i = int(i)
                        on = True

                    if on:
                        if self.run_oncehip:
                            self.ids.hipbutton.text = "pause"
                            self.run_oncehip = False
                        #stringformatting main cd
                            if self.ids.hipinput.text != "00:00":
                                Clock.schedule_once(self.hipplaysound)
                                Clock.schedule_interval(self.hipstart, 1)

                                yy = (splitter(self.ids.hipinput.text))
                                self.hipfull_seconds= int(yy)

                elif self.ids.hipbutton.text == "pause":
                    self.hipon = False
                    self.ids.hipbutton.text = "resume"
                elif self.ids.hipbutton.text == "resume":
                    self.hipon = True
                    self.ids.hipbutton.text = "pause"
            elif self.ids.hipinput.text == "00:00":
                self.ids.hipinput.text = "missing input"#her
                self.ids.hipinput.font_size = 50

        else:#her er den checker
            self.ids.hipinput.text = "00:00"
            self.ids.hipinterval.text = "1"
            self.ids.hipintervalto.text = "1"
    def refereshsqd(self, *args): #sets the time back to 00:00 when entertime
        if self.ids.hipinput.text == "missing input":
            self.ids.hipinput.font_size = 100
            self.ids.hipinput.text = "00:00"##problem area
    def thesch(self, *args):
        i = random.randint(self.t,self.z)
        Clock.schedule_interval(self.hipplaysound, i)


    def hipstart(self, *args):
        #countdown
        if self.hipon:
            self.hipfull_seconds -= 1
            self.run_oncehip = False
            minutes, seconds = divmod(self.hipfull_seconds, 60)
            hipshow=(f"{minutes:02d}:{seconds:02d}")
            self.ids.hipinput.text = hipshow
            if self.oneon: ##resetr ved tabbedpanelclick
                self.hipreset()

            if self.hipfull_seconds == 0:
                self.hipgj()
                Clock.unschedule(self.hipstart)
                Clock.unschedule(self.hipplaysound)
                self.ids.hipbutton.text = "start"
  
    #hipreset
    def hipreset(self, *args):
        self.ids.hipbutton.text = "start"
        #self.running = False
        Clock.unschedule(self.thesch)
        Clock.unschedule(self.hipplaysound)
        Clock.unschedule(self.hipstart)
        self.ids.hipinput.text = "00:00"
        self.ids.hipinterval.text = "1"
        self.ids.hipintervalto.text = "1"
        self.ids.hipimage.source = self.numbers

        self.run_oncehip = True
    def hipgj(self):
        Clock.unschedule(self.hipplaysound)
        #LAV EN GET OUT PLAY HERself.getout.play()
        myapp.goodjobs.play()
        self.run_oncehip = True
        self.it = self.ids.hipinterval.text
        
    soundss = [1,2,3,4,5,6,7,8]
    #måske lav en option som kan være 1,2,3,4,5 eller flip shuffle osv.
    def hipplaysound(self, *args):
        
        if self.hipon and self.ids.flipspinner.text !="mode":
            Clock.unschedule(self.hipplaysound)
            Clock.schedule_once(self.thesch)
            if self.flipdirection:
                t = random.randrange(len(self.soundss)-1)
                self.soundss.append(self.soundss.pop(t)) 
                x = (self.soundss[-1])  
                #her er det hvis man skal bruge dierctions altså op, ned, højre osv   
                if x == 1:
                    myapp.forward.play()
                    
                    #self.ids.bongbong.source = self.sqd1
                elif x == 2:
                    myapp.back.play()

                    #self.ids.bongbong.source = self.sqd2
                elif x == 3:
                    myapp.left.play()
                    #self.ids.bongbong.source = self.sqd3
                elif x == 4:
                    myapp.right.play()
                    #self.ids.bongbong.source = self.sqd4
                elif x == 5:
                    myapp.flipleft.play()

                elif x == 6:
                    myapp.flipright.play()
                    
                elif x == 7:
                    myapp.downright.play()
                elif x == 8:
                    
                    myapp.downleft.play()
                #flip 


            elif self.flipnumbers:
                t = random.randrange(len(self.soundss)-1)
                self.soundss.append(self.soundss.pop(t)) 
                x = (self.soundss[-1])     
                if x == 1:
                    myapp.en.play()
                    self.ids.hipimage.source = self.flipdrill1
                elif x == 2:
                    myapp.to.play()
                    self.ids.hipimage.source = self.flipdrill2
                elif x == 3:
                    myapp.tre.play()
                    self.ids.hipimage.source = self.flipdrill3
                elif x == 4:
                    myapp.fire.play()
                    self.ids.hipimage.source = self.flipdrill4
                elif x == 5:
                    myapp.fem.play()
                    self.ids.hipimage.source = self.flipdrill5
                elif x == 6:
                    myapp.seks.play()
                    self.ids.hipimage.source = self.flipdrill6
                elif x == 7:
                    myapp.syv.play()
                    self.ids.hipimage.source = self.flipdrill7
                elif x == 8:
                    myapp.otte.play()
                    self.ids.hipimage.source = self.flipdrill8
            
class FourWay(Screen):
    fouron = True
    img_src = "images/efourwaydrillbutton.png"
    four1 = "images/efourwaydrillleft.png"
    four2 = "images/efourwaydrillright.png"
    four3 = "images/efourwaydrilldown.png"
    four4 = "images/efourwaydrillup.png"
    oneon = False
    def fourtoggle(self, *args):
        #stringformatting main cd
        nl = checker(self.ids.fourinput.text)
        il = checker(self.ids.fourinterval.text)
        tl = checker(self.ids.fourintervalto.text)
        if tl and il and nl: #checker to
            if self.ids.fourinput.text != "00:00" and self.ids.fourinput.text != "Enter Time":
                if self.ids.fourbutton.text == "start":
                    self.t = self.ids.fourinterval.text
                    self.t = int(self.t)
                    self.z = self.ids.fourintervalto.text
                    self.z = int(self.z)
                    if self.ids.fourinterval.text == "":
                        self.ids.fourinterval.text = "1"
                        self.t = 1
                    if self.ids.fourintervalto.text == "":
                        self.ids.fourintervalto.text = "1"
                        self.z = 1

                    if self.t > self.z:
                        dong = False
                    elif self.t == self.z:
                        i = self.t 
                        dong = True

                    elif self.t != self.z:
                        i = random.randint(self.t,self.z)
                        i = int(i)
                        dong = True

                    if dong == True: 
                        self.ids.fourbutton.text = "pause"
                        Clock.schedule_interval(self.fourstart, 1)
                        if self.ids.fourinput.text != "00:00":
                            Clock.schedule_once(self.fourplaysound)

                            yy = (splitter(self.ids.fourinput.text))
                            self.fourfull_seconds= int(yy)   
                                        
                    
                elif self.ids.fourbutton.text == "pause":
                    self.fouron = False
                    self.ids.fourbutton.text ="resume"

                elif self.ids.fourbutton.text == "resume":
                    self.ids.fourbutton.text = "pause"
                    self.fouron = True
            elif self.ids.fourinput.text == "00:00":
                self.ids.fourinput.text = "Enter Time"
                self.ids.fourinput.font_size = 50
        else:#her er den checker
            self.ids.fourinput.text = "00:00"
            self.ids.fourinterval.text = "1"
            self.ids.fourintervalto.text = "1"

    def refereshfour(self, *args):
        if self.ids.fourinput.text == "Enter Time":
            self.ids.fourinput.text = "00:00"
            self.ids.fourinput.font_size = 100


    def thesch(self, *args):
        i = random.randint(self.t,self.z)
        Clock.schedule_once(self.fourplaysound, i)

    def fourstart(self, *args):
        #countdown
        if self.fouron:
            self.fourfull_seconds -= 1

            minutes, seconds = divmod(self.fourfull_seconds, 60)
            fourshow=(f"{minutes:02d}:{seconds:02d}")
            self.ids.fourinput.text = fourshow
            if self.oneon:
                self.fourreset()

            if self.fourfull_seconds == 0:
                myapp.goodjobs.play()
                self.fourreset()
                
    
    def fourreset(self, *args):
        Clock.unschedule(self.thesch)
        Clock.unschedule(self.fourstart)
        Clock.unschedule(self.fourplaysound)
        self.ids.fourbutton.text = "start"
        self.ids.fourinput.text = "00:00"
        self.ids.fourinterval.text = "1"
        self.ids.fourintervalto.text = "1"
        self.i = self.ids.fourinterval.text
        #self.ids.fourimg.source = self.img_src
        self.run_once = True
        self.running = False
        self.ids.fourimg.source = self.img_src
        
        
    sounds = [1,2,3,4]
    
    def fourplaysound(self, *args):
        Clock.schedule_once(self.thesch)
        if self.fouron:
            t = random.randrange(len(self.sounds)-1)
            self.sounds.append(self.sounds.pop(t)) 
            x = (self.sounds[-1])     
            if x == 1:
                myapp.left.play()
                self.ids.fourimg.source = self.four1
            elif x == 2:
                myapp.right.play()
                self.ids.fourimg.source = self.four2
            elif x == 3:
                myapp.forward.play()
                self.ids.fourimg.source = self.four3
            elif x == 4:
                myapp.back.play()
                self.ids.fourimg.source = self.four4

class HipFlip(Screen):
    dbon = True
    img_src = "images/erealflipdrill.png"
    oneon = False
    def dbtoggle(self, *args):
        #stringformatting main cd
        nl = checker(self.ids.dbinput.text)
        il = checker(self.ids.dbinterval.text)
        tl = checker(self.ids.dbintervalto.text)
        if tl and il and nl: #checker to
            if self.ids.dbinput.text != "00:00" and self.ids.dbinput.text != "Enter Time":
                if self.ids.dbbutton.text == "start":

                    self.t = self.ids.dbinterval.text
                    self.t = int(self.t)
                    self.z = self.ids.dbintervalto.text
                    self.z = int(self.z)
                    if self.ids.dbinterval.text == "":
                        self.ids.dbinterval.text = "1"
                        self.t = 1
                    if self.ids.dbintervalto.text == "":
                        self.ids.dbintervalto.text = "1"
                        self.z = 1

                    if self.t > self.z:
                        dong = False
                    elif self.t == self.z:
                        i = self.t 
                        dong = True

                    elif self.t != self.z:
                        i = random.randint(self.t,self.z)
                        i = int(i)
                        dong = True

                    if dong == True:   
                        myapp.back.play()
                        self.ids.dbbutton.text = "pause"
                        Clock.schedule_interval(self.dbstart, 1)

                        if self.ids.dbinput.text != "00:00":
                            Clock.schedule_interval(self.dbplaysound, i)
                            
                            yy = (splitter(self.ids.dbinput.text))
                            self.dbfull_seconds= int(yy)   
                                       

                    
                elif self.ids.dbbutton.text == "pause":
                    self.dbon = False
                    self.ids.dbbutton.text ="resume"

                elif self.ids.dbbutton.text == "resume":
                    self.ids.dbbutton.text = "pause"
                    self.dbon = True
            elif self.ids.dbinput.text == "00:00":
                self.ids.dbinput.font_size = 50
                self.ids.dbinput.text = "Enter Time"
        else:#her er den checker
            self.ids.dbinput.text = "00:00"
            self.ids.dbinterval.text = "1"
            self.ids.dbintervalto.text = "1" 



    def thesch(self, *args):
        i = random.randint(self.t,self.z)
        Clock.schedule_interval(self.dbplaysound, i)

    def refereshdb(self, *args): #sets the time back to 00:00 when entertime
        if self.ids.dbinput.text == "Enter Time":
            self.ids.dbinput.font_size = 100
            self.ids.dbinput.text = "00:00"##problem area

    def dbstart(self, *args):
        #countdown
        if self.dbon:
            self.dbfull_seconds -= 1
            minutes, seconds = divmod(self.dbfull_seconds, 60)
            dbshow=(f"{minutes:02d}:{seconds:02d}")
            self.ids.dbinput.text = dbshow
            if self.oneon:
                self.dbreset()

            if self.dbfull_seconds == 0:
                myapp.out.play()
                myapp.goodjobs.play()
                self.dbreset()
                
    
    def dbreset(self, *args):
        Clock.unschedule(self.thesch)
        Clock.unschedule(self.dbstart)
        Clock.unschedule(self.dbplaysound)
        self.ids.dbbutton.text = "start"
        self.ids.dbinput.text = "00:00"
        self.ids.dbinterval.text = "1"
        self.ids.dbintervalto.text = "1"
        self.i = self.ids.dbinterval.text
        self.run_once = True
        self.running = False
        
        
        
    sounds = [1,2]
    
    def dbplaysound(self, *args):
        Clock.unschedule(self.dbplaysound)
        Clock.schedule_once(self.thesch)
        if self.dbon:
            t = random.randrange(len(self.sounds)-1)
            self.sounds.append(self.sounds.pop(t)) 
            x = (self.sounds[-1])     
            if x == 1:
                myapp.left.play()
            elif x == 2:
                myapp.right.play()


#timers tabbedpanel
class TimerMain(Screen):
    pass

class StopWatch(Screen):
    oneon = False
    sw_started = False
    sw_seconds = 0
    def startsw(self):
        if not self.sw_started:
            Clock.schedule_interval(self.test1, 0.01)
            self.sw_started = True
            self.ids.start_stop.text = "pause"
            
        elif self.sw_started:
            Clock.unschedule(self.test1)
            self.ids.start_stop.text = "unpause"
            self.sw_started = False
    def test1(self, *args):
        self.sw_seconds += 0.01
        m, s = divmod(self.sw_seconds, 60)
        self.ids.stopwatch.text = ('%02d:%02d.%02d' %
                                        (int(m), int(s), int(s * 100 % 100)))
        if self.oneon:
                self.swreset()
    def swreset(self):
        self.sw_started = False
        self.sw_seconds = 0
        self.ids.start_stop.text = "start"
        Clock.unschedule(self.test1)

        self.ids.stopwatch.text = "00:00:00"



    
class IntervalTimer(Screen):
    def ivtchooser(self, value, *args):
        if value == "Time Input":
            self.ivttimeinput = True
            self.ivtrounds = False
            self.ids.ivtinput.text = "00:00"
        elif value == "Rounds":
            self.ivtrounds= True
            self.ivttimeinput = False
            self.ids.ivtinput.text = "00"
    oneon = False
    ivton = True
    def ivttoggle(self, *args):
        nl = checker(self.ids.ivtinput.text)
        il = checker(self.ids.ivtinputon.text)
        tl = checker(self.ids.ivtinputoff.text)
        if tl and il and nl: #checker to 
            if self.ids.ivtinput.text != "00:00" and self.ids.ivtinput.text !="00" and self.ids.ivtinput.text != "Select Mode":
                if self.ids.ivtstartbutton.text == "start" and self.ids.ivtinputon.text !="00:00" and self.ids.ivtinputoff.text !="00:00":
                    self.ids.ivtstartbutton.text = "pause"
                    if self.ivttimeinput:
                        #stringformatting main cd
                        Clock.schedule_interval(self.ivtstart, 1)
                        Clock.schedule_interval(self.ivtcd1, 1)

                        whole = (splitter(self.ids.ivtinput.text))
                        self.ful_seconds= int(whole)  
                        
                        #on stringformatting
                        secon = (splitter(self.ids.ivtinputon.text))
                        self.ful_secondson= int(secon) 

                        #off stringformatting
                        secoff = (splitter(self.ids.ivtinputoff.text))
                        self.ful_secondsoff= int(secoff)  


                    elif self.ivtrounds:
                        #stringformatting main cd
                        Clock.schedule_interval(self.ivtstart, 1)
                        Clock.schedule_interval(self.ivtcd1, 1)
                        
                        
                        #on stringformatting
                        whole = (splitter(self.ids.ivtinput.text))
                        self.ful_seconds= int(whole)  
                        
                        #on stringformatting
                        secon = (splitter(self.ids.ivtinputon.text))
                        self.ful_secondson= int(secon) 

                        #off stringformatting
                        secoff = (splitter(self.ids.ivtinputoff.text))
                        self.ful_secondsoff= int(secoff)  

                        #off stringformatting
                        


                        self.roundstime  = self.ful_secondsoff + self.ful_secondson
                        self.roundsinput = self.ids.ivtinput.text
                        self.roundrealtimes = int(self.roundsinput) * int(self.roundstime)
            

            
                elif self.ids.ivtstartbutton.text == "pause":
                    self.ivton = False
                    self.ids.ivtstartbutton.text = "resume"
                elif self.ids.ivtstartbutton.text == "resume":
                    self.ivton = True
                    self.ids.ivtstartbutton.text = "pause"
        else:#her er den checker
            try:
                if self.ivttimeinput:
                    self.ids.ivtinput.text = "00:00"
                else:
                    self.ids.ivtinput.text = "00"
                    self.ids.ivtinputon.text = "00:00"
                    self.ids.ivtinputoff.text = "00:00"
            except:
                self.ids.ivtinput.text ="Select Mode"

    def ivtstart(self, *args):
        #countdown
        if self.ivttimeinput:
            if self.ivton:

                minutes, seconds = divmod(self.ful_seconds, 60)
                self.bingbong=(f"{minutes:02d}:{seconds:02d}")
                self.ids.ivtshow.text = self.bingbong
                #label mintuesof
                minutesof, secondsof= divmod(self.ful_secondsoff, 60)
                bingbng=(f"{minutesof:02d}:{secondsof:02d}")
                self.ids.ivtoff.text = bingbng
                #mintues on label
                minuteso, secondso = divmod(self.ful_secondson, 60)
                bingbing=(f"{minuteso:02d}:{secondso:02d}")
                self.ids.ivton.text = bingbing


                if self.ids.ivton.text == "00:00":
                    myapp.en.play()
                if self.ids.ivtoff.text == "00:00":
                    myapp.to.play()
                self.ful_seconds -= 1
                
                
                if self.oneon:
                    self.ivtreset()

                if self.ful_seconds == 0:
                    Clock.unschedule(self.ivtstart)
                    Clock.unschedule(self.ivtcd1)
                    Clock.unschedule(self.ivtcd2)
                    self.ids.ivtinput.text ="00:00"
                    self.ids.ivton.text ="00:00"
                    self.ids.ivtoff.text = "00:00"
                    self.ids.ivtstartbutton.text ="start"

        elif self.ivtrounds:
            if self.ivton:
                minutes, seconds = divmod(self.roundrealtimes, 60)
                self.bingbong=(f"{minutes:02d}:{seconds:02d}")
                self.ids.ivtshow.text = self.bingbong
                #label mintuesof
                minutesof, secondsof= divmod(self.ful_secondsoff, 60)
                bingbng=(f"{minutesof:02d}:{secondsof:02d}")
                self.ids.ivtoff.text = bingbng
                #label minutes on
                minuteso, secondso = divmod(self.ful_secondson, 60)
                bingbing=(f"{minuteso:02d}:{secondso:02d}")
                self.ids.ivton.text = bingbing

                if self.ids.ivton.text == "00:00":
                    myapp.en.play()
                if self.ids.ivtoff.text == "00:00":
                    myapp.to.play()
                self.roundrealtimes -= 1
              

                if self.roundrealtimes == 0:
                    Clock.unschedule(self.ivtcd1)
                    Clock.unschedule(self.ivtcd2)
                    self.ids.ivton.text ="00:00"
                    self.ids.ivtoff.text = "00:00"
                    self.ids.ivtstartbutton.text = "start"
                    Clock.unschedule(self.ivtstart)

    def ivtcd1(self, *args):
        if self.ivton:     
            
            self.ful_secondson -=1
            if self.ful_secondson == 0:
                Clock.schedule_interval(self.ivtcd2, 1)
                Clock.unschedule(self.ivtcd1)
            secoff = (splitter(self.ids.ivtinputoff.text))
            self.ful_secondsoff= int(secoff)  



    def ivtcd2(self, *args):
        if self.ivton:
            #label mintuesof
            
            self.ful_secondsoff -=1
            #
            if self.ful_secondsoff == 0:
                #myapp.to.play()
                Clock.schedule_interval(self.ivtcd1, 1)
                Clock.unschedule(self.ivtcd2)
                self.minuteson, self.secondson = 0, 0
            

            secon = (splitter(self.ids.ivtinputon.text))
            self.ful_secondson= int(secon) 


    def ivtreset(self, *args):
        Clock.unschedule(self.ivtcd1)
        Clock.unschedule(self.ivtstart)
        Clock.unschedule(self.ivtcd2)

        self.ids.ivtstartbutton.text = "start"

        self.ids.ivtshow.text = "00:00"
#        self.ids.ivtinput.text ="00:00"
        
        try:
            if self.ivtrounds:
                self.ids.ivtinput.text = "00"
            elif self.ivttimeinput:
                self.ids.ivtinput.text ="00:00"
            else:
                self.ids.ivtinput.text ="00"
        except:
            self.ids.ivtinput.text ="select mode"

        self.ids.ivton.text = "00:00"
        self.ids.ivtoff.text = "00:00"
        self.ids.ivtinputon.text = "00:00"
        self.ids.ivtinputoff.text = "00:00"
    
    
class TabataTimer(Screen):
        #tabata
    on = True
    oneon = False
    def workon(self):
        if self.ids.ttstartbutton.text == "start":
            self.ids.ttstartbutton.text = "pause"
            Clock.schedule_interval(self.maincountdown, 1)
            self.full_seconds = 480
            self.secc = 40
            self.seccoff = 20
            Clock.schedule_interval(self.test, 1)
        elif self.ids.ttstartbutton.text =="pause":
            self.on = False
            self.ids.ttstartbutton.text = "resume"
        elif self.ids.ttstartbutton.text =="resume":
            self.on = True
            self.ids.ttstartbutton.text ="pause"

    def maincountdown(self, *args):
        if self.on == True:
            self.full_seconds -= 1


            minutes, seconds = divmod(self.full_seconds, 60)
            self.bongbong =(f"{minutes:02d}:{seconds:02d}")
            self.ids.tabatashow.text = self.bongbong
            if self.oneon:
                self.tabatareset()
            if self.full_seconds == 0:
                Clock.unschedule(self.maincountdown)
                Clock.schedule_once(self.tabatareset)


    def test(self, *args):
        if self.on == True:
            self.secc -= 1
            self.ids.labelon.text = ('00:%02d' % ( int(self.secc)))
            self.ids.labeloff.text =str("00:20")
            self.seccoff = 20
            if self.secc == 0:
                myapp.en.play()
                Clock.schedule_interval(self.test2, 1)
                Clock.unschedule(self.test)

    def test2(self, *args):
        if self.on == True:
            self.secc = 40
            self.ids.labelon.text =str("00:40")
            self.seccoff -= 1
            self.ids.labeloff.text = ('00:%02d' % (int(self.seccoff)))
            if self.seccoff == 0:
                myapp.to.play()
                self.secc = 40
                Clock.schedule_interval(self.test, 1)
                Clock.unschedule(self.test2)
   

    def tabatareset(self):
        Clock.unschedule(self.maincountdown)
        Clock.unschedule(self.test)
        Clock.unschedule(self.test2)
        Clock.unschedule(self.workon)
        self.ids.tabatashow.text = ("08:00")
        self.ids.ttstartbutton.text = "start"
        self.full_seconds = 480
        self.secc = 40
        self.seccoff = 20
        self.ids.labelon.text =str("00:40")
        self.ids.labeloff.text =str("00:20")
        
class DingTimer(Screen):
    ding_started = False
    ding_seconds = 0
    oneon = False
    def startding(self):
        nl = checker(self.ids.dinginterval.text)
        if nl:
            timeding = int(self.ids.dinginterval.text) 
            if not self.ding_started:
                Clock.schedule_interval(self.dingseconds, 1)
                self.ding_started = True
                self.ids.dingstartstop.text = "pause"
                Clock.schedule_interval(self.theding, timeding)

            elif self.ding_started:
                Clock.unschedule(self.dingseconds)
                self.ids.dingstartstop.text = "unpause"
                self.ding_started = False
                Clock.unschedule(self.theding)
        else:
            self.ids.dinginterval.text = "01"
    def dingseconds(self, *args):
        self.ding_seconds += 1
        self.ids.dingtimer.text = str(self.ding_seconds)
        m, s = divmod(self.ding_seconds, 60)
        
        self.ids.dingtimer.text = ('%02d:%02d' %
                                        (int(m), int(s)))
        if self.oneon:
            self.dingreset()    
    def dingreset(self):

        self.ding_started = False
        self.ding_seconds = 0
        self.ids.dingstartstop.text = "start"
        Clock.unschedule(self.dingseconds)
        Clock.unschedule(self.theding)
        self.ids.dingtimer.text = "00:00"
        
    def theding(self, *args):
        myapp.en.play()#her skal der være go
    
class ProgTimer(Screen):
    progon = False
    run_once = False
    running = False
    oneon = False
    def progtoggle(self):
        nl = checker(self.ids.proginput.text)
        il = checker(self.ids.progcd.text)
        tl = checker(self.ids.progcdto.text)
        if tl and il and nl: #checker to
            if self.ids.proginput.text != "00:00" and self.ids.proginput.text != "Enter Time":
                if self.ids.progstart.text == "start":

                    self.t = self.ids.progcd.text
                    self.t = int(self.t)

                    self.z = self.ids.progcdto.text
                    self.z = int(self.z)

                    if self.ids.progcd.text =="":
                        self.ids.progcd.text = "1"
                        self.t = 1
                    if self.ids.progcdto.text == "":
                        self.ids.progcdto.text = "1"
                        self.z = 1

                    if self.t > self.z:
                        on = False
                    elif self.t == self.z:
                        i = self.t 
                        on = True
                        Clock.schedule_once(self.adder)

                    elif self.t != self.z:
                        
                        on = True
                        Clock.schedule_once(self.adder)
                    
                    self.progon = True
                    self.run_once = True #måske problem her
                    Clock.schedule_interval(self.progstart, 1)
                    i = self.ids.progcd.text#.removeprefix("interval:")#her laver man det med interval i det selve inputtet
                    i = int(i)
                    if on:
                        if self.ids.proginput.text != "00:00":
                            self.ids.progstart.text = "pause"
                            Clock.schedule_once(self.progplaysound)
                            whole = (splitter(self.ids.proginput.text))
                            self.progfull_seconds= int(whole) 
                    
                elif self.ids.progstart.text == "pause":
                    self.progon = False
                    self.ids.progstart.text ="resume"

            elif self.ids.proginput.text == "resume":
                self.ids.proginput.text = "pause"
                self.progon = True
            elif self.ids.proginput.text == "00:00":
                self.ids.proginput.text = "Enter Time"
                self.ids.proginput.font_size = 50
        else:
            self.ids.proginput.text = "00:00"
            self.ids.progcd.text = "1"
            self.ids.progcdto.text = "1"

    def refereshprog(self, *args): #sets the time back to 00:00 when entertime
        if self.ids.proginput.text == "Enter Time":
            self.ids.proginput.font_size = 100
            self.ids.proginput.text = "00:00"##problem area
    def thesch(self, *args):
        i = random.randint(self.t,self.z)
        Clock.schedule_interval(self.progplaysound, i)

    def progstart(self, *args):
        if self.progon:
            self.progfull_seconds -= 1

            minutes, seconds = divmod(self.progfull_seconds, 60)
            progshow=(f"{minutes:02d}:{seconds:02d}")
            self.ids.proginput.text = progshow

            if self.oneon:
                self.progreset()
            if self.progfull_seconds == 0:
                myapp.goodjobs.play()
                Clock.unschedule(self.progstart)
                Clock.unschedule(self.progplaysound)
                self.ids.progstart.text = "start"
                self.ids.proginput.text = "00:00"
                self.i = self.ids.progcd.text
                self.run_once = True
                self.running = False
                self.sounds = []
                
    def progreset(self, *args):
        Clock.unschedule(self.progstart)
        Clock.unschedule(self.thesch)
        Clock.unschedule(self.progplaysound)
        self.ids.progstart.text = "start"
        self.ids.progcd.text ="1"
        self.ids.progcdto.text ="1"
        self.i = self.ids.progcd.text
        self.run_once = True
        self.running = False
        self.sounds = []
        self.ids.proginput.text = "00:00"
        for child in reversed(self.ids.boxy.children):
            if isinstance(child, CheckBox):
                child.active = False
        
    def progplaysound(self, *args):
        if self.progon:
            Clock.unschedule(self.progplaysound)
            Clock.schedule_once(self.thesch)
            if len(self.sounds) > 1:
                t = random.randrange(len(self.sounds)-1)
                self.sounds.append(self.sounds.pop(t)) 
                x = (self.sounds[-1])
                x.play()

            elif len(self.sounds) == 0:
                pass
            else:
                x = (self.sounds[0])
                x.play()
    numbers = []

    def chooser(self, instance, value, number):
        if value:
            self.numbers.append(number)
        else:
            self.numbers.remove(number)
    sounds=[]
    def adder(self, *args):
        if "one" in self.numbers:
           self.sounds.append(myapp.en) 
        if "two" in self.numbers:
           self.sounds.append(myapp.to) 
        if "three" in self.numbers:
           self.sounds.append(myapp.tre) 
        if "four" in self.numbers:
           self.sounds.append(myapp.fire) 
        if "five" in self.numbers:
           self.sounds.append(myapp.fem) 
        if "six" in self.numbers:
           self.sounds.append(myapp.seks) 
        if "seven" in self.numbers:
           self.sounds.append(myapp.syv) 
        if "eight" in self.numbers:
           self.sounds.append(myapp.otte) 
        if "nine" in self.numbers:
           self.sounds.append(myapp.ni) 
        if "ten" in self.numbers:
           self.sounds.append(myapp.ti)
        if "left" in self.numbers:
           self.sounds.append(myapp.left)
        if "right" in self.numbers:
           self.sounds.append(myapp.right)
        if "back" in self.numbers:
           self.sounds.append(myapp.back)
        if "forward" in self.numbers:
           self.sounds.append(myapp.forward)

class LineTimer(Screen):
    #linetimer
    oneon = False
    def linetoggle(self, *args):
        self.sqdon = True
        self.sqi = self.ids.lineinput.text
        #stringformatting main cd
        nl = checker(self.ids.lineinput.text)
        il = checker(self.ids.lineinterval.text)
        tl = checker(self.ids.lineintervalto.text)
        if tl and il and nl: #checker to
            if self.ids.lineinput.text != "00:00" and self.ids.lineinput.text != "Enter Time":
                if self.ids.linestart.text == "start":
    
                    self.t = self.ids.lineinterval.text
                    self.t = int(self.t)

                    self.z = self.ids.lineintervalto.text
                    self.z = int(self.z)

                    if self.ids.lineinterval.text =="":
                        self.ids.lineinterval.text = "1"
                        self.t = 1
                    if self.ids.lineintervalto.text == "":
                        self.ids.lineintervalto.text = "1"
                        self.z = 1

                    if self.t > self.z:
                        on = False
                    elif self.t == self.z:
                        i = self.t 
                        on = True

                    elif self.t != self.z:
                        
                        on = True
                        
                        i = random.randint(self.t,self.z)
                        i = int(i)

                    if on:
                        self.ids.linestart.text = "pause"
                        if self.ids.lineinput.text != "00:00":
                            Clock.schedule_interval(self.linestart, 1)
                            Clock.schedule_once(self.lineplaysound)
                        
                            yy = (splitter(self.ids.lineinput.text))
                            self.line_seconds= int(yy)
                            self.sqdon = True

                elif self.ids.linestart.text == "pause":
                    self.sqdon = False
                    self.ids.linestart.text ="resume"

                elif self.ids.linestart.text == "resume":
                    self.ids.linestart.text = "pause"
                    self.sqdon = True
            elif self.ids.lineinput.text == "00:00":
                self.ids.lineinput.text = "Enter Time"
                self.ids.lineinput.font_size = 50
        else:#her er den checker
            self.ids.lineinput.text = "00:00"
            self.ids.lineinterval.text = "1"
            self.ids.lineintervalto.text = "1"
                    
            
    def refereshline(self, *args): #sets the time back to 00:00 when entertime
        if self.ids.lineinput.text == "Enter Time":
            self.ids.lineinput.text = "00:00"##problem area
            self.ids.lineinput.font_size = 100
    def thesch(self, *args):
        i = random.randint(self.t,self.z)
        Clock.schedule_interval(self.lineplaysound, i)

    def linestart(self, *args):
        #countdown
        if self.sqdon:
            self.line_seconds -= 1
            minutes, seconds = divmod(self.line_seconds, 60)
            sqdshow=(f"{minutes:02d}:{seconds:02d}")
            self.ids.lineinput.text = sqdshow

            if self.oneon:
                self.linereset()
            if self.line_seconds == 0:
                myapp.goodjobs.play()
                self.ids.lineinput.text = self.sqi 
                self.linereset() #her kan der vidreudvikles ved at lave en ny reset, som ikke fjerner de valgte.     
    def linereset(self, *args):
        Clock.unschedule(self.thesch)
        Clock.unschedule(self.linestart)
        Clock.unschedule(self.lineplaysound)
        self.ids.linestart.text = "start"
        self.ids.lineinput.text = "00:00"
        self.i = self.ids.lineinterval.text
        self.ids.lineinterval.text = "1"
        self.ids.lineintervalto.text = "1"
        self.run_once = True
        self.running = False
        self.realtext = []
        self.soundsadded = []
        self.updater()

    soundsadded = []
    realtext = []
    def updater(self, *args):
        self.ids.list.text = ', '.join(map(str, self.realtext))
    def en(self):
        self.soundsadded.append(myapp.en)
        self.realtext.append("1")
        self.updater()
    def to(self):
        self.realtext.append("2")
        self.soundsadded.append(myapp.to)
        self.updater()

    def tre(self):
        self.realtext.append("3")
        self.soundsadded.append(myapp.tre)
        self.updater()
    def fire(self):
        self.realtext.append("4")
        self.soundsadded.append(myapp.fire)
        self.updater()
    def fem(self):
        self.realtext.append("5")

        self.soundsadded.append(myapp.fem)
        self.updater()
    def seks(self):
        self.realtext.append("6")

        self.soundsadded.append(myapp.seks)
        self.updater()
    def syv(self):
        self.realtext.append("7")

        self.soundsadded.append(myapp.syv)
        self.updater()
    def otte(self):
        self.realtext.append("8")

        self.soundsadded.append(myapp.otte)
        self.updater()
    def ni(self):
        self.soundsadded.append(myapp.ni)
        self.realtext.append("9")
        self.updater()
    def ti(self):
        self.soundsadded.append(myapp.ti)

        self.realtext.append("10")
        self.updater()
    def left(self):

        self.soundsadded.append(myapp.left)
        self.realtext.append("left")
        self.updater()
    def right(self):

        self.soundsadded.append(myapp.right)
        self.realtext.append("right")
        self.updater()
    def back(self):
        self.soundsadded.append(myapp.back)

        self.realtext.append("back")
        self.updater()
    def down(self):

        self.soundsadded.append(myapp.forward)
        self.realtext.append("down")
        self.updater()
    bing = 0

    def lineplaysound(self, *args):
        if self.sqdon:
            Clock.schedule_once(self.thesch)
            Clock.unschedule(self.lineplaysound)
            if len(self.soundsadded) > 0:
                if self.bing >len(self.soundsadded) -1:
                    self.bing = 0
                x = self.soundsadded[self.bing]
                x.play()
                self.bing +=1


#condi screens

class MainCondi(Screen):
    pass
class BeepTest(Screen):
    beepimg = "images/eep.png"
    beepimg2 = "images/eep1.png"
    beepimg1 = "images/eep2.png"
    oneon = False
    beep_started = False
    beeptimer_seconds = 0
    def beepstart(self):
        if self.ids.beepstart.text == "Start":
            Clock.schedule_interval(self.beepseconds, 1)
            self.ids.beepstart.text = "Stop"
            Clock.schedule_once(self.thebeep)
            Clock.schedule_interval(self.thebeep, 9)
            self.ids.beepspeed.text = "Speed: 8.0 km/h"
            self.ids.beeplevel.text = "Level: 01"
            
        elif self.ids.beepstart.text == "Stop":
            Clock.unschedule(self.beepseconds)
            Clock.unschedule(self.thebeep)
            self.beeptimer_seconds = 0
            self.ids.beepstart.text = "Reset"
        elif self.ids.beepstart.text =="Reset":
            self.ids.beepspeed.text = "Speed: 00 km/h"
            self.ids.beeplevel.text = "Level: 00"
            self.ids.beepstart.text = "Start"
            self.ids.beepspeed.text = "Speed: 00"
            self.ids.beeptimer.text = "00:00"
            self.counter = 0
            self.ids.shuttledisplay.text = "Shuttles: 00"
    def beepreset(self):
        Clock.unschedule(self.beepseconds)
        Clock.unschedule(self.thebeep)
        self.ids.beepspeed.text = "Speed: 00 km/h"
        self.ids.beeplevel.text = "Level: 00"
        self.ids.beepstart.text = "Start"
        self.ids.beepspeed.text = "00:00"
        self.counter = 0
        self.ids.shuttledisplay.text = "Shuttles: 00"
        
    def beepseconds(self, *args):
        self.beeptimer_seconds += 1
        self.ids.beeptimer.text = str(self.beeptimer_seconds)
        m, s = divmod(self.beeptimer_seconds, 60)
        
        self.ids.beeptimer.text = ('%02d:%02d' %
                                        (int(m), int(s)))
        if self.oneon:
            self.beepreset()
            self.ids.beeptimer.text ="00:00"
        if self.counter < 10:
            self.ids.shuttledisplay.text = f"Shuttles: 0{self.counter}"
        else:
            self.ids.shuttledisplay.text = f"Shuttles: {self.counter}"

        if self.beeptimer_seconds == 63:
            myapp.tre.play() ##ekstra biblys fedt speed increase.
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 9)
            self.ids.beepspeed.text = "Speed: 9.0 km/h"
            self.ids.beeplevel.text = "level: 02"

        elif self.beeptimer_seconds == 127:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 7.58)
            self.ids.beepspeed.text = "Speed: 9.5 km/h"
            self.ids.beeplevel.text = "level: 02"

        elif self.beeptimer_seconds == 188:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 7.20)
            self.ids.beepspeed.text = "Speed: 10.0 km/h"
            self.ids.beeplevel.text = "level: 03"
        elif self.beeptimer_seconds == 240:
            Clock.unschedule(self.thebeep2)
            Clock.schedule_interval(self.thebeep, 6.86)
            self.ids.beepspeed.text = "Speed: 10.5 km/h"
            self.ids.beeplevel.text = "level: 04"
        elif self.beeptimer_seconds == 314:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 6.55)
            self.ids.beepspeed.text = "Speed: 11.0 km/h"
            self.ids.beeplevel.text = "level: 05"
        elif self.beeptimer_seconds == 380:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 6.26)
            self.ids.beepspeed.text = "Speed: 11.5 km/h"
            self.ids.beeplevel.text = "level: 06"
        elif self.beeptimer_seconds == 442:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 6)
            self.ids.beepspeed.text = "Speed: 12.0 km/h"
            self.ids.beeplevel.text = "level: 07"
        elif self.beeptimer_seconds == 508:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 5.76)
            self.ids.beepspeed.text = "Speed: 12.5 km/h"
            self.ids.beeplevel.text = "level: 08"
        elif self.beeptimer_seconds == 571:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 5.54)
            self.ids.beepspeed.text = "Speed: 13.0 km/h"
            self.ids.beeplevel.text = "level: 09"
        
        elif self.beeptimer_seconds == 632:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 5.33)
            self.ids.beepspeed.text = "Speed: 13.5 km/h"
            self.ids.beeplevel.text = "level: 10"
        elif self.beeptimer_seconds == 696:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 5.14)
            self.ids.beepspeed.text = "Speed: 14.0 km/h"
            self.ids.beeplevel.text = "level: 11"
        elif self.beeptimer_seconds == 758:
            Clock.unschedule(self.thebeep2)
            Clock.schedule_interval(self.thebeep, 4.97)
            self.ids.beepspeed.text = "Speed: 14.5 km/h"
            self.ids.beeplevel.text = "level: 12"
        elif self.beeptimer_seconds == 823:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 4.8)
            self.ids.beepspeed.text = "Speed: 15.0 km/h"
            self.ids.beeplevel.text = "level: 13"
        elif self.beeptimer_seconds == 885:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 4.65)
            self.ids.beepspeed.text = "Speed: 15.5 km/h"
            self.ids.beeplevel.text = "level: 14"
        elif self.beeptimer_seconds == 946:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 4.5)
            self.ids.beepspeed.text = "Speed: 16.0 km/h"
            self.ids.beeplevel.text = "level: 15"
        elif self.beeptimer_seconds == 1009:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 4.36)
            self.ids.beepspeed.text = "Speed: 16.5 km/h"
            self.ids.beeplevel.text = "level: 16"
        elif self.beeptimer_seconds == 1070:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 4.24)
            self.ids.beepspeed.text = "Speed: 17.0 km/h"
            self.ids.beeplevel.text = "level: 17"
        elif self.beeptimer_seconds == 1134:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 4.11)
            self.ids.beepspeed.text = "Speed: 17.5 km/h"
            self.ids.beeplevel.text = "level: 18"
        elif self.beeptimer_seconds == 1196:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 4)
            self.ids.beepspeed.text = "Speed: 18.0 km/h"
            self.ids.beeplevel.text = "level: 19"
        elif self.beeptimer_seconds == 1260:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 3.89)
            self.ids.beepspeed.text = "Speed: 18.5 km/h"
            self.ids.beeplevel.text = "level: 20"
        elif self.beeptimer_seconds == 1323:
            Clock.unschedule(self.thebeep)
            Clock.schedule_interval(self.thebeep, 3.81)
            self.ids.beepspeed.text = "Speed: 19 km/h" 
            self.ids.beeplevel.text = "level: 21"
            self.beep_started = False
    startline = True
    counter = 0
    def thebeep(self, *args):
        self.counter +=1
        if (self.counter%2) ==0:
            self.beepimg = "images/eep2.png"
            self.ids.beepimg.source = self.beepimg2
            self.startline = True
            myapp.to.play()
        else:      
            self.startline = False
            self.ids.beepimg.source = self.beepimg1
            myapp.en.play()
    
"""""
det her er til vo2 maxet i fremtiden
    def spinnerage(self, value):
        if value == "5-14":
            self.kid = True
        elif value == "15-19":
            self.teen = True
        elif value == "20-29":
            self.youngadult = True
        elif value == "30-39":
            self.adult = True
        elif value == "40-49":
            self.oldadult = True
        elif value == "50-59":
            self.old = True
        elif value == "60-69":
            self.older = True
        elif value == "70+":
            self.mormor = True
        elif value == "None":
            pass
    def spinnergender(self, value, *args):
        if value == "Male":
            self.boy = True
        elif value == "Female":
            self.female = True
        elif value == "None":
            pass
        if self.boy == True:
            if self.kid == True:
                self.kidboy = True

            elif self.teen == True:
                self.youngboy = True

            elif self.youngadult == True:
                self.youngman = True

            elif self.adult == True:
                self.olderdude = True

            elif self.oldadult == True:
                self.oldestdude = True

            elif self.old == True:
                self.gammel = True

            elif self.older == True:
               self.oldest = True
            
        elif self.female == True:

            if self.kid == True:
                self.girl = True

            elif self.teen == True:
                self.teengirl = True

            elif self.youngadult == True:
                self.girl = True

            elif self.adult == True:
                self.youngwoman = True
            elif self.oldadult == True:
                self.oldwoman = True

            elif self.old == True:
                self.olderwoman = True

            elif self.older == True:
                self.oldestwoman = True

            elif self.mormor == True:
                self.mormorest = True
    def tester(self):
        if self.kidboy == True:
            print("dong")

"""""

#visualscreens
class MainVisual(Screen):
    pass
class ColorTimer(Screen):
    oneon = False
    background = "images/ground.png"
    clrimgsrc = "images/lipdrill6.png"
    clrdrill1 = "images/clr1.png"
    clrdrill2 = "images/clr2.png"
    clrdrill3 = "images/clr3.png"
    clrdrill4 = "images/clr4.png"
    run_onceclr = True
    def clrchooser(self, valuee, *args):
        if valuee == "Color":
            self.clrcolor = True
            self.clrnumbers = False
            self.ids.colorlabel.color = (1,0,0,1)
            self.ids.colorlabel.background_color = (1,0,0,1) 
        elif valuee == "Numbers":
            self.clrnumbers = True
            self.clrcolor = False
            self.ids.colorlabel.color = (1,1,1,1)
            self.ids.colorlabel.background_color = (0,43,71,0) 
            
    clron = False
    def clrtoggle(self, *args):
        nl = checker(self.ids.clrinput.text)
        il = checker(self.ids.clrinterval.text)
        tl = checker(self.ids.clrintervalto.text)
        if tl and il and nl: #checker to
            if self.ids.clrinput.text != "00:00" and self.ids.clrspinner.text !="mode":
                if self.ids.clrbutton.text == "start":
                    self.t = self.ids.clrinterval.text
                    self.t = int(self.t)

                    self.z = self.ids.clrintervalto.text
                    self.z = int(self.z)

                    if self.ids.clrinterval.text =="":
                        self.ids.clrinterval.text = "1"
                        self.t = 1
                    if self.ids.clrintervalto.text == "":
                        self.ids.clrintervalto.text = "1"
                        self.z = 1

                    if self.t > self.z:
                        on = False
                    elif self.t == self.z:
                        i = self.t 
                        on = True

                    elif self.t != self.z:
                        i = random.randint(self.t,self.z)
                        i = int(i)
                        on = True

                    if on:
                        if self.run_onceclr:
                            self.ids.clrbutton.text = "pause"
                            self.run_onceclr = False
                        #stringformatting main cd
                            if self.ids.clrinput.text != "00:00":
                                self.clron = True
                                Clock.schedule_once(self.clrplaysound)
                                Clock.schedule_interval(self.clrstart, 1)

                                yy = (splitter(self.ids.clrinput.text))
                                self.clrfull_seconds= int(yy)

                elif self.ids.clrbutton.text == "pause":
                    self.clron = False
                    self.ids.clrbutton.text = "resume"
                elif self.ids.clrbutton.text == "resume":
                    self.clron = True
                    self.ids.clrbutton.text = "pause"
            elif self.ids.clrinput.text == "00:00":
                self.ids.clrinput.text = "missing input"#her
        else:#her er den checker
            self.ids.clrinput.text = "00:00"
            self.ids.clrinterval.text = "1"
            self.ids.clrintervalto.text = "1"
    def refereshclr(self, *args): #sets the time back to 00:00 when entertime
        if self.ids.clrinput.text == "missing input":
            self.ids.clrinput.text = "00:00"##problem area

    def thesch(self, *args):
        i = random.randint(self.t,self.z)
        Clock.schedule_interval(self.clrplaysound, i)


    def clrstart(self, *args):
        #countdown
        if self.clron:
            self.clrfull_seconds -= 1
            self.run_onceclr = False
            minutes, seconds = divmod(self.clrfull_seconds, 60)
            clrshow=(f"{minutes:02d}:{seconds:02d}")
            self.ids.clrinput.text = clrshow
            if self.oneon: ##resetr ved tabbedpanelclick
                self.clrreset()

            if self.clrfull_seconds == 0:
                self.clrgj()
                Clock.unschedule(self.clrstart)
                Clock.unschedule(self.clrplaysound)
                self.ids.clrbutton.text = "start"
  
    #clrreset
    def clrreset(self, *args):
        self.ids.clrbutton.text = "start"
        #self.running = False
        Clock.unschedule(self.thesch)
        Clock.unschedule(self.clrplaysound)
        Clock.unschedule(self.clrstart)
        try:
            if self.clrnumbers:
                self.ids.colorlabel.color = (1,1,1,1)
                self.ids.colorlabel.background_color = (0,43,71,0) 
                self.ids.colorlabel.text = "1"

            elif self.clrcolor:
                self.ids.colorlabel.color = (1,0,0,1)
                self.ids.colorlabel.background_color = (1,0,0,1) 
        except:
            self.ids.clrinput.text = "Select Mode"
        self.ids.clrinput.text = "00:00"
        self.ids.clrinterval.text = "1"
        self.ids.clrintervalto.text = "1"
        self.run_onceclr = True

    def clrgj(self):
        Clock.unschedule(self.clrplaysound)
        #LAV EN GET OUT PLAY HERself.getout.play()
        myapp.goodjobs.play()
        self.run_onceclr = True
        self.it = self.ids.clrinterval.text
        
    soundss = [1,2,3,4]
    #måske lav en option som kan være 1,2,3,4,5 eller clr shuffle osv.
    def clrplaysound(self, *args):
        if self.clron and self.ids.clrspinner.text !="mode":
            Clock.unschedule(self.clrplaysound)
            Clock.schedule_once(self.thesch)
            if self.clrcolor:
                t = random.randrange(len(self.soundss)-1)
                self.soundss.append(self.soundss.pop(t)) 
                x = (self.soundss[-1])  
                #her skal background colouren ændres
                if x == 1:
                    self.ids.colorlabel.color = (1,0,0,1)
                    self.ids.colorlabel.background_color = (1,0,0,1)  
                elif x == 2:
                    self.ids.colorlabel.color = (0,1,0,1)  
                    self.ids.colorlabel.background_color = (0,1,0,1)  

                elif x == 3:
                    self.ids.colorlabel.color = (0,0,1,1)
                    self.ids.colorlabel.background_color = (0,0,1,1)  
  
                elif x == 4:
                    self.ids.colorlabel.color = (1,1,0,1)  
                    self.ids.colorlabel.background_color = (1,1,0,1)  

            elif self.clrnumbers:
                t = random.randrange(len(self.soundss)-1)
                self.soundss.append(self.soundss.pop(t)) 
                x = (self.soundss[-1])     
                self.ids.colorlabel.text = str(x)
                #her er der numbers der updatere labelet
class OneClrTimer(Screen):
    oneon = False
    oneclron = False
    run_onceclr = True
    
    def oneclrtoggle(self, *args):
        nl = checker(self.ids.oneclrinput.text)
        il = checker(self.ids.oneclrinterval.text)
        tl = checker(self.ids.oneclrintervalto.text)
        if tl and il and nl: #checker to
            if self.ids.oneclrinput.text != "00:00":
                if self.ids.oneclrbutton.text == "start":
                    self.t = self.ids.oneclrinterval.text
                    self.t = int(self.t)

                    self.z = self.ids.oneclrintervalto.text
                    self.z = int(self.z)

                    if self.ids.oneclrinterval.text =="":
                        self.ids.oneclrinterval.text = "1"
                        self.t = 1
                    if self.ids.oneclrintervalto.text == "":
                        self.ids.oneclrintervalto.text = "1"
                        self.z = 1

                    if self.t > self.z:
                        on = False
                    elif self.t == self.z:
                        i = self.t 
                        on = True

                    elif self.t != self.z:
                        i = random.randint(self.t,self.z)
                        i = int(i)
                        on = True

                    if on:
                        if self.run_onceclr:
                            self.ids.oneclrbutton.text = "pause"
                            self.run_onceclr = False
                        #stringformatting main cd
                            if self.ids.oneclrinput.text != "00:00":
                                self.clron = True
                                Clock.schedule_interval(self.oneclrstart, 1)
                                Clock.schedule_once(self.colorchangeback)
                                yy = (splitter(self.ids.oneclrinput.text))
                                self.clrfull_seconds= int(yy)

                elif self.ids.oneclrbutton.text == "pause":
                    self.clron = False
                    self.ids.oneclrbutton.text = "resume"
                elif self.ids.oneclrbutton.text == "resume":
                    self.clron = True
                    self.ids.oneclrbutton.text = "pause"
            elif self.ids.oneclrinput.text == "00:00":
                self.ids.oneclrinput.text = "missing input"#her
        else:#her er den checker
            self.ids.oneclrinput.text = "00:00"
            self.ids.oneclrinterval.text = "1"
            self.ids.oneclrintervalto.text = "1"
    def refereshoneclr(self, *args): #sets the time back to 00:00 when entertime
        if self.ids.oneclrinput.text == "missing input":
            self.ids.oneclrinput.text = "00:00"##problem area

    
    def colorchanger(self, *args):
        self.ids.onecolorlabel.background_color = (1,0,0,1)
        Clock.schedule_once(self.colorchangeback, 1)
    def colorchangeback(self, *args):
        i = random.randint(self.t,self.z)
        self.ids.onecolorlabel.background_color = (0,43,71,0)
        Clock.schedule_once(self.colorchanger, i)


    def oneclrstart(self, *args):
        #countdown
        if self.clron:
            self.clrfull_seconds -= 1
            self.run_onceclr = False
            minutes, seconds = divmod(self.clrfull_seconds, 60)
            clrshow=(f"{minutes:02d}:{seconds:02d}")
            self.ids.oneclrinput.text = clrshow
            if self.oneon: ##resetr ved tabbedpanelclick
                self.oneclrreset()

            if self.clrfull_seconds == 0:
                self.oneclrgj()
                Clock.unschedule(self.oneclrstart)
                self.ids.oneclrbutton.text = "start"
  
    #clrreset
    def oneclrreset(self, *args):
        self.ids.oneclrbutton.text = "start"
        #self.running = False
        self.colorchanger()
        Clock.unschedule(self.colorchangeback)
        Clock.unschedule(self.colorchanger) #du mangler at sætte den her ind i dit apple projekt
        Clock.unschedule(self.oneclrstart)
        self.ids.oneclrinput.text = "00:00"
        self.ids.oneclrinterval.text = "1"
        self.ids.oneclrintervalto.text = "1"
        self.run_onceclr = True
        self.ids.onecolorlabel.background_color = (0,43,71,0)

    def oneclrgj(self):
        #LAV EN GET OUT PLAY HERself.getout.play()
        myapp.goodjobs.play()
        self.run_onceclr = True
        self.it = self.ids.oneclrinterval.text
        Clock.unschedule(self.colorchangeback)
        Clock.unschedule(self.colorchanger)
        
        
    

def splitter(inputtet):
    minutes, seconds = 0, 0
    string_split = inputtet.split(":")
    if len(string_split) == 2:
        minutes = int(string_split[0])
        seconds = int(string_split[1])      
    elif len(string_split) == 1:
        seconds = int(string_split[0])
    full_seconds = minutes * 60 + seconds
    return full_seconds
    
def checker(zing):
    zong = re.search('[a-zA-Z, |^&+\-%*/=!]', zing)
    yourword = zing
    wordcounter = yourword.count(":") #den her tjekker om der er flere :
    if wordcounter < 2:
        if zong == None:
            x = True
        else:
            x = False
        return x

    
root = Builder.load_file("main.kv")
class myapp(App):
    sw_started = False
    sw_seconds = 0
    running = False#interval timer
    goodjobs = SoundLoader.load("lyde/goodjob.mp3")
    en = SoundLoader.load("lyde/een.mp3")
    to = SoundLoader.load("lyde/eto.mp3")
    tre = SoundLoader.load("lyde/etre.mp3")
    fire = SoundLoader.load("lyde/efire.mp3")
    fem = SoundLoader.load("lyde/efem.mp3")
    seks = SoundLoader.load("lyde/eseks.mp3")
    syv = SoundLoader.load("lyde/esyv.mp3")
    otte = SoundLoader.load("lyde/eotte.mp3")
    ni = SoundLoader.load("lyde/eni.mp3")
    ti = SoundLoader.load("lyde/eti.mp3")
    left = SoundLoader.load("lyde/left.mp3")
    right = SoundLoader.load("lyde/eright.mp3")
    out = SoundLoader.load("lyde/out.mp3")
    forward = SoundLoader.load("lyde/efoward.mp3")
    back = SoundLoader.load("lyde/eback.mp3")
    flipleft = SoundLoader.load("lyde/eflipleft.mp3")
    flipright = SoundLoader.load("lyde/eflipright.mp3")
    downleft = SoundLoader.load("lyde/downleft.mp3")
    downright = SoundLoader.load("lyde/downright.mp3")

    def build(self):
        return root

if __name__ == '__main__':
    myapp().run()
#! /usr/bin/env python
'''
TOOF: Implement 
1. log of all actions at the end of a game before sys quit 
2. 
'''
import os, sys
import pygame
from pygame.locals import *
from Button import *
import math, random
import eztext, dimensions 

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class TestGame:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=640,height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        self.mult = 0 
        self.score = 0 
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        pygame.display.set_caption('The Length Estimation Challenge')

        self.input = 0 
        self.count = 0 
        # set up the colors 
        self.BLACK = (  0,   0,   0)
        self.WHITE = (255, 255, 255)
        self.RED = (255,   0,   0)
        self.GREEN = (  0, 255,   0)
        self.BLUE = (  0,   0, 255)
        self.GRAY = (  200,200,200)
                                                          
    def MainLoop(self):
        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill((255,255,255))

        # timer stuff 
        clock = pygame.time.Clock()
        frame_count = 0
        frame_rate = 20
        start_time = 60

        while True: # main game loop

            font = pygame.font.Font(None, 30)
            # --- Timer going down ---
            # --- Timer going up ---
            # Calculate total seconds
            total_seconds = start_time - (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0
             
            # Divide by 60 to get total minutes
            minutes = total_seconds // 60
             
            # Use modulus (remainder) to get seconds
            seconds = total_seconds % 60
             
            # Use python string formatting to format in leading zeros
            output_string = "Time left: {0:02}:{1:02}".format(minutes,seconds)
            
            # when timer runs out 
            if total_seconds == 0: 
                pygame.draw.rect(self.screen, self.GRAY, pygame.Rect(0, 0, 640, 480))
                text = font.render("Game over, thanks for playing! Your score is: "+str(self.score),1,self.RED)
                x ,y = self.screen.get_size()
                self.screen.blit(text, [50,y/2])
                pygame.display.flip() 
                pygame.time.wait(1000)
                sys.exit()

            # warning towards the end of the game
            rectCol = self.WHITE 
            # Blit to the screen
            if total_seconds <= 5 and total_seconds > 0: 
                if frame_count%20 == 0: 
                    rectCol = self.RED 
                else : 
                    rectCol = self.WHITE
            pygame.draw.rect(self.screen, rectCol, pygame.Rect(425, 0, 240, 40))
            text = font.render(output_string,1,self.BLACK)
            self.screen.blit(text, [450,10])
            pygame.display.flip() 

            '''timer = 0 
            seconds = clock.tick(40)/1000.0
            timer += seconds 
            displaytimer = math.trunc(timer)
            myfont = pygame.font.SysFont(None, 30)
            # apply it to text on a label
            label_time = myfont.render("Timer: "+str(displaytimer), 1, GREEN)
            # put the label object on the screen at point x=100, y=100
            self.screen.blit(label_time, (500, 450))
            pygame.display.flip()'''

            gobut = Button(10,10,"goMed.png")
            txtbx = eztext.Input(x=70,y=10,maxlength=2, color=(0,255,0), prompt='Type your guess: ')
            self.screen.blit(gobut.image,gobut.rect)
            pygame.display.flip() #update display



            k = pygame.event.poll() #look for an event
            if k.type == MOUSEBUTTONDOWN: #if they click,
                if k.button == 1: #if it's the left button,  
                    if gobut.clicked(k.pos): #check if the button's limits are clicked
                        self.screen.fill(self.WHITE)
                        pygame.display.flip()

                        gobut.press() #depress the button
                        self.screen.blit(gobut.image,gobut.rect) #update the screen
                        print "they clicked the go button"
                        pygame.display.flip() #update display

                        # self.generateRandom()
                        # TODO: generate the canvas here and increment the count 
                        if self.count <= len(dimensions.allDimensions): 
                            self.generateExperiment(self.count)
                            self.count+=1 
                        else: #exit with ty 
                            font = pygame.font.Font(None, 30)
                            pygame.draw.rect(self.screen, self.GRAY, pygame.Rect(0, 0, 640, 480))
                            text = font.render("You're done, thanks for playing! Your score is: "+str(self.score),1,self.RED)
                            x ,y = self.screen.get_size()
                            self.screen.blit(text, [50,y/2])
                            pygame.display.flip() 
                            pygame.time.wait(1000)
                            sys.exit()

                        # update txtbx
                        txtbx.update([k])
                        # blit txtbx on the sceen
                        txtbx.draw(self.screen)
                        # refresh the display
                        pygame.display.flip()

                        

            elif k.type == KEYDOWN: 
                if k.key == 13: 
                    print "entered enter"
                    # TODO: send the current guess to the log 
                    # refresh the page ie. get new problem 
                    # generate random measurement and reference lines and positions 
                    self.screen.fill(self.WHITE)
                    pygame.display.flip()
                    # self.generateRandom()
                    if self.count <= len(dimensions.allDimensions): 
                        self.generateExperiment(self.count)
                        self.count+=1 
                    else: #exit with ty 
                        font = pygame.font.Font(None, 30)
                        pygame.draw.rect(self.screen, self.GRAY, pygame.Rect(0, 0, 640, 480))
                        text = font.render("You're done, thanks for playing! Your score is: "+str(self.score),1,self.RED)
                        x ,y = self.screen.get_size()
                        self.screen.blit(text, [50,y/2])
                        pygame.display.flip() 
                        pygame.time.wait(1000)
                        sys.exit()
                    pygame.display.flip()
                    generatedMouse1 = pygame.event.Event(MOUSEBUTTONDOWN,{'pos':(11,11),'button':gobut})
                    generatedMouse2 = pygame.event.Event(MOUSEBUTTONUP,{'pos':(11,11),'button':gobut})
                    pygame.event.post(generatedMouse1)
                    pygame.event.post(generatedMouse2)

                    # display the score 
                    myfont = pygame.font.SysFont(None, 30)
                    # apply it to text on a label
                    label = myfont.render("Score: "+str(self.score), 1, self.BLUE)
                    # put the label object on the screen at point x=100, y=100
                    self.screen.blit(label, (300, 10))
                    pygame.display.flip()

                # update txtbx
                txtbx.update([k])
                # blit txtbx on the sceen
                txtbx.draw(self.screen)
                # refresh the display
                pygame.display.flip()
                #peek at value 
                print "USER ENTERED: ", txtbx.value
                print "MULT RIGHT HERE", self.mult
                
                self.input = txtbx.value
                if k.key != 13 and int(txtbx.value) == self.mult: 
                    print 'Trueee'
                    self.score += self.mult 
                elif k.key != 13 and int(txtbx.value) in [self.mult + 1, self.mult - 1]: 
                    self.score += self.mult - 2 #since self.mult >= 2, never a worry 


            frame_count += 1
            # Limit to 20 frames per second
            clock.tick(frame_rate)
          
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()


            if k.type == QUIT:
                    pygame.quit()
                    sys.exit()   
            pygame.display.update()

            '''# drawing the first bar! :) 
            self.drawBar(GRAY,60,120,60)
            self.drawBar(RED,120,250,240)'''

    def drawBar(self,color,left,right,y): 
        pygame.draw.line(self.screen, color, (left, y), (right, y), 4)
        pygame.draw.line(self.screen, color, (left, y-7), (left, y+7), 4)
        pygame.draw.line(self.screen, color, (right, y-7), (right, y+7), 4)


    def generateRandom(self): 
        # generate random measurement and reference lines and positions 
        self.left_x1 = random.randint(50,400)
        self.right_x1 = random.randint(self.left_x1+10,self.left_x1+20)
        self.y_x1 = random.randint(50,400)
        self.drawBar(self.GRAY,self.left_x1,self.right_x1,self.y_x1)
        # label the reference line 
        refLineFont = pygame.font.SysFont(None, 25)
        refLabel = refLineFont.render("1 unit", 1, self.GRAY)
        self.screen.blit(refLabel, (self.left_x1, self.y_x1 + 10))
        self.mult = random.randint(1,8)
        print "SYSTEM SELECTED: ",self.mult
        self.length_x2 = self.mult*(self.right_x1-self.left_x1)
        self.left_x2 = random.randint(50,380-self.length_x2)
        self.y_x2 = random.randint(50,400)
        self.drawBar(self.RED,self.left_x2,self.left_x2 + self.length_x2, self.y_x2)
        self.saveLog()

    def generateExperiment(self,n): 
        if n < len(dimensions.allDimensions):
            coords = dimensions.allDimensions[n]
            print coords
            self.drawBar(self.GRAY,coords[0],coords[1],coords[2])
            #label the reference line
            refLineFont = pygame.font.SysFont(None, 25)
            refLabel = refLineFont.render("1 unit", 1, self.GRAY)
            self.mult = (coords[4]-coords[3])/(coords[1]-coords[0])
            print "SYSTEM SELECTED: ",self.mult
            self.screen.blit(refLabel, (coords[0], coords[2] + 10))
            self.drawBar(self.RED,coords[3],coords[4],coords[5])
            self.saveLog()
        else: 
            font = pygame.font.Font(None, 30)
            pygame.draw.rect(self.screen, self.GRAY, pygame.Rect(0, 0, 640, 480))
            text = font.render("You're done, thanks for playing! Your score is: "+str(self.score),1,self.RED)
            x ,y = self.screen.get_size()
            self.screen.blit(text, [50,y/2])
            pygame.display.flip() 
            pygame.time.wait(1000)
            sys.exit()



    def saveLog(self): 
        f = open('logNEW.txt','a')
        strToWrite = str([dimensions.allDimensions[self.count][0], dimensions.allDimensions[self.count][1], \
            dimensions.allDimensions[self.count][2], dimensions.allDimensions[self.count][3], \
            dimensions.allDimensions[self.count][4], dimensions.allDimensions[self.count][5]])
        f.write("\n"+strToWrite)
        f.write("\t"+ str(self.mult)+ "\t"+str(self.input))
        f.write('\t Score: '+str(self.score))
        f.close()

if __name__ == "__main__":
    MainWindow = TestGame()
    MainWindow.MainLoop()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on January 27, 2024, at 06:47
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'M_SH_Project_2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\alamol\\Desktop\\M_SH_Project\\M_SH_Project_2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Introduction"
IntroductionClock = core.Clock()
import numpy as np 
import random
introduction = visual.ImageStim(
    win=win,
    name='introduction', units='norm', 
    image='intro.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',units='norm', 
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Video"
VideoClock = core.Clock()

# Initialize components for Routine "Blank"
BlankClock = core.Clock()
B = visual.Rect(
    win=win, name='B',units='norm', 
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "Cogn_E"
Cogn_EClock = core.Clock()
ce = visual.ImageStim(
    win=win,
    name='ce', units='norm', 
    image='cogn_i.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Cogn5"
Cogn5Clock = core.Clock()
image_c1 = visual.ImageStim(
    win=win,
    name='image_c1', units='norm', 
    image='cogn5.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_c1 = visual.Slider(win=win, name='slider_c1',
    size=(0.95, 0.05), pos=(-0.2, 0.35), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_c2 = visual.Slider(win=win, name='slider_c2',
    size=(0.95, 0.05), pos=(-0.2, 0.11), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_c3 = visual.Slider(win=win, name='slider_c3',
    size=(0.95, 0.05), pos=(-0.2, -0.13), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_c4 = visual.Slider(win=win, name='slider_c4',
    size=(0.95, 0.05), pos=(-0.2, -0.37), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_c5 = visual.Slider(win=win, name='slider_c5',
    size=(0.95, 0.05), pos=(-0.2, -0.61), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Cogn3"
Cogn3Clock = core.Clock()
image_c2 = visual.ImageStim(
    win=win,
    name='image_c2', units='norm', 
    image='cogn3.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_c6 = visual.Slider(win=win, name='slider_c6',
    size=(1.1, 0.05), pos=(0.02, 0.34), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_c7 = visual.Slider(win=win, name='slider_c7',
    size=(1.1, 0.05), pos=(0.02, -0.12), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_c8 = visual.Slider(win=win, name='slider_c8',
    size=(1.1, 0.05), pos=(0.02, -0.60), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "Aff_E"
Aff_EClock = core.Clock()
ae = visual.ImageStim(
    win=win,
    name='ae', units='norm', 
    image='aff_i.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Aff5"
Aff5Clock = core.Clock()
image_a1 = visual.ImageStim(
    win=win,
    name='image_a1', units='norm', 
    image='aff5.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_a1 = visual.Slider(win=win, name='slider_a1',
    size=(0.95, 0.05), pos=(-0.2, 0.35), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_a2 = visual.Slider(win=win, name='slider_a2',
    size=(0.95, 0.05), pos=(-0.2, 0.11), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_a3 = visual.Slider(win=win, name='slider_a3',
    size=(0.95, 0.05), pos=(-0.2, -0.13), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_a4 = visual.Slider(win=win, name='slider_a4',
    size=(0.95, 0.05), pos=(-0.2, -0.37), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_a5 = visual.Slider(win=win, name='slider_a5',
    size=(0.95, 0.05), pos=(-0.2, -0.61), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "Aff3"
Aff3Clock = core.Clock()
image_a2 = visual.ImageStim(
    win=win,
    name='image_a2', units='norm', 
    image='aff3.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider_a6 = visual.Slider(win=win, name='slider_a6',
    size=(1.1, 0.05), pos=(0.02, 0.34), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_a7 = visual.Slider(win=win, name='slider_a7',
    size=(1.1, 0.05), pos=(0.02, -0.12), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
slider_a8 = visual.Slider(win=win, name='slider_a8',
    size=(1.1, 0.05), pos=(0.02, -0.60), units='norm',
    labels=[1,2,3,4,5,6,7,8,9], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9),
    granularity=1, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', units='norm', 
    image='end.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Introduction"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
IntroductionComponents = [introduction, key_resp]
for thisComponent in IntroductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Introduction"-------
while continueRoutine:
    # get current time
    t = IntroductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction* updates
    if introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction.frameNStart = frameN  # exact frame index
        introduction.tStart = t  # local t and not account for scr refresh
        introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction, 'tStartRefresh')  # time at next scr refresh
        introduction.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Introduction"-------
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction.started', introduction.tStartRefresh)
thisExp.addData('introduction.stopped', introduction.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('video_file.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ITI"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [polygon]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "Video"-------
    # update component parameters for each repeat
    movie = visual.MovieStim3(
        win=win, name='movie',units='norm', 
        noAudio = False,
        filename=vc,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        size=[2,2],
        depth=-1.0,
        )
    # keep track of which components have finished
    VideoComponents = [movie]
    for thisComponent in VideoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    VideoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Video"-------
    while continueRoutine:
        # get current time
        t = VideoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=VideoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if movie.status == visual.FINISHED: 
            continueRoutine = False
        
        # *movie* updates
        if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            movie.frameNStart = frameN  # exact frame index
            movie.tStart = t  # local t and not account for scr refresh
            movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
            movie.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in VideoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Video"-------
    for thisComponent in VideoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('movie.started', movie.tStartRefresh)
    trials.addData('movie.stopped', movie.tStopRefresh)
    # the Routine "Video" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    BlankComponents = [B]
    for thisComponent in BlankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BlankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *B* updates
        if B.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            B.frameNStart = frameN  # exact frame index
            B.tStart = t  # local t and not account for scr refresh
            B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
            B.setAutoDraw(True)
        if B.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > B.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                B.tStop = t  # not accounting for scr refresh
                B.frameNStop = frameN  # exact frame index
                win.timeOnFlip(B, 'tStopRefresh')  # time at next scr refresh
                B.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank"-------
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('B.started', B.tStartRefresh)
    trials.addData('B.stopped', B.tStopRefresh)
    
    # ------Prepare to start Routine "Cogn_E"-------
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    Cogn_EComponents = [ce, key_resp_2]
    for thisComponent in Cogn_EComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Cogn_EClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Cogn_E"-------
    while continueRoutine:
        # get current time
        t = Cogn_EClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Cogn_EClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ce* updates
        if ce.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ce.frameNStart = frameN  # exact frame index
            ce.tStart = t  # local t and not account for scr refresh
            ce.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ce, 'tStartRefresh')  # time at next scr refresh
            ce.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_2.keys = theseKeys.name  # just the last key pressed
                key_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cogn_EComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cogn_E"-------
    for thisComponent in Cogn_EComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('ce.started', ce.tStartRefresh)
    trials.addData('ce.stopped', ce.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Cogn_E" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Cogn5"-------
    # update component parameters for each repeat
    slider_c1.reset()
    slider_c2.reset()
    slider_c3.reset()
    slider_c4.reset()
    slider_c5.reset()
    key_resp_3.keys = []
    key_resp_3.rt = []
    # keep track of which components have finished
    Cogn5Components = [image_c1, slider_c1, slider_c2, slider_c3, slider_c4, slider_c5, key_resp_3]
    for thisComponent in Cogn5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Cogn5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Cogn5"-------
    while continueRoutine:
        # get current time
        t = Cogn5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Cogn5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_c1* updates
        if image_c1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_c1.frameNStart = frameN  # exact frame index
            image_c1.tStart = t  # local t and not account for scr refresh
            image_c1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_c1, 'tStartRefresh')  # time at next scr refresh
            image_c1.setAutoDraw(True)
        
        # *slider_c1* updates
        if slider_c1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_c1.frameNStart = frameN  # exact frame index
            slider_c1.tStart = t  # local t and not account for scr refresh
            slider_c1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_c1, 'tStartRefresh')  # time at next scr refresh
            slider_c1.setAutoDraw(True)
        
        # *slider_c2* updates
        if slider_c2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_c2.frameNStart = frameN  # exact frame index
            slider_c2.tStart = t  # local t and not account for scr refresh
            slider_c2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_c2, 'tStartRefresh')  # time at next scr refresh
            slider_c2.setAutoDraw(True)
        
        # *slider_c3* updates
        if slider_c3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_c3.frameNStart = frameN  # exact frame index
            slider_c3.tStart = t  # local t and not account for scr refresh
            slider_c3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_c3, 'tStartRefresh')  # time at next scr refresh
            slider_c3.setAutoDraw(True)
        
        # *slider_c4* updates
        if slider_c4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_c4.frameNStart = frameN  # exact frame index
            slider_c4.tStart = t  # local t and not account for scr refresh
            slider_c4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_c4, 'tStartRefresh')  # time at next scr refresh
            slider_c4.setAutoDraw(True)
        
        # *slider_c5* updates
        if slider_c5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_c5.frameNStart = frameN  # exact frame index
            slider_c5.tStart = t  # local t and not account for scr refresh
            slider_c5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_c5, 'tStartRefresh')  # time at next scr refresh
            slider_c5.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_3.keys = theseKeys.name  # just the last key pressed
                key_resp_3.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cogn5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cogn5"-------
    for thisComponent in Cogn5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image_c1.started', image_c1.tStartRefresh)
    trials.addData('image_c1.stopped', image_c1.tStopRefresh)
    trials.addData('slider_c1.response', slider_c1.getRating())
    trials.addData('slider_c1.rt', slider_c1.getRT())
    trials.addData('slider_c1.started', slider_c1.tStartRefresh)
    trials.addData('slider_c1.stopped', slider_c1.tStopRefresh)
    trials.addData('slider_c2.response', slider_c2.getRating())
    trials.addData('slider_c2.rt', slider_c2.getRT())
    trials.addData('slider_c2.started', slider_c2.tStartRefresh)
    trials.addData('slider_c2.stopped', slider_c2.tStopRefresh)
    trials.addData('slider_c3.response', slider_c3.getRating())
    trials.addData('slider_c3.rt', slider_c3.getRT())
    trials.addData('slider_c3.started', slider_c3.tStartRefresh)
    trials.addData('slider_c3.stopped', slider_c3.tStopRefresh)
    trials.addData('slider_c4.response', slider_c4.getRating())
    trials.addData('slider_c4.rt', slider_c4.getRT())
    trials.addData('slider_c4.started', slider_c4.tStartRefresh)
    trials.addData('slider_c4.stopped', slider_c4.tStopRefresh)
    trials.addData('slider_c5.response', slider_c5.getRating())
    trials.addData('slider_c5.rt', slider_c5.getRT())
    trials.addData('slider_c5.started', slider_c5.tStartRefresh)
    trials.addData('slider_c5.stopped', slider_c5.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "Cogn5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Cogn3"-------
    # update component parameters for each repeat
    slider_c6.reset()
    slider_c7.reset()
    slider_c8.reset()
    key_resp_4.keys = []
    key_resp_4.rt = []
    # keep track of which components have finished
    Cogn3Components = [image_c2, slider_c6, slider_c7, slider_c8, key_resp_4]
    for thisComponent in Cogn3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Cogn3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Cogn3"-------
    while continueRoutine:
        # get current time
        t = Cogn3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Cogn3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_c2* updates
        if image_c2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_c2.frameNStart = frameN  # exact frame index
            image_c2.tStart = t  # local t and not account for scr refresh
            image_c2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_c2, 'tStartRefresh')  # time at next scr refresh
            image_c2.setAutoDraw(True)
        
        # *slider_c6* updates
        if slider_c6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_c6.frameNStart = frameN  # exact frame index
            slider_c6.tStart = t  # local t and not account for scr refresh
            slider_c6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_c6, 'tStartRefresh')  # time at next scr refresh
            slider_c6.setAutoDraw(True)
        
        # *slider_c7* updates
        if slider_c7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_c7.frameNStart = frameN  # exact frame index
            slider_c7.tStart = t  # local t and not account for scr refresh
            slider_c7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_c7, 'tStartRefresh')  # time at next scr refresh
            slider_c7.setAutoDraw(True)
        
        # *slider_c8* updates
        if slider_c8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_c8.frameNStart = frameN  # exact frame index
            slider_c8.tStart = t  # local t and not account for scr refresh
            slider_c8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_c8, 'tStartRefresh')  # time at next scr refresh
            slider_c8.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_4.keys = theseKeys.name  # just the last key pressed
                key_resp_4.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cogn3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cogn3"-------
    for thisComponent in Cogn3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image_c2.started', image_c2.tStartRefresh)
    trials.addData('image_c2.stopped', image_c2.tStopRefresh)
    trials.addData('slider_c6.response', slider_c6.getRating())
    trials.addData('slider_c6.rt', slider_c6.getRT())
    trials.addData('slider_c6.started', slider_c6.tStartRefresh)
    trials.addData('slider_c6.stopped', slider_c6.tStopRefresh)
    trials.addData('slider_c7.response', slider_c7.getRating())
    trials.addData('slider_c7.rt', slider_c7.getRT())
    trials.addData('slider_c7.started', slider_c7.tStartRefresh)
    trials.addData('slider_c7.stopped', slider_c7.tStopRefresh)
    trials.addData('slider_c8.response', slider_c8.getRating())
    trials.addData('slider_c8.rt', slider_c8.getRT())
    trials.addData('slider_c8.started', slider_c8.tStartRefresh)
    trials.addData('slider_c8.stopped', slider_c8.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Cogn3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Aff_E"-------
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    # keep track of which components have finished
    Aff_EComponents = [ae, key_resp_5]
    for thisComponent in Aff_EComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Aff_EClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Aff_E"-------
    while continueRoutine:
        # get current time
        t = Aff_EClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Aff_EClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ae* updates
        if ae.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ae.frameNStart = frameN  # exact frame index
            ae.tStart = t  # local t and not account for scr refresh
            ae.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ae, 'tStartRefresh')  # time at next scr refresh
            ae.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_5.keys = theseKeys.name  # just the last key pressed
                key_resp_5.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Aff_EComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Aff_E"-------
    for thisComponent in Aff_EComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('ae.started', ae.tStartRefresh)
    trials.addData('ae.stopped', ae.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "Aff_E" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Aff5"-------
    # update component parameters for each repeat
    slider_a1.reset()
    slider_a2.reset()
    slider_a3.reset()
    slider_a4.reset()
    slider_a5.reset()
    key_resp_9.keys = []
    key_resp_9.rt = []
    # keep track of which components have finished
    Aff5Components = [image_a1, slider_a1, slider_a2, slider_a3, slider_a4, slider_a5, key_resp_9]
    for thisComponent in Aff5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Aff5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Aff5"-------
    while continueRoutine:
        # get current time
        t = Aff5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Aff5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_a1* updates
        if image_a1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_a1.frameNStart = frameN  # exact frame index
            image_a1.tStart = t  # local t and not account for scr refresh
            image_a1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_a1, 'tStartRefresh')  # time at next scr refresh
            image_a1.setAutoDraw(True)
        
        # *slider_a1* updates
        if slider_a1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_a1.frameNStart = frameN  # exact frame index
            slider_a1.tStart = t  # local t and not account for scr refresh
            slider_a1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_a1, 'tStartRefresh')  # time at next scr refresh
            slider_a1.setAutoDraw(True)
        
        # *slider_a2* updates
        if slider_a2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_a2.frameNStart = frameN  # exact frame index
            slider_a2.tStart = t  # local t and not account for scr refresh
            slider_a2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_a2, 'tStartRefresh')  # time at next scr refresh
            slider_a2.setAutoDraw(True)
        
        # *slider_a3* updates
        if slider_a3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_a3.frameNStart = frameN  # exact frame index
            slider_a3.tStart = t  # local t and not account for scr refresh
            slider_a3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_a3, 'tStartRefresh')  # time at next scr refresh
            slider_a3.setAutoDraw(True)
        
        # *slider_a4* updates
        if slider_a4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_a4.frameNStart = frameN  # exact frame index
            slider_a4.tStart = t  # local t and not account for scr refresh
            slider_a4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_a4, 'tStartRefresh')  # time at next scr refresh
            slider_a4.setAutoDraw(True)
        
        # *slider_a5* updates
        if slider_a5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_a5.frameNStart = frameN  # exact frame index
            slider_a5.tStart = t  # local t and not account for scr refresh
            slider_a5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_a5, 'tStartRefresh')  # time at next scr refresh
            slider_a5.setAutoDraw(True)
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_9.keys = theseKeys.name  # just the last key pressed
                key_resp_9.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Aff5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Aff5"-------
    for thisComponent in Aff5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image_a1.started', image_a1.tStartRefresh)
    trials.addData('image_a1.stopped', image_a1.tStopRefresh)
    trials.addData('slider_a1.response', slider_a1.getRating())
    trials.addData('slider_a1.rt', slider_a1.getRT())
    trials.addData('slider_a1.started', slider_a1.tStartRefresh)
    trials.addData('slider_a1.stopped', slider_a1.tStopRefresh)
    trials.addData('slider_a2.response', slider_a2.getRating())
    trials.addData('slider_a2.rt', slider_a2.getRT())
    trials.addData('slider_a2.started', slider_a2.tStartRefresh)
    trials.addData('slider_a2.stopped', slider_a2.tStopRefresh)
    trials.addData('slider_a3.response', slider_a3.getRating())
    trials.addData('slider_a3.rt', slider_a3.getRT())
    trials.addData('slider_a3.started', slider_a3.tStartRefresh)
    trials.addData('slider_a3.stopped', slider_a3.tStopRefresh)
    trials.addData('slider_a4.response', slider_a4.getRating())
    trials.addData('slider_a4.rt', slider_a4.getRT())
    trials.addData('slider_a4.started', slider_a4.tStartRefresh)
    trials.addData('slider_a4.stopped', slider_a4.tStopRefresh)
    trials.addData('slider_a5.response', slider_a5.getRating())
    trials.addData('slider_a5.rt', slider_a5.getRT())
    trials.addData('slider_a5.started', slider_a5.tStartRefresh)
    trials.addData('slider_a5.stopped', slider_a5.tStopRefresh)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    trials.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        trials.addData('key_resp_9.rt', key_resp_9.rt)
    trials.addData('key_resp_9.started', key_resp_9.tStartRefresh)
    trials.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
    # the Routine "Aff5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Aff3"-------
    # update component parameters for each repeat
    slider_a6.reset()
    slider_a7.reset()
    slider_a8.reset()
    key_resp_6.keys = []
    key_resp_6.rt = []
    # keep track of which components have finished
    Aff3Components = [image_a2, slider_a6, slider_a7, slider_a8, key_resp_6]
    for thisComponent in Aff3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Aff3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Aff3"-------
    while continueRoutine:
        # get current time
        t = Aff3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Aff3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_a2* updates
        if image_a2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_a2.frameNStart = frameN  # exact frame index
            image_a2.tStart = t  # local t and not account for scr refresh
            image_a2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_a2, 'tStartRefresh')  # time at next scr refresh
            image_a2.setAutoDraw(True)
        
        # *slider_a6* updates
        if slider_a6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_a6.frameNStart = frameN  # exact frame index
            slider_a6.tStart = t  # local t and not account for scr refresh
            slider_a6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_a6, 'tStartRefresh')  # time at next scr refresh
            slider_a6.setAutoDraw(True)
        
        # *slider_a7* updates
        if slider_a7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_a7.frameNStart = frameN  # exact frame index
            slider_a7.tStart = t  # local t and not account for scr refresh
            slider_a7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_a7, 'tStartRefresh')  # time at next scr refresh
            slider_a7.setAutoDraw(True)
        
        # *slider_a8* updates
        if slider_a8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_a8.frameNStart = frameN  # exact frame index
            slider_a8.tStart = t  # local t and not account for scr refresh
            slider_a8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_a8, 'tStartRefresh')  # time at next scr refresh
            slider_a8.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_6.keys = theseKeys.name  # just the last key pressed
                key_resp_6.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Aff3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Aff3"-------
    for thisComponent in Aff3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image_a2.started', image_a2.tStartRefresh)
    trials.addData('image_a2.stopped', image_a2.tStopRefresh)
    trials.addData('slider_a6.response', slider_a6.getRating())
    trials.addData('slider_a6.rt', slider_a6.getRT())
    trials.addData('slider_a6.started', slider_a6.tStartRefresh)
    trials.addData('slider_a6.stopped', slider_a6.tStopRefresh)
    trials.addData('slider_a7.response', slider_a7.getRating())
    trials.addData('slider_a7.rt', slider_a7.getRT())
    trials.addData('slider_a7.started', slider_a7.tStartRefresh)
    trials.addData('slider_a7.stopped', slider_a7.tStopRefresh)
    trials.addData('slider_a8.response', slider_a8.getRating())
    trials.addData('slider_a8.rt', slider_a8.getRT())
    trials.addData('slider_a8.started', slider_a8.tStartRefresh)
    trials.addData('slider_a8.stopped', slider_a8.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    trials.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials.addData('key_resp_6.rt', key_resp_6.rt)
    trials.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    trials.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    # the Routine "Aff3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "End"-------
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [image_6]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    if image_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_6.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            image_6.tStop = t  # not accounting for scr refresh
            image_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
            image_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_6.started', image_6.tStartRefresh)
thisExp.addData('image_6.stopped', image_6.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Fri 04 Aug 2023 01:55:58 PM 
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '0'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'microphone'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
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
    originPath='/home/marco/Downloads/PsychoPy3 Demos/Feature Demos/microphone/microphone_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
# Make folder to store recordings from mic
micRecFolder = filename + '_mic_recorded'
if not os.path.isdir(micRecFolder):
    os.mkdir(micRecFolder)

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
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
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "proseRecord"
proseRecordClock = core.Clock()
mic = sound.microphone.Microphone(
    device=5, channels=1, 
    sampleRateHz=44100, maxRecordingSize=480000.0
)
stimuli = visual.TextStim(win=win, name='stimuli',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
cross = visual.TextStim(win=win, name='cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Syllable = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('1BalancedSyllableSequence.csv', selection='0:5'),
    seed=None, name='Syllable')
thisExp.addLoop(Syllable)  # add the loop to the experiment
thisSyllable = Syllable.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSyllable.rgb)
if thisSyllable != None:
    for paramName in thisSyllable:
        exec('{} = thisSyllable[paramName]'.format(paramName))

for thisSyllable in Syllable:
    currentLoop = Syllable
    # abbreviate parameter names if possible (e.g. rgb = thisSyllable.rgb)
    if thisSyllable != None:
        for paramName in thisSyllable:
            exec('{} = thisSyllable[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "proseRecord"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    stimuli.setText(token)
    # keep track of which components have finished
    proseRecordComponents = [mic, stimuli, cross]
    for thisComponent in proseRecordComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    proseRecordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "proseRecord"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = proseRecordClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=proseRecordClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # mic updates
        if mic.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mic.frameNStart = frameN  # exact frame index
            mic.tStart = t  # local t and not account for scr refresh
            mic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
            # start recording with mic
            mic.start()
            mic.status = STARTED
        if mic.status == STARTED:
            # update recorded clip for mic
            mic.poll()
        if mic.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mic.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                mic.tStop = t  # not accounting for scr refresh
                mic.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mic, 'tStopRefresh')  # time at next scr refresh
                # stop recording with mic
                mic.stop()
                mic.status = FINISHED
        
        # *stimuli* updates
        if stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli.frameNStart = frameN  # exact frame index
            stimuli.tStart = t  # local t and not account for scr refresh
            stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
            stimuli.setAutoDraw(True)
        if stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                stimuli.tStop = t  # not accounting for scr refresh
                stimuli.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli, 'tStopRefresh')  # time at next scr refresh
                stimuli.setAutoDraw(False)
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 4.8-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cross, 'tStopRefresh')  # time at next scr refresh
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in proseRecordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "proseRecord"-------
    for thisComponent in proseRecordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # tell mic to keep hold of current recording in mic.clips and transcript (if applicable) in mic.scripts
    # this will also update mic.lastClip and mic.lastScript
    mic.stop()
    tag = data.utils.getDateStr()
    micClip = mic.bank(
        tag=tag, transcribe='None',
        config=None
    )
    Syllable.addData('mic.clip', os.path.join(micRecFolder, 'recording_mic_%s.wav' % tag))
    Syllable.addData('mic.started', mic.tStart)
    Syllable.addData('mic.stopped', mic.tStop)
    Syllable.addData('stimuli.started', stimuli.tStartRefresh)
    Syllable.addData('stimuli.stopped', stimuli.tStopRefresh)
    Syllable.addData('cross.started', cross.tStartRefresh)
    Syllable.addData('cross.stopped', cross.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Syllable'

# save mic recordings
for tag in mic.clips:
    for i, clip in enumerate(mic.clips[tag]):
        clipFilename = 'recording_mic_%s.wav' % tag
        # if there's more than 1 clip with this tag, append a counter for all beyond the first
        if i > 0:
            clipFilename += '_%s' % i
        clip.save(os.path.join(micRecFolder, clipFilename))

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

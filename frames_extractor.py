#!/usr/bin/python3

import sys, glob, getopt, os
import cv2

VIDEO_FILE_EXT = ['*.mp4', '*.mov', '*.avi']

def findAllVideoFiles(directory, recursiveSearch):
    videoFiles = []
    for ext in VIDEO_FILE_EXT:
        pattern = os.path.join(
            directory, 
            ('**/' + ext) if recursiveSearch else ext
        )
        videoFiles.extend(glob.glob(pattern, recursive=recursiveSearch))
    return videoFiles

def getFrameFilename(videoFilePath, frames):
    filenameWithoutExt = os.path.splitext(os.path.basename(videoFilePath))[0]
    
    idx = 1
    while(filenameWithoutExt in frames):
        idx += 1

    return filenameWithoutExt + '-' + str(idx)

def extractMiddleFrames(videoFiles):
    frames = {}
    for video in videoFiles:
        cap = cv2.VideoCapture(video)
        framesCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        middleFrameIndex = int(framesCount / 2)
        
        cap.set(cv2.CAP_PROP_POS_FRAMES, middleFrameIndex)
        ret, frame = cap.read()
        
        frames[getFrameFilename(video, frames)] = frame
        
        cap.release()

    return frames

def main():
    usageMessage = 'USAGE: ' +  __file__ + ' -i <INPUT_DIR> -o <OUTPUT_DIR> [-r]'
    inputDir = os.path.abspath('.')
    outputDir = os.path.abspath(os.path.join('.', 'out'))
    recursiveSearch = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:o:r', ['input-dir=', 'output-dir=', 'help', 'recursive'])
    except getopt.GetoptError:
        print(usageMessage)
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(usageMessage)
            sys.exit(0)
        elif opt in ('-i', '--input-dir'):
            inputDir = os.path.abspath(arg)
        elif opt in ('-o', '--output-dir'):
            outputDir = os.path.abspath(arg)
        elif opt in ('-r', '--recursive'):
            recursiveSearch = True
        
    videoFiles = findAllVideoFiles(inputDir, recursiveSearch)
    print('[*] Video files found in ' + inputDir + ': ' + str(len(videoFiles)))
    
    if not videoFiles:
        sys.exit(0)

    frames = extractMiddleFrames(videoFiles)
    print('[*] Extracted ' + str(len(frames)) + ' frames')

    os.makedirs(outputDir, exist_ok=True)

    for key in frames:
        frameFilename = os.path.join(outputDir, key + '.png')
        cv2.imwrite(frameFilename, frames[key])
    
    print('[*] Saved ' + str(len(frames)) + ' frames in ' + outputDir)

if __name__ == '__main__':
    main()

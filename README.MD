# Overview

The script extracts a video frame from the middle of each video file, in the given input directory. Extracted frames are saved in the given output directory. The script uses OpenCV 3.4.2 for video processing and handles the following video file extensions: `*.mp4`, `*.mov`, `*.avi`.

The supported video files list can be extended (by adding a new extensio to the `VIDEO_FILE_EXT` list) as long as the required codecs are installed.

# Usage

```
python frames_extractor.py -i <INPUT_DIR> -o <OUTPUT_DIR> [-r]
```

## -i \<INPUT\_DIR\>

Directory with the input video files. If no parameter is given, the current directory `.` is assumed.

## -o \<OUTPUT\_DIR\>

Directory that will contain output images (extracted video frames). If no parameter is given, the `.\out` directory is assumed. If given directory does not exist, it will be created automatically.

## -r

Recursive search. If the parameter is given, the script will find and process all video files in the given input directory, including its subdirectories.

# Requirements

* OpenCV 3.4.2

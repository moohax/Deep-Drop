# Deep-Drop
Machine learning enabled dropper

### Quick Start
```
pip install -r requirements.txt
python deepdrop.py
```

Copy paste the payload (core\macros) into a word doc and run.

### Structure
```
deepdrop.py -> handles loading models, patching payloads, and starting app
core\
  data\ -> process list data
  macros\ -> any macros
  models\ -> trained models
  static\ -> flask default
  templates\ -> flask default
  config.py -> set info for data, macros, and models
  ddmodels.py -> deep drop model classes
  deepdrop.py -> holds dropper parsing and logic
  logging.py -> prettify logging output
  payloads.py -> handles patching/processing of payloads
  routing.py -> holds the main app routes
```

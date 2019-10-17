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
core
  bin\ -> contains dlls (covenant, silenttrinity, etc. Alternatively grab a test dll from [here](https://github.com/monoxgas/sRDI/blob/master/TestDLL/dllmain.cpp)
  data\ -> process list data for (re)training
  models\ -> trained models used for classification
  payloads\ -> template and patched payloads for initial access
  stagers\ -> stager templates 
  utils\ -> contains SRDi
  config.py -> set info for various items, paths, dlls, etc.
  ddmodels.py -> deep drop model classes
  deepdrop.py -> dropper parsing, staging, and decision logic
  logging.py -> prettify logging output
  routing.py -> holds the main app routes
```

### Quick start
```
λ pip3 install requirements
λ python3 deepdrop.py

 ____              ____
|    \ ___ ___ ___|    \ ___ ___ ___
|  |  | -_| -_| . |  |  |  _| . | . |
|____/|___|___|  _|____/|_| |___|  _|
              |_|               |_|


[-] All models loaded
[-] Routes loaded
[-] Payloads patched for localhost

 * Serving Flask app "deepdrop" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
```

### Testing
Passing `-d\--debug` to 
Copy the `localhost.vba` into a word doc
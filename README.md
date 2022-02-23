# Voice Assistent

Author: Pavel Podrazký

Small voice assistent that can make working on PC more convinient.
<b>Note</b>: This voice assistent is currently not supported on Windows. Windows support will be added in the future.

## Setup

Firs you need to install dependencies.<br>

```python
pip install -r requirements.txt
```

Than you need to setup some JSON files, or you can modify existing files.
Put them all next to `main.py` folder

1. paths.json
   This path contains paths to notes folder and programming projects folders.
   ```json
   {
     "linux": {
       "project1": "path1",
       "notes": "path/to/notes"
     },
     "windows": {
       "project2": "path2",
       "notes": "path/to/notes"
     }
   }
   ```
2. speach_key_words.json
   This file is for key words that will be used to figure out what you want to do with voice assistent.
   ```json
   {
     "open": ["open", "key", "words"],
     "close": ["close", "key", "words"],
     "apps": {
       "app1": ["app", "key", "words"]
     }
   }
   ```
3. speach_responses.json
   This file will be used for random choosing of response.
   ```json
   {
     "response_type": ["respone1", "respone1"]
   }
   ```

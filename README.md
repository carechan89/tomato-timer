# tomato-timer
A Pomodoro-style web app written with Python and Flask.

# startup
1. Download some sort of virtual environment. 
  - I used a combination of [VirtualBox](https://www.virtualbox.org/) and [pipenv](https://pypi.org/project/pipenv/) because Windows 10 
  has some path issues that make it difficult to set up and install
  - This guide will be written with this in mind but feel free to use whichever virtual environment you're comfortable with
  - Or don't
  - 
2.  Fork the repo
  - I'm not entirely sure how pip lock files work when you fork a repo so...sorry about that
  - But there is some info [here](https://pipenv-fork.readthedocs.io/en/latest/advanced.html) that I haven't read through yet
  - ~~If you figure it out, please just edit the README~~
  - I *think* you can install everything by running
    ```shellscript
    pip -r requirements.txt
    ```

3. That's it, get coding!

# running flask
```shellscript 
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```
Follow the link given in the terminal (most likely [localhost:5000](http://localhost:5000/))

# other pertinent info
I'm currently using [this guide](https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html).

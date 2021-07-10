# InstaBot

Minimal command line automation tool to automate your instagram with **[python](https://www.python.org/)** and **[instapy](https://instapy.org/)**.


## Installation

### requirements
- install [python3](https://www.python.org/) 
- install [firefox](https://www.mozilla.org/en-US/firefox/new/) & [geckodriver](https://github.com/mozilla/geckodriver/releases)
- install [wget](https://phoenixnap.com/kb/wget-command-with-examples)
- install [instapy](https://instapy.org/)

### install the bot
- open terminal or cmd and download main.py file with [wget](https://phoenixnap.com/kb/wget-command-with-examples).
	```console
	wget https://raw.githubusercontent.com/akshay-rf/instabot/main/main.py
	```

## Usage
### start instabot
- launch terminal or cmd and locate to your *Downloads* folder.
	```console
	$ cd Downloads
	```
- run main.py in your terminal or cmd.
	```console
	$ python3 main.py
	```
### interface
- enter your instagram *username* and *password*.

![enter image description here](https://i.ibb.co/ctJXxFJ/Screenshot-from-2021-07-10-15-33-30.png)

- set comments - leave it empty to disable commenting.

![enter image description here](https://i.ibb.co/25DPcXm/Screenshot-from-2021-07-10-16-26-23.png)
- set tags - leaving it empty will cause the script to crash.

![enter image description here](https://i.ibb.co/FHynjjT/Screenshot-from-2021-07-10-16-29-50.png)

- the script will start doing its thing - like, comment on posts.

![enter image description here](https://i.ibb.co/kyNf5t5/Screenshot-from-2021-07-10-16-33-43.png)
![enter image description here](https://i.ibb.co/0cg4pWP/Screenshot-from-2021-07-10-16-34-59.png)
- working [video](https://drive.google.com/file/d/1oK6wDan_ZN6aGyFq7_pnoPG8VSRetm3D/view?usp=sharing).
## Some Common Errors

- ### cannot detect post media type
	- solved - https://stackoverflow.com/questions/66963998/cannot-detect-post-media-type-skip-instapy-bot-doesnt-interact-with-posts 

- ### KeyError: 0
	- solved - https://github.com/timgrossmann/InstaPy/issues/6191

- ### unable to determine correct filename for 64bit linux
	- solved - https://stackoverflow.com/questions/63235553/instapy-error-unable-to-determine-correct-filename-for-64bit-linux  

## Licence 
GNU General Public License v3.0

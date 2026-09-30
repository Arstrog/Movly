# Movly: CLI tool for displaying movie information
Movly is a simple cli tool created based on the insctructions of https://roadmap.sh/projects/tmdb-cli.
Movly uses the TMDB GET requests in order to display various movie information based on the category provided by the user.

## Instalation
In order to use movly, you first need to clone the repository:

```bash
git clone https://github.com/Arstrog/Movly.git
```

After that you need to run this command:

```bash
cd Movly
pip install .
```
Before moving on, you need to have your own API Read Access Token in order to be able to use this tool.

Go to the TMDB website,
https://www.themoviedb.org/
Create an account or login to an existing one. After that click on Account, then Settings and the choose the API section. Click on generate API key and follow the instructions. Copy the API Read Access Token.

Go back to the Movly directory and create a new file named .env and paste this:

'''bash
TMBD_ACCESS_TOKEN=your_access_token
'''

Now you can use movly from anywhere in your terminal.

## Usage

```bash
$ movly --type "playing"
$ movly --type "popular"
$ movly --type "top"
$ movly --type "upcoming"
```


## License
This projects is under the MIT License, this means it is free of use and can be distributed freely

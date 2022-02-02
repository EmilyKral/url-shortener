# URL Shortener

A site to generate a shortened url of any link passed to it, in order to more easily share long
urls.

## Installation

- clone the repo and cd into root directory
- run `pipenv shell` and then `pipenv install` to install dependencies

## Usage

- within shell terminal, go into shortener folder and run `python manage.py runserver` to start
  local server
- If css is not loading correctly on the pages run `python manage.py runserver --insecure`

### Wins & Challenges

- Custom 500 error page
- Redirecting to the correct pages
- Linking the css to the html correctly

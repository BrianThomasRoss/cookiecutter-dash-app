# {{ cookiecutter.project_name }}

{{cookiecutter.project_short_description}}

### Running locally

Run the following commands to bootstrap your environment if you are unable to run the application using Docker

```bash
cd {{cookiecutter.app_name}}
{%- if cookiecutter.use_pipenv == "yes" %}
pipenv install --dev
pipenv shell
{%- else %}
pip install -r requirements/dev.txt
{%- endif %}
```

Once you have installed the project dependencies you can run the app locally with the command

``flask run``

## Deployment


## Heroku

The best effort has been made to make deployment as easy and seamless as possible, however you should 
 familiarize yourself with the basic [Git](https://git-scm.com/) and [Heroku](https://heroku.com/) concepts before
  deploying this app. 

Application configuration is in `app.json` and you should be able to deploy using

<a href="https://heroku.com/deploy" style="display: block"><img src="https://www.herokucdn.com/deploy/button.svg" title="Deploy" alt="Deploy"></a>
    <br>

Deployment by using [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli):

If you're unable to successfully deploy using the button you will need to try using the CLI.

### Create a new Heroku App.

    heroku create {{cookiecutter.app_name}}

### Add buildpacks

    heroku buildpacks:add --index=1 heroku/python

### Deploy on Heroku by pushing to the `heroku` branch

    git push heroku master

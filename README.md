# cookiecutter-dash-app

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for making a minimal dash app, deployable to Heroku.

A live demo is running at [cookiecutter-dash.herokuapp.com](https://cookiecutter-dash.herokuapp.com).

----

To use this cookiecutter template you need to have cookiecutter installed.

`pip install cookiecutter`

Create a new **public** repository in GitHub, this will be the name of your app. **Do not initialize the repository with a .gitignore LICENSE or README**

On your local machine navigate to your workspace and run:

`cookiecutter https://github.com/brianthomasross/cookiecutter-dash-app.git`

This will ask you a few questions, be sure to use the app name from the GitHub repo you created earlier.

When you've answered all the questions a folder will have been created with the app name.

Navigate into the directory `cd <your-app-name>`

Then run the following:

```
git init

git add .

git commit -m "Initial commit"

git remote add origin <the url for your github repo>

git push origin master

```

When you've made through the above commands you can navigate to your repo on GitHub. Scroll down and you will see a `deploy to Heroku` button. Click the button and choose a name for your app on Heroku, this will prepend the url `your-app-name.herokuapp.com` will be the main site.

Click Deploy and the app should build! Enjoy!

----

**Thanks to [Ryan Herr](https://www.github.com/rrherr) for the original template as inspiration.**


# Flask-getting-started

A simple Python application based on Flask for LeanEngine Python runtime.

[中文 README](/README-zh.md)

## Local Development

First make sure [Python](http://python.org/) and [lean-cli](https://docs.leancloud.app/leanengine_cli.html#hash2037210682) are installed on the machine, then run the following commands:

```sh
# clone the repository
git clone git@github.com:leancloud/python-getting-started.git
cd python-getting-started
# install dependencies
pip install -r requirements.txt
# connect LeanCloud application
lean switch
# run the project locally
lean up
```

Open http://localhost:3000 in your browser to view the homepage of your project.

## Deploy to LeanEngine

Run the following command to deploy your project to the production environment (if you haven't purchased a standard instance):

```
lean deploy
```

If you have purchased a standard instance, your project will be deployed to the staging environment first when you run `lean deploy`.
You need to run `lean publish` to deploy the code in the staging environment to the production environment.

## Documentation

* [Python Web Hosting Guide](https://docs.leancloud.app/leanengine_webhosting_guide-python.html)
* [Python Cloud Function Guide](https://docs.leancloud.app/leanengine_cloudfunction_guide-python.html)
* [LeanStorage Python Guide](https://docs.leancloud.app/leanstorage_guide-python.html)
* [Python SDK API](https://leancloud.github.io/python-sdk/)
* [lean-cli Guide](https://docs.leancloud.app/leanengine_cli.html)

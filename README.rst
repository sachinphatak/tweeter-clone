=============
Tweeter clone
=============

Tweeter clone is a Django + angular app to view and post tweets. It is a modified clone of this tweeter app: https://github.com/nnja/tweeter


Quick start
-----------

1. cd into the twitter_clone directory and run `python manage.py migrate` to create the tweeter models.

2. Start the development server by running `python manage.py runserver`

3. Visit http://127.0.0.1:8000/ on your browser to start tweeting!


Editing frontend
----------------

All django template files are available in "tweeter_clone/tweeter/templates/tweeter/"
All css files are available in "tweeter_clone/tweeter/static/tweeter/css/"
The js files are available in "tweeter_clone/tweeter/static/tweeter/js/"
Angularjs, ngResource and bootstrap are being included in the index.html file through their cdn links.

To add more javascript or css, create new files in the above mentioned locations and reference them in the required django template as follows:

{% load staticfiles %}
<script src="{% static 'tweeter/js/<new-js-file-name>.js' %}"></script>
<link rel="stylesheet" type="text/css" href="{% static 'tweeter/css/new-css-file-name.css' %}">

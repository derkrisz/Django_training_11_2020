# Django Review Exercise 1

Open 'polls/models.py' and declare a model for 'weather'
This should include 'city', 'country' and 'description' as character fields
Also include 'temperature' as a FloatField (with a sensible default value)
Write a new __str__ method for this data model, which returns the city, description and temperature

Make migrations and migrate

Open 'polls/admin.py' and import your Weather model
Register your Weather model with the admin site (exactly as for 'Question' and 'Choice')

Open the admin site and add several weather reports
(Notice that new 'Weather' instances use your __str__ in the Admin interface)

Open 'polls/views.py' and declare a view called 'weather'
Write a weather template descended from 'base.html'
Return some content for this view from the weather model (e.g. list the weather instances)
Open 'polls/urls.py' and add a path 'weather/' which leads to this new view
Check your view content gets rendered in the browser when you navigate to 127.0.0.1:8000/polls/weather/

## Optional

Add more data members to the weather model e.g. wind speed and direction etc.
Create a weather_detail page which shows details for a selected weather member
Link the weather list to the weather detail, passing a context dictionary
Remember the 'temperature' field should be type='number'
(NB this is NOT as complex as the 'votes' system)

## Django Review Exercise 2

reference: see
<https://docs.djangoproject.com/en/3.1/ref/forms/>
<https://docs.djangoproject.com/en/3.1/ref/forms/renderers/#overriding-built-in-widget-templates>
<https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/>

Write unit tests for the 'Choice' model
This is a trivial model, so the tests will be prety basic, such as testing that an choice created during the test has the
expected text, defaults to zero votes and is associated with a particular question (which you set in the test!!)
You could also test the __str__ method of the Choice class

Make significant changes to 'detail.html' so it uses a Django form widget rather than a hard-coded <input /> tag
To do this you will need to create a new .py module containing code and also alter the view.py file accordingly

## Optional

Add a field to the detail form for 'username' (no need to add this to the models)
Include validation so the detail form (for voting) cannot be submitted until a 'username' has been provided (We are not
persisting the username in this example)
Write unit tests for your 'Weather' model
Customize the Admin interface to show your Weather model differently to the default
(i.e. choose banner headers, order etc.)

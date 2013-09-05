# django-reactify

Makes it easy to use `reactify` with Django via `reactify-server-rendering`. No more Jinja templates!

## Getting started

### 1. Set up your dev environment

In your dev environment set up Node.js and `npm`. Then do `sudo npm install -g reactify-server-rendering-tools`.

### 2. Update `settings.py`

`reactify` needs to create a JS file that your app will serve.

1. Add `REACTIFY_BUNDLE_PATH` to `settings.py`. This is a path to a JS file in one of Django's `STATICFILES_DIRS` that `reactify` will create.
2. Add `REACTIFY_BUNDLE_URL` to `settings.py`. This is `STATIC_URL` pointing to the bundle file specified in `REACTIFY_BUNDLE_PATH`.

### 2. Write your code

Write your code using React and CommonJS modules. You can require React by doing `require('React')` or `npm install` it yourself.

To bundle your JS you need to run `reactify`. You'll need to provide a list of **MODULE_ID**s that you want to call from Django.

Run `reactify -o **REACTIFY_BUNDLE_PATH** -b **PATH_TO_YOUR_SOURCE** **MODULE_ID...**` to do this. You can add `-w` and `-d` flags in development.

### 3. Render a React component from Django

Create your views like this:

```python
import reactify
def home(request):
    return reactify.render_component(
        'MODULE_ID',
        prop='value'
    )
```

**NOTE:** you will need to have a working `PyExecJS` installed for this to work.

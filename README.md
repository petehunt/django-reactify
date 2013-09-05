# django-reactify

Makes it easy to use `reactify` with Django via `reactify-server-rendering`. No more Jinja templates!

## Getting started

### 1. Set up your dev environment

In your dev environment set up Node.js and `npm`. Then do `sudo npm install -g reactify-server-rendering-tools`.

### 2. Update `settings.py`

`reactify` needs to create a JS file that your app will serve.

1. Add `REACTIFY_BUNDLE_PATH` to `settings.py`. This is a path to a JS file in one of Django's `STATICFILES_DIRS` that `reactify` will create.
2. Add `REACTIFY_BUNDLE_URL` to `settings.py`. This is `STATIC_URL` pointing to the bundle file specified in `REACTIFY_BUNDLE_PATH`.
3. Add `REACTIFY_SRC` to `settings.py`. This will point to the root directory of your CommonJS modules.
4. Add `REACTIFY_MODULE_IDS` to `settings.py`. This is the list of React component module IDs you want to call from Django. **NOTE:** this is relative to `REACTIFY_SRC` and must begin with `./`.

### 3. Write your code

Run `python manage.py reactify` to build your JS bundles. This will watch for changes in `DEBUG` and will minify in prod.

Write your code using React and CommonJS modules. You can require React by doing `require('React')` or `npm install` it yourself.

Create your Python views like this:

```python
import reactify
def home(request):
    return reactify.render_component(
        'MODULE_ID',
        prop='value'
    )
```

**NOTE:** you will need to have a working `PyExecJS` installed for this to work.

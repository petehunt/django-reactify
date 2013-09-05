from django.conf import settings
from django.http import HttpResponse
import execjs
import json

class DjangoReactify(object):
    def __init__(self, local_bundle, bundle_url):
        self.local_bundle = local_bundle
        self.bundle_url = bundle_url
        if not settings.DEBUG:
            self.load_source()

    def load_source(self):
        with open(self.local_bundle, 'r') as f:
            self.source = f.read()

    def render_page(self, module, props):
        if settings.DEBUG:
            self.load_source()
        runtime = execjs.compile(self.source)
        return runtime.eval(
            'require("reactify-server-rendering").serverRender(%s, %s, %s)' % (
                json.dumps(module),
                json.dumps(props),
                json.dumps(self.bundle_url)
            )
        )

_instance = DjangoReactify(settings.REACTIFY_BUNDLE_PATH, settings.REACTIFY_BUNDLE_URL)

def render_to_response(component_module, **props):
    return HttpResponse(_instance.render_page(component_module, props))

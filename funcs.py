import requests
from const import *
import restapi.resolver.params as rarp


def api_get_template(url, auth=None, headers=None, params=None):
    return requests.request('GET', url,
                            headers=headers,
                            auth=auth,
                            params=params)


def space_template(builder, loc_params, *args):
    args_to_join = [builder.domain, SPACES]

    if len(args):
        args_to_join.extend(args)

    url = '/'.join(args_to_join)
    params = {rarp.key(k): rarp.value(v) for k, v in loc_params if v not in (None, False)}
    return api_get_template(url, builder.auth, headers=builder.headers, params=params)

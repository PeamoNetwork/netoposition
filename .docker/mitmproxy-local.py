from mitmproxy import http
from mitmproxy.proxy import server_hooks

account_domains = [
    "conntest.ixchats.com",
    "cbvc.cdn.ixchats.com",
    'c.account.ixchats.com', 'account.ixchats.com',
    "nasc.ixchats.com",
    "datastore.ixchats.com",
    "api.ixchats.com",
    "local-cdn.ixchats.com",
    "assets.ixchats.com",
]

miiverse_domains = [
    "discovery.olv.nintendo.net",
    "discovery.olv.ixchats.com",
    "api.olv.ixchats.com",
]

juxt_domains = [
    "juxt.ixchats.com",
    "portal.olv.ixchats.com",
    "ctr.olv.ixchats.com",
]

s3_domains = [
    "cdn.ixchats.com",
    "r2-cdn.ixchats.com"
]

def request(flow: http.HTTPFlow):
    # redirect to different host
    if flow.request.pretty_host in account_domains:
        old = flow.request.host
        flow.request.host = "account"
        flow.request.scheme = "http"
        flow.request.port = 8000
        flow.request.host_header = old
    elif flow.request.pretty_host in miiverse_domains:
        old = flow.request.host
        flow.request.host = "host.docker.internal"
        flow.request.scheme = "http"
        flow.request.port = 8080
        flow.request.host_header = old
    elif flow.request.pretty_host in juxt_domains:
        old = flow.request.host
        flow.request.host = "host.docker.internal"
        flow.request.scheme = "http"
        flow.request.port = 5173
        flow.request.host_header = old
    elif flow.request.pretty_host in s3_domains:
        old = flow.request.host
        flow.request.host = "minio"
        flow.request.scheme = "http"
        flow.request.port = 9000
        #flow.request.host_header = old

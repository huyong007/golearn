# hello.py


def application(env,start_resource):
    start_resource('200 ok',[('content-Type','text/html')])
    body = '<h1>hello,%s!</h1>' % (env['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


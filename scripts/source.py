from subprocess import Popen, PIPE

def source(script, update=True, clean=True):
    """
    Source variables from a shell script
    import them in the environment (if update==True)
    and report only the script variables (if clean==True)
    """

    global environ, environ_back
    if clean:
        environ_back = dict(environ)
        environ.clear()

    pipe = Popen(". %s; env" % script, stdout=PIPE, shell=True)
    data = pipe.communicate()[0]

    env = dict(line.decode().split("=", 1) for line in data.splitlines())

    if clean:
        # remove unwanted minimal vars
        env.pop('_', None)
        env.pop('INPUT_FILE', None)
        env.pop('OUTPUT_FILE', None)
        env.pop('PWD', None)
        env.pop('SHLVL', None)
        environ = dict(environ_back)

    if update:
        environ.update(env)

    return env
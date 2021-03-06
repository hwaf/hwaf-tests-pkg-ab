# -*- python -*-

import waflib.Logs as msg

PACKAGE = {
    'name': 'pkg-ab',
    'author': 'hwaf collaboration',
}

def pkg_deps(ctx):
    ctx.use_pkg('pkg-aa')
    return

def configure(ctx):
    return

def build(ctx):

    ctx.build_linklib(
        name="pkg-ab",
        source="src/pkg-ab.cxx",
        use="ROOT pkg-aa",
        )

    msg.info("ROOT-home: %s" % ctx.env.ROOT_HOME)
    return

def install(ctx):
    return

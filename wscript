# -*- python -*-

import waflib.Logs as msg

def pkg_deps(ctx):
    ctx.use_pkg('pkg-aa')
    return

def configure(ctx):
    ctx.find_root()
    return

def build(ctx):
    ctx(
        features="cxx cxxshlib",
        name="pkg-ab",
        source="src/pkg-ab.cxx",
        target="pkg-ab",
        includes=["inc"],
        export_includes=["inc"],
        use="ROOT pkg-aa",
        )
    def subst(s):
        import waflib.Utils
        return waflib.Utils.subst_vars(s, ctx.env)
    ctx.env['INCLUDES_pkg-ab'] = [subst('${INSTALL_AREA}/include')]
    ctx.env['LIBPATH_pkg-ab'] = [subst('${INSTALL_AREA}/lib')]
    ctx.env['LIB_pkg-ab'] = ['pkg-ab']
    
    incdir = ctx.path.find_node('inc')
    includes = incdir.ant_glob('**/*', dir=False)
    ctx.install_files(
        '${INSTALL_AREA}/include', includes, 
        relative_trick=True,
        cwd=incdir,
        )

    msg.info("ROOT-home: %s" % ctx.env.ROOT_HOME)
    return

def install(ctx):
    return

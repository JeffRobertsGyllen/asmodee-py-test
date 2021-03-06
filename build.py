from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.distutils")


name = "asmodee-py-test"
default_task = "publish"


@init
def initialize(project):
    project.set_property("dir_source_unittest_python", "src/main/python")

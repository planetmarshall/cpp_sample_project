import os

from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.layout import cmake_layout
from conan.tools import microsoft


class CppSampleProjectConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "fPIC": [True, False],
        "shared": [True, False]
    }
    default_options = {
        "fPIC": True,
        "shared": False
    }
    generators = "CMakeToolchain", "CMakeDeps"

    def set_boost_options(self):
        def enable_feature(feature, boolean):
            return f"without_{feature}", not boolean

        options = {
            "atomic": False,
            "chrono": False,
            "container": False,
            "context": False,
            "contract": False,
            "coroutine": False,
            "date_time": False,
            "exception": False,
            "fiber": False,
            "filesystem": False,
            "graph": False,
            "graph_parallel": False,
            "iostreams": False,
            "json": False,
            "locale": False,
            "log": False,
            "math": False,
            "mpi": False,
            "nowide": False,
            "program_options": True,
            "python": False,
            "random": False,
            "regex": False,
            "serialization": False,
            "stacktrace": False,
            "system": False,
            "test": False,
            "thread": False,
            "timer": False,
            "type_erasure": False,
            "wave": False
        }
        for opt, val in options.items():
            feature, disable = enable_feature(opt, val)
            setattr(self.options["boost"], feature, disable)

    def layout(self):
        compiler = "msvc" if microsoft.is_msvc(self) else str(self.settings.compiler)
        build_folder_name = f"{str(self.settings.os)}-{compiler}-{str(self.settings.build_type)}"
        build_folder_path = os.path.join("build", build_folder_name.lower())
        cmake_layout(self, build_folder=build_folder_path)

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        self.set_boost_options()

    def requirements(self):
        self.requires("range-v3/0.12.0")

    def build_requirements(self):
        self.tool_requires("boost/1.80.0")
        self.tool_requires("catch2/3.1.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

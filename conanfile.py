from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools import microsoft, apple


class CppSampleProjectConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "fPIC": [True, False],
        "shared": [True, False],
    }
    default_options = {
        "fPIC": True,
        "shared": False
    }
    generators = "CMakeDeps"

    def requirements(self):
        self.requires("boost/1.85.0")

    def build_requirements(self):
        self.test_requires("catch2/3.6.0")

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
        self.requires("cli11/2.4.2")

    def build_requirements(self):
        self.test_requires("catch2/3.6.0")

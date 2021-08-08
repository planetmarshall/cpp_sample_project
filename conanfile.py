from conans import ConanFile, CMake


class CppSampleProjectConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   generators = "cmake", "cmake_find_package"
   options = {
      "fPIC": [True, False],
      "shared": [True, False]
   }
   default_options = {
      "fPIC": True,
      "shared": False
   }

   def config_options(self):
      if self.settings.os == "Windows":
         del self.options.fPIC

   def build_requirements(self):
      self.build_requires("catch2/2.13.6")
      self.build_requires("ninja/1.10.2")

   def build(self):
      cmake = CMake(self)
      cmake.configure()
      cmake.build()

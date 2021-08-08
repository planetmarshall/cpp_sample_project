from conans import ConanFile


class CppSampleProjectConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   generators = "cmake", "cmake_find_package"

   def build_requirements(self):
      self.build_requires("gtest/1.11.0")

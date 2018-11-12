from conans import ConanFile, tools


class LibbConan(ConanFile):
    name = "libB"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    description = "<Description of Libb here>"
    url = "None"
    license = "None"
    author = "None"
    topics = None

    def build_requirements(self):
        self.build_requires("libA/1.0@test/test")

    def package(self):
        self.copy("*")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

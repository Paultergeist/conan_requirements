from conans import ConanFile, tools


class LibaConan(ConanFile):
    name = "libA"
    version = "2.0"
    settings = "os", "compiler", "build_type", "arch"
    description = "<Description of Liba here>"
    url = "None"
    license = "None"
    author = "None"
    topics = None

    def package(self):
        self.copy("*")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

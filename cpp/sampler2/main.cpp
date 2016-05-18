#include <iostream>
#include<unistd.h>
#include <log4cxx/propertyconfigurator.h> //link:log4cxx

using namespace std;

#define LOG(level,msg) LOG4CXX_##level(log4cxx::Logger::getRootLogger(), msg)
#define LOG2(dest,level,msg) LOG4CXX_##level(log4cxx::Logger::getLogger(#dest), msg)

int main(int argc, char** argv) {
	if(argc < 2) {
		std::cerr << "Usage: logger-file" << std::endl;
		return 1;
	}

	std::cout << "logger file is: " << argv[1] << std::endl;

	// init log4cxx_file
	char buf[16];
	sprintf(buf, "%d", getpid());
	log4cxx::MDC::put("pid", buf);
	log4cxx::PropertyConfigurator::configure(argv[1]);

	LOG2(forStat, DEBUG, "this is debug");
	LOG2(forStat, INFO, "this is info");

	LOG2(forERROR, ERROR, "hello world");

	return 0;
}

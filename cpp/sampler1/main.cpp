#include <log4cxx/logger.h>  
#include <log4cxx/basicconfigurator.h>  
#include <log4cxx/propertyconfigurator.h>  
#include <log4cxx/helpers/exception.h>  
#include <iostream>  

#define LOG(level,msg) LOG4CXX_##level(log4cxx::Logger::getRootLogger(), msg)
#define LOG2(dest,level,msg) LOG4CXX_##level(log4cxx::Logger::getLogger(#dest), msg)

int main(int argc, char **argv)
{  

    if(argc < 2) {
        std::cerr << "Usage: logger-file" << std::endl;
        return 1;
    }

    std::cout << "logger file is: " << argv[1] << std::endl;
    log4cxx::PropertyConfigurator::configure(argv[1]);

    LOG(INFO, "11111111111111111111111111111");
    LOG(DEBUG, "2222222222222222222222222222");
    LOG(ERROR, "2222222222222222222222222222");
    return 0;  
}  

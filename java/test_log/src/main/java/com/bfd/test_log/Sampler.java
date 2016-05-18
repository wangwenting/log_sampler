package com.bfd.test_log;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Hello world!
 *
 */
public class Sampler 
{
	private static final Logger log = LoggerFactory.getLogger(Sampler.class);
    public static void main( String[] args )
    {
    	
        log.info("1111111111111");
        log.debug("222222222222");
        log.error("333333333333333");
    }
}

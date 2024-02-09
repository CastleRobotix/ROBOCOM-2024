package de.castlerobotix;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ExampleMainTest {
	
	@Test
	public void testGetHelloWorld() {
		assertEquals("Hello World!", ExampleMain.getHelloWorld());
	}
	
}

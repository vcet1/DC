import java.rmi.*;

public interface SampleServer extends Remote
{
  public int sum(int a,int b) throws RemoteException;
}

// //compile SampleServer.java
// //compile SampleServerImpl.java
// //compile SampleClient.java

// //start rmi registry
// start rmiregistry

// //create stubs and drivers using the following
// rmic SampleServerImpl

// //run the server
// java –Djava.security.policy=policy.all SampleServerImpl

// //run the client
// java –Djava.security.policy=policy.all SampleClient

// //if it gives an error retype"-" for -D

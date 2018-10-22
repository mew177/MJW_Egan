package Request;

import java.io.Serializable;
import java.util.ArrayList;

public class Activity implements Serializable, Comparable<Activity>{

	/**
	 * 
	 */
	private static final long serialVersionUID = -2193091130641718696L;
	private int TimeStamp;  
	private String requesterID;   // session ID
	private ClientRequest clientRequest;    // Client request
        private int type;   //0 read or write, 1 readSkip, 2 readRelease, 3 writeRelease ;
	
	public Activity(int time, String requestID, ClientRequest clientRequest, int type) 
	{
		// initialization constructor
		this.TimeStamp = time;
		this.requesterID = requestID;
		this.clientRequest=clientRequest;
                
                
	}
        
        public Activity(int type){
              this.type=type;
        }
        
        public static Activity createReadSkip(){
            
            return new Activity(1);
        }
        
        public static Activity createReadRelease(){
            return new Activity(2);
            
        }
        
        public static Activity createWriteRelease(){
            return new Activity(3);
        
        }
        
       
	
	// get TimeStamp of this Request
	public int getTimeStamp() 
	{
		return TimeStamp;
	}
	
	// get Requester ID
	public String getRequesterId()
	{
		return requesterID;
	}
        
        public int getType(){
        return this.type;
        }
        
        public String getInfo(){
        
        return String.valueOf(this.TimeStamp)+" "+this.clientRequest.getTarget()+" "+this.getRequesterId()+" "+this.clientRequest.getType();
        }


	
	// get attached request content
	public ClientRequest getRequest() {
		return clientRequest;
	}
        
        public static Activity requestConversion(int time, String requestID,ClientRequest request){
            
            return new Activity(time,requestID ,request,0);
            
        
        }

    
    @Override
    public int compareTo(Activity o) {
        if(this.TimeStamp<=o.TimeStamp){
        return 1;
             }else{
        return -1;
        }
        
    }
	
	

}

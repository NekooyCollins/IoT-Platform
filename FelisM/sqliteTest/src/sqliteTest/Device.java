package sqliteTest;

public class Device {

	private String id;
	private String user;
	private String identifier;
	private String name;
	private float physicalquantity;
	private String updatetime;
	private int alert;
	private int alertline;
	private int state;
	private String onoff;
	
	public Device(String aid, String auser, String sn, String aname, String aupdatetime, float atemperature, int al, int aline, int astate, String onoff) {
		this.id = aid;
		this.user = auser;
		this.identifier = sn;
		this.name = aname;
		this.physicalquantity = atemperature;
		this.updatetime = aupdatetime;
		this.alert = al;
		this.alertline = aline;
		this.state = astate;
		this.onoff = onoff;
	}
	
	public String getId(){
		return id;
	}
	public void setId(String aid){
		this.id = aid;
	}
	
	public String getUser(){
		return user;
	}
	public void setUser(String auser){
		this.user = auser;
	}
	
	public String getSN(){
		return identifier;
	}
	public void setSN(String sn){
		this.identifier = sn;
	}
	
	public String getName(){
		return name;
	}
	public void setName(String na){
		this.name = na;
	}
	
	public String getLastUpdateTime(){
		return updatetime;
	}
	public void setLastUpdateTime(String lastUpdate){
		this.updatetime = lastUpdate;
	}
	
	public double getTemperature(){
		return physicalquantity;
	}
	public void setTemperature(float atemperature){
		this.physicalquantity = atemperature;
	}
	
	public int getAlarm(){
		return alert;
	}
	public void setAlarm(int al){
		this.alert = al;
	}
	
	public int getAlertLine(){
		return alertline;
	}
	public void setAlertLine(int aline){
		this.alertline = aline;
	}
	
	public int getState(){
		return state;
	}
	public void setState(int aState){
		this.state = aState;
	}
	
	public String getOnoff(){
		return onoff;
	}
	public void setOnoff(String onoff){
		this.onoff = onoff;
	}
}

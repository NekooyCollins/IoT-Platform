package linkSQL;
import java.sql.Connection;
import java.sql.Statement;
import java.sql.Timestamp;
import java.util.Random;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class JDBC {
	
	private static Connection getConn() {
	    String driver = "com.mysql.jdbc.Driver";
	    String url = "jdbc:mysql://127.0.0.1:3306/felism";
	    String username = "root";
	    String password = "";
	    Connection conn = null;
	    try {
	        Class.forName(driver); //classLoader,加载对应驱动
	        conn = (Connection) DriverManager.getConnection(url, username, password);
	    } catch (ClassNotFoundException e) {
	        e.printStackTrace();
	    } catch (SQLException e) {
	        e.printStackTrace();
	    }
	    return conn;
	}
	
	public static void main(String[] args) throws InterruptedException{
		Random random = new Random();
		Connection conn = null;
		Statement pstmt1 = null, pstmt2 = null;
		ResultSet reSetDev; 					// 查询数据
		
		try {
			conn = getConn();
			pstmt1 = conn.createStatement();
			pstmt2 = conn.createStatement();
		} 
		catch (SQLException e) {
			e.printStackTrace();
		}
		
		try {
			pstmt1.executeUpdate("drop table if exists device_history;");
			pstmt1.executeUpdate("create table if not exists default_device(id varchar(5), user varchar(30), identifier varchar(10), name varchar(10), physicalquantity double, alert int,  alertline int, sw int, updatetime Timestamp);");
			pstmt1.executeUpdate("create table if not exists default_history(user varchar(30), identifier varchar(10), name varchar(10), physicalquantity double, alert int,  alertline int, sw int, updatetime Timestamp);");
		} 
		catch (SQLException e1) {
			e1.printStackTrace();
		}
		
		while(true){
			try{
				String id;
				String user;
				String identifier;
				String name;
				double physicalquantity;
				int alert;
				int alertline;
				int sw;
				String onoff;
				Timestamp updatetime;
				reSetDev = pstmt2.executeQuery("select * from default_device;"); // 查询数据
			
				while(reSetDev.next()){
					
					id = reSetDev.getString("id");
					user = reSetDev.getString("user");
					identifier = reSetDev.getString("identifier");
					name = reSetDev.getString("name");
					physicalquantity = random.nextDouble()+35;
					updatetime = new Timestamp(System.currentTimeMillis());
					alert = reSetDev.getInt("alert");
					alertline = reSetDev.getInt("alertline");
					sw = reSetDev.getInt("sw");
					onoff = reSetDev.getString("onoff");
						
					if(sw != 0){
						Thread.sleep(3000);
		                String sq1 = "update default_device set updatetime ='" + updatetime + "',physicalquantity =" + physicalquantity + " where id =" + id + ";";
		                System.out.println(sq1);
		                pstmt1.executeUpdate(sq1); // 插入数据
		                
		                
		                String sq2 = "insert into default_history (user,identifier,name,updatetime,physicalquantity,alert,alertline,sw,onoff) values('" + user +"','"+ identifier + "','" + name+ "','" + updatetime + "'," + physicalquantity + "," + alert + "," + alertline + "," + sw + ",'" + onoff + "');";
		                System.out.println(sq2);
		                
		                //1?2?
		                pstmt1.executeUpdate(sq2);
		                
		                System.out.print("\nidentifier = " + reSetDev.getString("identifier")); // 列属性一
                    	System.out.println("\nname = " + reSetDev.getString("name")); // 列属性二
        				System.out.println("updatetime = " + reSetDev.getString("updatetime")); // 列属性二
        				System.out.println("temperature = " + reSetDev.getDouble("physicalquantity")); // 列属性二
        				System.out.println("alarm = " + reSetDev.getInt("alert")); // 列属性二
        				System.out.println("alarmline = " + reSetDev.getInt("alertline")); // 
        				System.out.println("state = " + reSetDev.getInt("sw")); // 列属性二
        				System.out.println("onoff = " + reSetDev.getString("onoff"));

					}
				}//end while(reSetDev.next())
			}
			catch(SQLException e){
				e.printStackTrace();
				break;
			}
		}// end while(true)
		try {
			conn.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}//end try&catch
	}//end main
}

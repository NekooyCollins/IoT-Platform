package sqliteTest;
import java.sql.*;
import java.util.*;

public class sqliteTest {

	public static void main(String[] args) throws SQLException, InterruptedException{
		//sqlite3_busy_timeout(sqlite3*.100000);
		
		String sql = "jdbc:sqlite://d:/python projects/FelisM/db.sqlite3";
		Connection conn = null;	//连接状态
		Statement stat = null, stat2 = null;		//设备状态
		Random random = new Random();	//随机数的设置
		ResultSet reSetDev; 	// 查询数据
		int flag = 1;
		
		//链接SQLite的JDBC
		try{
		Class.forName("org.sqlite.JDBC");
		conn = DriverManager.getConnection(sql);
		stat = conn.createStatement();
		stat2 = conn.createStatement();
		}
		catch(Exception e){
			e.printStackTrace();
		}//end try&catch
		
		try {
			stat.executeUpdate("drop table if exists default_history;");
			stat.executeUpdate("create table if not exists default_device(id varchar(5), user varchar(30), identifier varchar(10), name varchar(10), physicalquantity double, alert int,  alertline int, sw int, updatetime Timestamp,onoff varchar(5));");
			stat.executeUpdate("create table if not exists default_history(id varchar(5), user varchar(30), identifier varchar(10), name varchar(10), physicalquantity double, alert int,  alertline int, sw int, updatetime Timestamp, onoff varchar(5));");
		} 
		catch (SQLException e1) {
			e1.printStackTrace();
		}
	
		//遍历所有的设备，找出正在运行的设备然后随机分配一个温度值从而完成状态的更新
		while(flag == 1){
			try{
				String id;
				String user;
				String identifier;
				String name;
				String onoff;
				float physicalquantity;
				int alert;
				int alertline;
				int sw;
				Timestamp updatetime;
				reSetDev = stat2.executeQuery("select * from default_device;"); // 查询数据
				
				while(reSetDev.next()){
					
					id = reSetDev.getString("id");
					user = reSetDev.getString("user");
					identifier = reSetDev.getString("identifier");
					name = reSetDev.getString("name");
					physicalquantity = random.nextFloat()+35;
					updatetime = new Timestamp(System.currentTimeMillis());
					alert = reSetDev.getInt("alert");
					alertline = reSetDev.getInt("alertline");
					sw = reSetDev.getInt("sw");
					onoff = reSetDev.getString("onoff");
					
					if(sw != 0){
                    	Thread.sleep(1000);
						String sq1 = "update default_device set updatetime ='" + updatetime + "',physicalquantity =" + physicalquantity + " where id = " + id + ";";
                    	System.out.println(sq1);
                    	stat.executeUpdate(sq1); // 插入数据
                    	
                    	String sq2 = "insert into default_history (id,user,identifier,name,updatetime,physicalquantity,alert,alertline,sw) values('" + id + "','" + user +"','"+ identifier + "','" + name+ "','" + updatetime + "'," + physicalquantity + "," + alert + "," + alertline + "," + sw + ",'" + id + "');";
                    	System.out.println(sq2);
                    	stat.executeUpdate(sq2);
                    	
              
                    	System.out.print("\nidentifier = " + reSetDev.getString("identifier")); // 列属性一
                    	System.out.println("\nname = " + reSetDev.getString("name")); // 列属性二
        				System.out.println("updatetime = " + reSetDev.getString("updatetime")); // 列属性二
        				System.out.println("temperature = " + reSetDev.getDouble("physicalquantity")); // 列属性二
        				System.out.println("alarm = " + reSetDev.getInt("alert")); // 列属性二
        				System.out.println("alarmline = " + reSetDev.getInt("alertline")); // 
        				System.out.println("state = " + reSetDev.getInt("sw")); // 列属性二
                	}// end if
				}//end while(reSetDev.next())
			}
			catch(SQLException e){
				e.printStackTrace();
				break;
			}// end try&catch
			//Sflag = 0;
		}//end while(true)
		
		//关闭连接
		conn.close();
	}
}

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.*;

import com.google.gson.Gson;

public class DataReader {
	public static String readDataQ1() {
		try(BufferedReader br = new BufferedReader(new FileReader(new File("/Users/srividyavaranasi/arun/query1/q1.csv")))) {
			Map<String, String> map = new LinkedHashMap<String, String>();
			String line = null;
			while((line = br.readLine()) != null) {
				try {
					String[] w = line.split(",");
					map.put(w[0], w[1]);
				} catch(Exception e ) {
					
				}
			}
			Gson gson = new Gson(); 
		    String json = gson.toJson(map);
		    return json;
		} catch(Exception e) {
			e.printStackTrace();
		}
		return null;
	}
	
	public static String readDataQ2() {
		try(BufferedReader br = new BufferedReader(new FileReader(new File("/Users/srividyavaranasi/arun/query2/q2.csv")))) {
			Map<String, String> map = new LinkedHashMap<String, String>();
			String line = null;
			while((line = br.readLine()) != null) {
				try {
					String[] w = line.split(",");
					map.put(w[0], w[1]);
				} catch(Exception e ) {
					
				}
			}
			Gson gson = new Gson(); 
		    String json = gson.toJson(map);
		    return json;
		} catch(Exception e) {
			e.printStackTrace();
		}
		return null;
	}
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package unread_email_count;

/**
 *
 * @author MA
 */

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.io.IOException;
import javax.net.ssl.HttpsURLConnection;
import javax.swing.JOptionPane;
public class Unread_email_count {

  
	private final String USER_AGENT = "Mozilla/5.0";


	// HTTP GET request
	public String sendGet(String param1, String param2, String hostname, String port) throws Exception {
            try{String url = "http://"+ hostname + ":" + port;//"http://192.168.0.122:8080";
                String charset = "UTF-8";  // Or in Java 7 and later, use the constant: java.nio.charset.StandardCharsets.UTF_8.name()
               
                String query = String.format("login=%s&pwd=%s", 
                URLEncoder.encode(param1, charset), 
                URLEncoder.encode(param2, charset));
            
		URL obj = new URL(url + "?" + query);
		HttpURLConnection con = (HttpURLConnection) obj.openConnection();

		// optional default is GET
		con.setRequestMethod("GET");

		//add request header
		con.setRequestProperty("User-Agent", USER_AGENT);
		int responseCode = con.getResponseCode();
		System.out.println("\nSending 'GET' request to URL : " + url );
		System.out.println("Response Code : " + responseCode);

		BufferedReader in = new BufferedReader(
		        new InputStreamReader(con.getInputStream()));
		String inputLine;
		StringBuffer response = new StringBuffer();

		while ((inputLine = in.readLine()) != null) {
			response.append(inputLine);
		}
		in.close();

		//print result
		System.out.println(response.toString());
                if(response.toString().equals("NULL"))
                    JOptionPane.showMessageDialog(null, "Invalid login or password.\nPlease correct and try again.");
                return response.toString();}
            catch(Exception e){                
                JOptionPane.showMessageDialog(null, "Could not connect to http server.\nPlease check settings and try again.");
                return "NULL";}
	}
    
}

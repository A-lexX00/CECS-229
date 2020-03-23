/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cecs323.jbdcproject;

import java.beans.Statement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 *
 * @author thefr
 */
public class userInterface {
     public static void main(String[] args){
        Connection myconObj = null;
        Statement mystatObj = null;
        ResultSet myresObj = null;
        
        try{
            myconObj = DriverManager.getConnection("jdbc:derby://localhost:1527/jdbcDatabase");
        }
        catch(SQLException e){
            e.printStackTrace();
        }
    }
}

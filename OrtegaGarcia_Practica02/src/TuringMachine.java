

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;

import netscape.javascript.JSException;

import java.util.Scanner;
import java.util.ArrayList;

public class TuringMachine {

    //ArrayList que representa los estados de nuestra MT.
    ArrayList<String> estados = new ArrayList<String>();
    
    //ArrayList que representa el alfabeto de entrada de nuestra MT.
    ArrayList<String> entrada = new ArrayList<String>();


    public static void main(String[] args) throws Exception {
        
        TuringMachine mt = new TuringMachine();
        //Reader r = new Reader();
        JSONParser parser = new JSONParser();
		Scanner sc = new Scanner(System.in);
        System.out.println("Introduce el nombre del archivo con la descripción de la MT: ");
        String name = "";
        name = sc.nextLine();

        try{

            // parsing file "JSONExample.json"
             Object ob = parser.parse(new FileReader(name));
        
            // typecasting ob to JSONObject
            JSONObject js = (JSONObject) ob;

            mt.estados = (ArrayList<String>) js.get("Estados");
            mt.entrada = (ArrayList<String>) js.get("Entrada");

        } catch(FileNotFoundException e) {}
        catch(IOException e) {}
        //catch(ParseException e) {}

        System.out.println(mt.estados);
        System.out.println(".");
    }
}
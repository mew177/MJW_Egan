/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Server1;

import Request.ClientRequest;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author brantxu
 */
public class ClientHandle extends Thread {

    private Socket socket;
    
    public ClientHandle(Socket socket) throws IOException {
        this.socket = socket;
        
    }

    public void run() {

        try {
            
            String result = ActivityHandler.Handle(socket, "S1"+this.getId());
            PrintWriter pw = new PrintWriter(socket.getOutputStream());
            
            pw.write(result);
            pw.flush();
            socket.close();

        } catch (IOException ex) {
            Logger.getLogger(ClientHandle.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(ClientHandle.class.getName()).log(Level.SEVERE, null, ex);
        } catch (InterruptedException ex) {
            Logger.getLogger(ClientHandle.class.getName()).log(Level.SEVERE, null, ex);
        }

    }
}

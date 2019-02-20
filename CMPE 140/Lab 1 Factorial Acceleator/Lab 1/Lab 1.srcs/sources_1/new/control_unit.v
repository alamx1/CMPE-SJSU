`timescale 1ns / 1ps

module control_unit( 
    input clk, 
    input go, 
    input gt,
    input error,
	output reg [5:0] out,
	//Verification variables
	output reg [1:0] cs, ns
    );
    // internal constants (states)
    // IDLE = S0, WAIT = S3, ADD = S4, SUB = S5....etc
    parameter IDLE = 2'b00, ST1 = 2'b01, ST2 = 2'b10, ERR =  2'b11;
    
    // internal registers
    //reg [2:0] ns;
    //reg [2:0] cs;
    
    initial // start at IDLE;
        begin
            cs = IDLE;
        end
    
    always @ (cs,go,gt,error) // FSM state transitions
        begin
            case(cs)
                IDLE: begin // IF GO is active, go to ST1, if not stay idle
                        if (go) 
                          ns = ST1; 
                        else 
                          ns = IDLE;
                      end
                ST1: begin
                        if (error)
                            ns = ERR;
                        else                           
                        ns = ST2;
                     end   
                ST2: begin 
                        if (gt) 
                          ns = ST2; 
                        else 
                          ns = IDLE;
                      end 
                 ERR: ns = IDLE;     
                default: ns = IDLE;
            endcase
        end
        
     // Output logic combinatorial
     always @ (ns,cs,gt)
        begin
            case(ns)
                IDLE: //out = 6'b000000;
                      begin
                        if(cs == ST2)
                          out = 6'b000011;
                        else  
                          out = 6'b000000;
                      end//*/                      
                ST1:  out = 6'b111100;
                ST2:  begin
                        if  (gt == 1)
                          out = 6'b001100;    
                        else 
                          out = 6'b000011;      
                      end    
                 ERR: out = 6'b000001;                   
            endcase
            #1;
       end
                      
      // Sequential
     always @ (posedge clk)
        begin
            cs <= ns; // change states on positive edge clock
        end              
endmodule

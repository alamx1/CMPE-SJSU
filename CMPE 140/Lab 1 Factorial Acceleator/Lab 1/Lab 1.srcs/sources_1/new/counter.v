`timescale 1ns / 1ps

module counter#(parameter WIDTH = 4)(
    input clk,
    input en,
    input ld,
    input [WIDTH-1:0] d,
    output reg [WIDTH-1:0] q
    );

always @ (posedge clk) begin
   if(en)//ce = 1
      begin
        if(ld)//ld = 1 Load
          q = d;
        else//ld = 0 
          q = q-1;     
      end         
    end 
endmodule

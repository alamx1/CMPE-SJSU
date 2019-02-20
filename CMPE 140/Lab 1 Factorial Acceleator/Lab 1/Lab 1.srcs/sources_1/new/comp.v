`timescale 1ns / 1ps

module comp(
    input [3:0] a,    
    input [3:0] b,
    output gt
  );
  assign gt = (a>b) ? 1 : 0;
    
endmodule


`timescale 1ns / 1ps

module multiplier#(parameter WIDTH = 4)(
    input [WIDTH-1:0] a,
    input [WIDTH-1:0] b,
    output reg[2*WIDTH-1:0] p
    );
    always@(a,b)
    begin
      p = a * b;
    end
endmodule

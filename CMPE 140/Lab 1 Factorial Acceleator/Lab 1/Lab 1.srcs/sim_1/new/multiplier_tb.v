`timescale 1ns / 1ps

module multiplier_tb;
reg [3:0] a_tb, b_tb;
reg [7:0] p_tb;
wire [7:0] p_dut;

multiplier MUL(
    .a      (a_tb),
    .b      (b_tb),    
    .p      (p_dut)
);

integer i, j;

initial
begin
    for(i = 0; i < 2 ** 4; i = i + 1)
    begin                
       for(j = 0; j < 2 ** 4; j = j + 1)
       begin
         #2;
         a_tb = i;
         b_tb = j;
         p_tb = a_tb * b_tb;
       end
    end   
    $finish;
end

endmodule

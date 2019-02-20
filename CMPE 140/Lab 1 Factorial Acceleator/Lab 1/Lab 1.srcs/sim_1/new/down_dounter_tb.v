`timescale 1ns / 1ps

module down_counter_tb;
    reg [3:0] d_tb, q_tb;
    wire [3:0] q_dut;
    reg ld, en;
    wire error;
    reg clk;
    
    counter CNT(
        .clk    (clk),
        .en     (en),
        .ld     (ld),
        .d      (d_tb),
        .q      (q_dut),
        .error  (error)
    );
        
    task tick;
    begin
        clk = 1;
        #5 clk = 0;
        #5;
    end
    endtask  
    
    initial
    begin
        en = 1;
        ld = 1;
        d_tb = 5;
        tick;
        ld = 0;
        tick;
        tick;
    
        $finish;
    end
    
endmodule

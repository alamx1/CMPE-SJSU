`timescale 1ns / 1ps

module nfactorial_tb;
  wire done, error;
  wire [31:0] out;
  reg clk, go;  
  reg [3:0] n;
  wire [1:0] cs, ns;
  wire [3:0] q_cnt;
  wire [31:0] q_reg,d_reg,p;
   
  nfactorial FAC(
    .clk    (clk),
    .go     (go),
    .n      (n),
    .done   (done),
    .error  (error),
    .out    (out),
    //verification variables  
    .q_cnt  (q_cnt),
    .q_reg  (q_reg),
    .d_reg  (d_reg),
    .p      (p),
    .ns     (ns),
    .cs     (cs)  
  );
  
task tick;
  begin
    clk = 1;
    #5 clk = 0;
    #5;    
  end
endtask

integer i;

initial
begin
    go = 0;
    tick;
    for (i = 0; i < 13; i = i + 1)
    begin
        n = i;
        go = 1;
        tick;
        go = 0;
        tick;
        while(~done)
        begin
            tick;
        end
        tick;
    end
    $finish;
end
endmodule
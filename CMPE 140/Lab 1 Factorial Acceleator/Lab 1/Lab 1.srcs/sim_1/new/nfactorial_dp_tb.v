`timescale 1ns / 1ps

module nfactorial_dp_tb;

reg clk;
reg [3:0] n;
reg sel,ld_cnt,en,ld_reg,oe,done;
wire gt,error;
wire [3:0] q_cnt;
wire [31:0] d_reg, q_reg,p,out;
//integer i;

nfactorial_dp DP(
  .clk      (clk),
  .sel      (sel),
  .ld_cnt   (ld_cnt),
  .en       (en),
  .ld_reg   (ld_reg),
  .oe       (oe),
  .done     (done),
  .n        (n),
  .gt       (gt),
  .error    (error),
  .q_cnt    (q_cnt),
  .q_reg    (q_reg),
  .d_reg    (d_reg),
  .p        (p),
  .out      (out)
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
    n = 4;
    {sel,ld_cnt,en,ld_reg,oe,done} = 6'b000000;//ST0
    tick;
    {sel,ld_cnt,en,ld_reg,oe,done} = 6'b111100;//ST1
    tick;
    {sel,ld_cnt,en,ld_reg,oe,done} = 6'b001100;//ST2 GT
    tick;
    {sel,ld_cnt,en,ld_reg,oe,done} = 6'b001100;//ST2 GT
    tick;
    {sel,ld_cnt,en,ld_reg,oe,done} = 6'b001100;//ST2 GT
    tick;   
    {sel,ld_cnt,en,ld_reg,oe,done} = 6'b000011;//ST2 GT'
    tick;
    $finish;
end
endmodule

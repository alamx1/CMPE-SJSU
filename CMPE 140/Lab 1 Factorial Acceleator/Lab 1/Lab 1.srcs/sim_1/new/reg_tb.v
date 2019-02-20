module reg_tb;

reg ld_reg, clk;
reg [31:0] d;
wire [31:0] q;

task tick;
begin
    clk = 1;
    #5 clk = 0;
    #5;
end
endtask

register #(32) REG(
      .ld   (ld_reg),
      .clk  (clk),
      .d    (d),
      .q    (q)
    );
    
initial
begin
    d = 3;
    ld_reg = 1;
    tick;
    ld_reg = 0;
    d = 4;
    tick;
    $finish;
end 
endmodule    
    
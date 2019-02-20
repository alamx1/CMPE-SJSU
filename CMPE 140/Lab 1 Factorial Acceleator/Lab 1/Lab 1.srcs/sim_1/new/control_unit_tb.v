module cu_tb;

reg clk, go, gt;
wire [1:0] cs, ns;
wire sel, ld_cnt,en,ld_reg,oe,done;


control_unit CU(
    .clk    (clk), 
    .go     (go), 
    .gt     (gt),
	.out    ({sel, ld_cnt,en,ld_reg,oe,done}),
    //verification variables
    .cs     (cs),
    .ns     (ns)	
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
    go = 0;
    gt = 0;
    tick;
    go = 1;
    tick;
    go = 0;
    gt = 1;
    tick;
    gt = 1;
    tick;
    gt = 1;
    tick;
    gt  = 0;
    tick;
    tick;
    $finish;
end

endmodule
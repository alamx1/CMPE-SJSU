module mux2_tb;

reg sel;
reg [3:0] in0, in1;
wire [3:0] out;

mux2 MUX(
      .sel      (sel),
      .in0      (in0),
      .in1      (in1),
      .out      (out)
    );
    
initial
begin
    in0 = 0;
    in1 = 15;
    sel = 0;
    #5;
    sel = 1;
    #5;
    $finish;
end
endmodule    
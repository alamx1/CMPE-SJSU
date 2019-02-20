
module nfactorial(
      input clk,
      input go,
      input [3:0] n,
      output done,
      output error,
      output [31:0]out,
      //Troubleshooting variables
      output [31:0] q_cnt,
      output [31:0] q_reg,
      output [31:0] d_reg,
      output [31:0] p,
      output [1:0] ns,
      output [1:0] cs,
      output gt
    );

    wire [5:0] ctrl;
    //wire [1:0] ns,cs;
    //wire gt;
    
    assign done = ctrl[0];

    nfactorial_dp DP(
      .clk      (clk),
      .sel      (ctrl[5]), 
      .ld_cnt   (ctrl[4]),
      .en       (ctrl[3]),
      .ld_reg   (ctrl[2]),
      .oe       (ctrl[1]),
      .done     (ctrl[0]),
      .n        (n),
      .gt       (gt),
      .error    (error),
       //outputs used for verification
      .q_cnt    (q_cnt),
      .q_reg    (q_reg),
      .d_reg    (d_reg),
      .p        (p),
      .out      (out)    
    );
    
    control_unit CU(
      .clk      (clk), 
      .go       (go), 
      .gt       (gt),
      .error    (error),
      .out      (ctrl),
      .ns       (ns),
      .cs       (cs)
    );

endmodule
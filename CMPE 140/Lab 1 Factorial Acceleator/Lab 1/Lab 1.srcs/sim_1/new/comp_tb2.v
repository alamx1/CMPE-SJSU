`timescale 1ns / 1ps

module comp_tb;

  reg [3:0] a_tb, b_tb;
  reg gt_tb;
  wire gt;

  comp CMP(
    .a      (a_tb),
    .b      (b_tb),
    .gt     (gt)
  );
  
  integer i, j;
  
  initial
  begin
    for (i = 0; i < 2**3; i = i+1)
        for(j = 0; j < 2**3; j = j+1)
        begin
            a_tb = i;
            b_tb = j;
            gt_tb = (a_tb > b_tb) ? 1 : 0;
            #2;
        end    
    $finish;
  end  
endmodule

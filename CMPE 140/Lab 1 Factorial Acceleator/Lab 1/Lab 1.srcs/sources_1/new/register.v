module register #(parameter WIDTH = 4)(
         input ld,
         input clk,
         input [WIDTH-1:0] d,
         output reg [WIDTH-1:0] q
    );
    
    always@(posedge clk)
    begin
        if(ld)  
            q = d;
        else 
            q = q;    
    end
    
endmodule    
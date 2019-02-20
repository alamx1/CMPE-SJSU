module buff#(parameter WIDTH = 4)(
        input oe,
        input [WIDTH-1:0] d,
        output reg[WIDTH-1:0] out
    );
    
    always@(oe)
    begin
            out = d;
    end
endmodule    
--Copyright (C) 2016 Siavoosh Payandeh Azad
------------------------------------------------------------
-- This file is automatically generated!
-- Here are the parameters:
-- 	 network size x: 2
-- 	 network size y: 2
-- 	 LV network: True
-- 	 Data width: 32
-- 	 Parity: False
-- 	 Fault injectors: False
------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
USE ieee.numeric_std.ALL; 

entity network_2x2 is
 generic (DATA_WIDTH: integer := 32);
port (reset: in  std_logic; 
	clk: in  std_logic; 
	--------------
	RX_L_0: in std_logic_vector (DATA_WIDTH-1 downto 0);
	credit_out_L_0, valid_out_L_0: out std_logic;
	credit_in_L_0, valid_in_L_0: in std_logic;
	TX_L_0: out std_logic_vector (DATA_WIDTH-1 downto 0);
	--------------
	RX_L_1: in std_logic_vector (DATA_WIDTH-1 downto 0);
	credit_out_L_1, valid_out_L_1: out std_logic;
	credit_in_L_1, valid_in_L_1: in std_logic;
	TX_L_1: out std_logic_vector (DATA_WIDTH-1 downto 0);
	--------------
	RX_L_2: in std_logic_vector (DATA_WIDTH-1 downto 0);
	credit_out_L_2, valid_out_L_2: out std_logic;
	credit_in_L_2, valid_in_L_2: in std_logic;
	TX_L_2: out std_logic_vector (DATA_WIDTH-1 downto 0);
	--------------
	RX_L_3: in std_logic_vector (DATA_WIDTH-1 downto 0);
	credit_out_L_3, valid_out_L_3: out std_logic;
	credit_in_L_3, valid_in_L_3: in std_logic;
	TX_L_3: out std_logic_vector (DATA_WIDTH-1 downto 0);
	--------------
    credit_in_LV_0: in std_logic;
    valid_out_LV_0 : out std_logic;
    TX_LV_0: out std_logic_vector (DATA_WIDTH-1 downto 0);

	--------------
    credit_in_LV_1: in std_logic;
    valid_out_LV_1 : out std_logic;
    TX_LV_1: out std_logic_vector (DATA_WIDTH-1 downto 0);

	--------------
    credit_in_LV_2: in std_logic;
    valid_out_LV_2 : out std_logic;
    TX_LV_2: out std_logic_vector (DATA_WIDTH-1 downto 0);

	--------------
    credit_in_LV_3: in std_logic;
    valid_out_LV_3 : out std_logic;
    TX_LV_3: out std_logic_vector (DATA_WIDTH-1 downto 0)
            ); 
end network_2x2; 


architecture behavior of network_2x2 is

component router_credit_based_parity_lv is
    generic (
        DATA_WIDTH: integer := 32;
        current_address : integer := 0;
        Rxy_rst : integer := 60;
        Cx_rst : integer := 10;
        NoC_size: integer := 4
    );
    port (
    reset, clk: in std_logic;

    RX_N, RX_E, RX_W, RX_S, RX_L : in std_logic_vector (DATA_WIDTH-1 downto 0); 
    credit_in_N, credit_in_E, credit_in_W, credit_in_S, credit_in_L: in std_logic;
    valid_in_N, valid_in_E, valid_in_W, valid_in_S, valid_in_L : in std_logic;
    valid_out_N, valid_out_E, valid_out_W, valid_out_S, valid_out_L : out std_logic;
    credit_out_N, credit_out_E, credit_out_W, credit_out_S, credit_out_L: out std_logic;
    TX_N, TX_E, TX_W, TX_S, TX_L: out std_logic_vector (DATA_WIDTH-1 downto 0);
    ------------------------- lV network port
    -- the router just sends the packets out. no need for any incomming packets support. 
    -- the output of the LV network will be connected to the PEs

    credit_in_LV: in std_logic;
    valid_out_LV : out std_logic;
    TX_LV: out std_logic_vector (DATA_WIDTH-1 downto 0)
 ); 
end component;


component router_LV is
	generic (
        DATA_WIDTH: integer := 11;
        current_address : integer := 0;
        Rxy_rst : integer := 60;
        Cx_rst : integer := 10;
        NoC_size: integer := 4
    );
    port (
    reset, clk: in std_logic;

    RX_N, RX_E, RX_W, RX_S, RX_L : in std_logic_vector (DATA_WIDTH-1 downto 0); 

    credit_in_N, credit_in_E, credit_in_W, credit_in_S, credit_in_L: in std_logic;
    valid_in_N, valid_in_E, valid_in_W, valid_in_S, valid_in_L : in std_logic;

    valid_out_N, valid_out_E, valid_out_W, valid_out_S, valid_out_L : out std_logic;
    credit_out_N, credit_out_E, credit_out_W, credit_out_S, credit_out_L: out std_logic;

    TX_N, TX_E, TX_W, TX_S, TX_L: out std_logic_vector (DATA_WIDTH-1 downto 0)
    ); 
end component;




-- generating bulk signals. not all of them are used in the design...
	signal credit_out_N_0, credit_out_E_0, credit_out_W_0, credit_out_S_0: std_logic;
	signal credit_out_N_1, credit_out_E_1, credit_out_W_1, credit_out_S_1: std_logic;
	signal credit_out_N_2, credit_out_E_2, credit_out_W_2, credit_out_S_2: std_logic;
	signal credit_out_N_3, credit_out_E_3, credit_out_W_3, credit_out_S_3: std_logic;

	signal credit_in_N_0, credit_in_E_0, credit_in_W_0, credit_in_S_0: std_logic;
	signal credit_in_N_1, credit_in_E_1, credit_in_W_1, credit_in_S_1: std_logic;
	signal credit_in_N_2, credit_in_E_2, credit_in_W_2, credit_in_S_2: std_logic;
	signal credit_in_N_3, credit_in_E_3, credit_in_W_3, credit_in_S_3: std_logic;

	signal RX_N_0, RX_E_0, RX_W_0, RX_S_0 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal RX_N_1, RX_E_1, RX_W_1, RX_S_1 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal RX_N_2, RX_E_2, RX_W_2, RX_S_2 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal RX_N_3, RX_E_3, RX_W_3, RX_S_3 : std_logic_vector (DATA_WIDTH-1 downto 0);

	signal valid_out_N_0, valid_out_E_0, valid_out_W_0, valid_out_S_0: std_logic;
	signal valid_out_N_1, valid_out_E_1, valid_out_W_1, valid_out_S_1: std_logic;
	signal valid_out_N_2, valid_out_E_2, valid_out_W_2, valid_out_S_2: std_logic;
	signal valid_out_N_3, valid_out_E_3, valid_out_W_3, valid_out_S_3: std_logic;

	signal valid_in_N_0, valid_in_E_0, valid_in_W_0, valid_in_S_0: std_logic;
	signal valid_in_N_1, valid_in_E_1, valid_in_W_1, valid_in_S_1: std_logic;
	signal valid_in_N_2, valid_in_E_2, valid_in_W_2, valid_in_S_2: std_logic;
	signal valid_in_N_3, valid_in_E_3, valid_in_W_3, valid_in_S_3: std_logic;

	signal TX_N_0, TX_E_0, TX_W_0, TX_S_0 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal TX_N_1, TX_E_1, TX_W_1, TX_S_1 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal TX_N_2, TX_E_2, TX_W_2, TX_S_2 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal TX_N_3, TX_E_3, TX_W_3, TX_S_3 : std_logic_vector (DATA_WIDTH-1 downto 0);


	signal RX_LV_N0, RX_LV_E0, RX_LV_W0, RX_LV_S0, RX_LV_L0 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal RX_LV_N1, RX_LV_E1, RX_LV_W1, RX_LV_S1, RX_LV_L1 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal RX_LV_N2, RX_LV_E2, RX_LV_W2, RX_LV_S2, RX_LV_L2 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal RX_LV_N3, RX_LV_E3, RX_LV_W3, RX_LV_S3, RX_LV_L3 : std_logic_vector (DATA_WIDTH-1 downto 0);

	signal credit_in_LV_N0, credit_in_LV_E0, credit_in_LV_W0, credit_in_LV_S0, credit_in_LV_L0: std_logic;
	signal credit_in_LV_N1, credit_in_LV_E1, credit_in_LV_W1, credit_in_LV_S1, credit_in_LV_L1: std_logic;
	signal credit_in_LV_N2, credit_in_LV_E2, credit_in_LV_W2, credit_in_LV_S2, credit_in_LV_L2: std_logic;
	signal credit_in_LV_N3, credit_in_LV_E3, credit_in_LV_W3, credit_in_LV_S3, credit_in_LV_L3: std_logic;

	signal credit_out_LV_N0, credit_out_LV_E0, credit_out_LV_W0, credit_out_LV_S0, credit_out_LV_L0: std_logic;
	signal credit_out_LV_N1, credit_out_LV_E1, credit_out_LV_W1, credit_out_LV_S1, credit_out_LV_L1: std_logic;
	signal credit_out_LV_N2, credit_out_LV_E2, credit_out_LV_W2, credit_out_LV_S2, credit_out_LV_L2: std_logic;
	signal credit_out_LV_N3, credit_out_LV_E3, credit_out_LV_W3, credit_out_LV_S3, credit_out_LV_L3: std_logic;

	signal valid_in_LV_N0, valid_in_LV_E0, valid_in_LV_W0, valid_in_LV_S0, valid_in_LV_L0: std_logic;
	signal valid_in_LV_N1, valid_in_LV_E1, valid_in_LV_W1, valid_in_LV_S1, valid_in_LV_L1: std_logic;
	signal valid_in_LV_N2, valid_in_LV_E2, valid_in_LV_W2, valid_in_LV_S2, valid_in_LV_L2: std_logic;
	signal valid_in_LV_N3, valid_in_LV_E3, valid_in_LV_W3, valid_in_LV_S3, valid_in_LV_L3: std_logic;

	signal valid_out_LV_N0, valid_out_LV_E0, valid_out_LV_W0, valid_out_LV_S0, valid_out_LV_L0: std_logic;
	signal valid_out_LV_N1, valid_out_LV_E1, valid_out_LV_W1, valid_out_LV_S1, valid_out_LV_L1: std_logic;
	signal valid_out_LV_N2, valid_out_LV_E2, valid_out_LV_W2, valid_out_LV_S2, valid_out_LV_L2: std_logic;
	signal valid_out_LV_N3, valid_out_LV_E3, valid_out_LV_W3, valid_out_LV_S3, valid_out_LV_L3: std_logic;


	signal TX_LV_N0, TX_LV_E0, TX_LV_W0, TX_LV_S0, TX_LV_L0 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal TX_LV_N1, TX_LV_E1, TX_LV_W1, TX_LV_S1, TX_LV_L1 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal TX_LV_N2, TX_LV_E2, TX_LV_W2, TX_LV_S2, TX_LV_L2 : std_logic_vector (DATA_WIDTH-1 downto 0);
	signal TX_LV_N3, TX_LV_E3, TX_LV_W3, TX_LV_S3, TX_LV_L3 : std_logic_vector (DATA_WIDTH-1 downto 0);



--        organizaiton of the network:
--     x --------------->
--  y         ----       ----
--  |        | 0  | --- | 1  |
--  |         ----       ----
--  |          |          |
--  |         ----       ----
--  |        | 2  | --- | 3  |
--  v         ----       ----
--                         
begin


R_0: router_credit_based_parity_lv 
	generic map (DATA_WIDTH =>DATA_WIDTH,         current_address => 0, Rxy_rst => 60,
        Cx_rst =>  10, NoC_size => 2)
    port map(
    reset, clk,
	RX_N_0, RX_E_0, RX_W_0, RX_S_0, RX_L_0,
	credit_in_N_0, credit_in_E_0, credit_in_W_0, credit_in_S_0, credit_in_L_0,
	valid_in_N_0, valid_in_E_0, valid_in_W_0, valid_in_S_0, valid_in_L_0,
	valid_out_N_0, valid_out_E_0, valid_out_W_0, valid_out_S_0, valid_out_L_0,
	credit_out_N_0, credit_out_E_0, credit_out_W_0, credit_out_S_0, credit_out_L_0,
	TX_N_0, TX_E_0, TX_W_0, TX_S_0, TX_L_0,    ------------------------- lV network port
    -- the router just sends the packets out. no need for any incomming packets support. 
    -- the output of the LV network will be connected to the PEs

    credit_out_LV_L0,
    valid_in_LV_L0,
    RX_LV_L0
 ); 
R_1: router_credit_based_parity_lv 
	generic map (DATA_WIDTH =>DATA_WIDTH,         current_address => 1, Rxy_rst => 60,
        Cx_rst =>  12, NoC_size => 2)
    port map(
    reset, clk,
	RX_N_1, RX_E_1, RX_W_1, RX_S_1, RX_L_1,
	credit_in_N_1, credit_in_E_1, credit_in_W_1, credit_in_S_1, credit_in_L_1,
	valid_in_N_1, valid_in_E_1, valid_in_W_1, valid_in_S_1, valid_in_L_1,
	valid_out_N_1, valid_out_E_1, valid_out_W_1, valid_out_S_1, valid_out_L_1,
	credit_out_N_1, credit_out_E_1, credit_out_W_1, credit_out_S_1, credit_out_L_1,
	TX_N_1, TX_E_1, TX_W_1, TX_S_1, TX_L_1,    ------------------------- lV network port
    -- the router just sends the packets out. no need for any incomming packets support. 
    -- the output of the LV network will be connected to the PEs

    credit_out_LV_L1,
    valid_in_LV_L1,
    RX_LV_L1
 ); 
R_2: router_credit_based_parity_lv 
	generic map (DATA_WIDTH =>DATA_WIDTH,         current_address => 2, Rxy_rst => 60,
        Cx_rst =>  3, NoC_size => 2)
    port map(
    reset, clk,
	RX_N_2, RX_E_2, RX_W_2, RX_S_2, RX_L_2,
	credit_in_N_2, credit_in_E_2, credit_in_W_2, credit_in_S_2, credit_in_L_2,
	valid_in_N_2, valid_in_E_2, valid_in_W_2, valid_in_S_2, valid_in_L_2,
	valid_out_N_2, valid_out_E_2, valid_out_W_2, valid_out_S_2, valid_out_L_2,
	credit_out_N_2, credit_out_E_2, credit_out_W_2, credit_out_S_2, credit_out_L_2,
	TX_N_2, TX_E_2, TX_W_2, TX_S_2, TX_L_2,    ------------------------- lV network port
    -- the router just sends the packets out. no need for any incomming packets support. 
    -- the output of the LV network will be connected to the PEs

    credit_out_LV_L2,
    valid_in_LV_L2,
    RX_LV_L2
 ); 
R_3: router_credit_based_parity_lv 
	generic map (DATA_WIDTH =>DATA_WIDTH,         current_address => 3, Rxy_rst => 60,
        Cx_rst =>  5, NoC_size => 2)
    port map(
    reset, clk,
	RX_N_3, RX_E_3, RX_W_3, RX_S_3, RX_L_3,
	credit_in_N_3, credit_in_E_3, credit_in_W_3, credit_in_S_3, credit_in_L_3,
	valid_in_N_3, valid_in_E_3, valid_in_W_3, valid_in_S_3, valid_in_L_3,
	valid_out_N_3, valid_out_E_3, valid_out_W_3, valid_out_S_3, valid_out_L_3,
	credit_out_N_3, credit_out_E_3, credit_out_W_3, credit_out_S_3, credit_out_L_3,
	TX_N_3, TX_E_3, TX_W_3, TX_S_3, TX_L_3,    ------------------------- lV network port
    -- the router just sends the packets out. no need for any incomming packets support. 
    -- the output of the LV network will be connected to the PEs

    credit_out_LV_L3,
    valid_in_LV_L3,
    RX_LV_L3
 ); 

-- instantiating the LV routers
R_lv_0: router_LV generic map (DATA_WIDTH => 11, 
current_address =>0, Rxy_rst => 60, Cx_rst =>10, 
 NoC_size =>2)    PORT MAP (reset, clk, RX_LV_N0, RX_LV_E0, RX_LV_W0, RX_LV_S0, RX_LV_L0,
     credit_in_LV_N0, credit_in_LV_E0, credit_in_LV_W0, credit_in_LV_S0, credit_in_LV_L0,
    valid_in_LV_N0, valid_in_LV_E0, valid_in_LV_W0, valid_in_LV_S0, valid_in_LV_L0,
    valid_out_LV_N0, valid_out_LV_E0, valid_out_LV_W0, valid_out_LV_S0, valid_out_LV_L0,
    credit_out_LV_N0, credit_out_LV_E0, credit_out_LV_W0, credit_out_LV_S0, credit_out_LV_L0,
    TX_LV_N0, TX_LV_E0, TX_LV_W0, TX_LV_S0, TX_LV_L0
    ); 
R_lv_1: router_LV generic map (DATA_WIDTH => 11, 
current_address =>1, Rxy_rst => 60, Cx_rst =>12, 
 NoC_size =>2)    PORT MAP (reset, clk, RX_LV_N1, RX_LV_E1, RX_LV_W1, RX_LV_S1, RX_LV_L1,
     credit_in_LV_N1, credit_in_LV_E1, credit_in_LV_W1, credit_in_LV_S1, credit_in_LV_L1,
    valid_in_LV_N1, valid_in_LV_E1, valid_in_LV_W1, valid_in_LV_S1, valid_in_LV_L1,
    valid_out_LV_N1, valid_out_LV_E1, valid_out_LV_W1, valid_out_LV_S1, valid_out_LV_L1,
    credit_out_LV_N1, credit_out_LV_E1, credit_out_LV_W1, credit_out_LV_S1, credit_out_LV_L1,
    TX_LV_N1, TX_LV_E1, TX_LV_W1, TX_LV_S1, TX_LV_L1
    ); 
R_lv_2: router_LV generic map (DATA_WIDTH => 11, 
current_address =>2, Rxy_rst => 60, Cx_rst =>3, 
 NoC_size =>2)    PORT MAP (reset, clk, RX_LV_N2, RX_LV_E2, RX_LV_W2, RX_LV_S2, RX_LV_L2,
     credit_in_LV_N2, credit_in_LV_E2, credit_in_LV_W2, credit_in_LV_S2, credit_in_LV_L2,
    valid_in_LV_N2, valid_in_LV_E2, valid_in_LV_W2, valid_in_LV_S2, valid_in_LV_L2,
    valid_out_LV_N2, valid_out_LV_E2, valid_out_LV_W2, valid_out_LV_S2, valid_out_LV_L2,
    credit_out_LV_N2, credit_out_LV_E2, credit_out_LV_W2, credit_out_LV_S2, credit_out_LV_L2,
    TX_LV_N2, TX_LV_E2, TX_LV_W2, TX_LV_S2, TX_LV_L2
    ); 
R_lv_3: router_LV generic map (DATA_WIDTH => 11, 
current_address =>3, Rxy_rst => 60, Cx_rst =>5, 
 NoC_size =>2)    PORT MAP (reset, clk, RX_LV_N3, RX_LV_E3, RX_LV_W3, RX_LV_S3, RX_LV_L3,
     credit_in_LV_N3, credit_in_LV_E3, credit_in_LV_W3, credit_in_LV_S3, credit_in_LV_L3,
    valid_in_LV_N3, valid_in_LV_E3, valid_in_LV_W3, valid_in_LV_S3, valid_in_LV_L3,
    valid_out_LV_N3, valid_out_LV_E3, valid_out_LV_W3, valid_out_LV_S3, valid_out_LV_L3,
    credit_out_LV_N3, credit_out_LV_E3, credit_out_LV_W3, credit_out_LV_S3, credit_out_LV_L3,
    TX_LV_N3, TX_LV_E3, TX_LV_W3, TX_LV_S3, TX_LV_L3
    ); 
---------------------------------------------------------------
-- binding the routers together
-- vertical ins/outs
-- connecting router: 0 to router: 2 and vice versa
RX_N_2<= TX_S_0;
RX_S_0<= TX_N_2;
-------------------
-- connecting router: 1 to router: 3 and vice versa
RX_N_3<= TX_S_1;
RX_S_1<= TX_N_3;
-------------------

-- horizontal ins/outs
-- connecting router: 0 to router: 1 and vice versa
RX_E_0 <= TX_W_1;
RX_W_1 <= TX_E_0;
-------------------
-- connecting router: 2 to router: 3 and vice versa
RX_E_2 <= TX_W_3;
RX_W_3 <= TX_E_2;
-------------------
---------------------------------------------------------------
-- binding the routers together
-- connecting router: 0 to router: 2 and vice versa
valid_in_N_2 <= valid_out_S_0;
valid_in_S_0 <= valid_out_N_2;
credit_in_S_0 <= credit_out_N_2;
credit_in_N_2 <= credit_out_S_0;
-------------------
-- connecting router: 1 to router: 3 and vice versa
valid_in_N_3 <= valid_out_S_1;
valid_in_S_1 <= valid_out_N_3;
credit_in_S_1 <= credit_out_N_3;
credit_in_N_3 <= credit_out_S_1;
-------------------

-- connecting router: 0 to router: 1 and vice versa
valid_in_E_0 <= valid_out_W_1;
valid_in_W_1 <= valid_out_E_0;
credit_in_W_1 <= credit_out_E_0;
credit_in_E_0 <= credit_out_W_1;
-------------------
-- connecting router: 2 to router: 3 and vice versa
valid_in_E_2 <= valid_out_W_3;
valid_in_W_3 <= valid_out_E_2;
credit_in_W_3 <= credit_out_E_2;
credit_in_E_2 <= credit_out_W_3;
-------------------
---------------------------------------------------------------
-- binding the routers together
-- vertical ins/outs
-- connecting router: 0 to router: 2 and vice versa
RX_LV_N2<= TX_LV_S0;
RX_LV_S0<= TX_LV_N2;
-------------------
-- connecting router: 1 to router: 3 and vice versa
RX_LV_N3<= TX_LV_S1;
RX_LV_S1<= TX_LV_N3;
-------------------

-- horizontal ins/outs
-- connecting router: 0 to router: 1 and vice versa
RX_LV_E0 <= TX_LV_W1;
RX_LV_W1 <= TX_LV_E0;
-------------------
-- connecting router: 2 to router: 3 and vice versa
RX_LV_E2 <= TX_LV_W3;
RX_LV_W3 <= TX_LV_E2;
-------------------
-- binding the LV routers together
-- connecting router: 0 to router: 2 and vice versa
valid_in_LV_N2 <= valid_out_LV_S0;
valid_in_LV_S0 <= valid_out_LV_N2;
credit_in_LV_S0 <= credit_out_LV_N2;
credit_in_LV_N2 <= credit_out_LV_S0;
-------------------
-- connecting router: 1 to router: 3 and vice versa
valid_in_LV_N3 <= valid_out_LV_S1;
valid_in_LV_S1 <= valid_out_LV_N3;
credit_in_LV_S1 <= credit_out_LV_N3;
credit_in_LV_N3 <= credit_out_LV_S1;
-------------------

-- connecting router: 0 to router: 1 and vice versa
valid_in_LV_E0 <= valid_out_LV_W1;
valid_in_LV_W1 <= valid_out_LV_E0;
credit_in_LV_W1 <= credit_out_LV_E0;
credit_in_LV_E0 <= credit_out_LV_W1;
-------------------
-- connecting router: 2 to router: 3 and vice versa
valid_in_LV_E2 <= valid_out_LV_W3;
valid_in_LV_W3 <= valid_out_LV_E2;
credit_in_LV_W3 <= credit_out_LV_E2;
credit_in_LV_E2 <= credit_out_LV_W3;
-------------------
end;

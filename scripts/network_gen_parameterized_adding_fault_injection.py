# Copyright (C) 2016 Siavoosh Payandeh Azad

import sys

# MAN:
# you should run this as
# python network_gen_parameterized.py [options]
#         -D [size]:  allows you to set the size of the network. it can be powers of two. 
#         -NI: adds NI to network
#         -P adds parity checker to the network



if '-D'  in sys.argv[1:]:
  network_dime = int(sys.argv[sys.argv.index('-D')+1])
else:
  network_dime = 4

if '-P'  in sys.argv[1:]: 
  add_parity = True
else:
  add_parity = False

if '-NI'  in sys.argv[1:]: 
  add_NI = True
else:
  add_NI = False

if '-FI'  in sys.argv[1:]: 
  add_FI = True
else:
  add_FI = False

def rxy_rst_calculator(node_id):
  rxy_rst = 60
  return rxy_rst

def cx_rst_calculator(node_id):
  cx_rst = 0
  node_x = i % network_dime
  node_y = i / network_dime
  c_n = 1
  c_e = 1
  c_w = 1
  c_s = 1 
  if node_y == 0 : 
    c_n = 0
  if node_y == network_dime-1 : 
    c_s = 0
  if node_x == 0:
    c_w = 0
  if node_x == network_dime-1: 
    c_e = 0
  return c_s*8+c_w*4+c_e*2+c_n

file_name= 'network'
if add_NI:
  file_name += '_NI'
if add_parity:
  file_name += '_parity'

noc_file = open(file_name+'_'+str(network_dime)+"x"+str(network_dime)+'.vhd', 'w')


noc_file.write("--Copyright (C) 2016 Siavoosh Payandeh Azad\n")
noc_file.write("------------------------------------------------------------\n")
noc_file.write("-- This file is automatically generated!\n")
noc_file.write("-- Here are the parameters:\n")
noc_file.write("-- \t network size x:"+str(network_dime)+"\n")
noc_file.write("-- \t network size y:"+str(network_dime)+"\n")
noc_file.write("------------------------------------------------------------\n\n")

noc_file.write("library ieee;\n")
noc_file.write("use ieee.std_logic_1164.all;\n")
noc_file.write("use IEEE.STD_LOGIC_ARITH.ALL;\n")
noc_file.write("use IEEE.STD_LOGIC_UNSIGNED.ALL;\n\n")
 
noc_file.write("entity network_"+str(network_dime)+"x"+str(network_dime)+" is\n")
noc_file.write(" generic (DATA_WIDTH: integer := 32);\n")
noc_file.write("port (reset: in  std_logic; \n")
noc_file.write("\tclk: in  std_logic; \n")
for i in range(network_dime*network_dime):
  noc_file.write("\t--------------\n")
  noc_file.write("\tRX_L_"+str(i)+": in std_logic_vector (DATA_WIDTH-1 downto 0);\n")
  noc_file.write("\tRTS_L_"+str(i)+", CTS_L_"+str(i)+": out std_logic;\n")
  noc_file.write("\tDRTS_L_"+str(i)+", DCTS_L_"+str(i)+": in std_logic;\n")
  if i == network_dime*network_dime-1:
    noc_file.write("\tTX_L_"+str(i)+": out std_logic_vector (DATA_WIDTH-1 downto 0)\n")
  else:
    noc_file.write("\tTX_L_"+str(i)+": out std_logic_vector (DATA_WIDTH-1 downto 0);\n")
noc_file.write("            ); \n")
noc_file.write("end network_"+str(network_dime)+"x"+str(network_dime)+"; \n")


noc_file.write("\n\n")
noc_file.write("architecture behavior of network_"+str(network_dime)+"x"+str(network_dime)+" is\n\n")
noc_file.write("-- Declaring router component\n")
if add_parity:
  noc_file.write("component router_parity is\n")
else:
  noc_file.write("component router is\n")
noc_file.write(" generic (\n")
noc_file.write("        DATA_WIDTH: integer := 32;\n")
noc_file.write("        current_address : integer := 5;\n")
noc_file.write("        Rxy_rst : integer := 60;\n")
noc_file.write("        Cx_rst : integer := 15;\n")
noc_file.write("        NoC_size : integer := 4\n")
noc_file.write("    );\n")
noc_file.write("    port (\n")
noc_file.write("    reset, clk: in std_logic;\n")
noc_file.write("    DCTS_N, DCTS_E, DCTS_w, DCTS_S, DCTS_L: in std_logic;\n")
noc_file.write("    DRTS_N, DRTS_E, DRTS_W, DRTS_S, DRTS_L: in std_logic;\n")
noc_file.write("    RX_N, RX_E, RX_W, RX_S, RX_L : in std_logic_vector (DATA_WIDTH-1 downto 0);\n")
noc_file.write("    RTS_N, RTS_E, RTS_W, RTS_S, RTS_L: out std_logic;\n")
noc_file.write("    CTS_N, CTS_E, CTS_w, CTS_S, CTS_L: out std_logic;\n")
if add_parity:
  noc_file.write("    TX_N, TX_E, TX_W, TX_S, TX_L: out std_logic_vector (DATA_WIDTH-1 downto 0);\n")
  noc_file.write("    fault_out_N, fault_out_E, fault_out_W, fault_out_S, fault_out_L: out std_logic);\n")
else:
  noc_file.write("    TX_N, TX_E, TX_W, TX_S, TX_L: out std_logic_vector (DATA_WIDTH-1 downto 0));\n")
noc_file.write("end component; \n")
noc_file.write("\n\n")

if add_NI:
  noc_file.write("component NI is\n")
  noc_file.write("    generic (\n")
  noc_file.write("        DATA_WIDTH: integer := 32\n")
  noc_file.write("    );\n")
  noc_file.write("    port (  reset: in  std_logic;\n")
  noc_file.write("            clk: in  std_logic;\n")
  noc_file.write("            ---------------------------------------\n")
  noc_file.write("            RX1: in std_logic_vector(DATA_WIDTH-1 downto 0); \n")
  noc_file.write("            TX1: out std_logic_vector(DATA_WIDTH-1 downto 0); \n")
  noc_file.write("            DRTS1, DCTS1: in  std_logic;\n")
  noc_file.write("            RTS1,CTS1: out  std_logic;\n")
  noc_file.write("            ---------------------------------------\n")
  noc_file.write("            RX2: in std_logic_vector(DATA_WIDTH-1 downto 0); \n")
  noc_file.write("            TX2: out std_logic_vector(DATA_WIDTH-1 downto 0); \n")
  noc_file.write("            DRTS2, DCTS2: in  std_logic;\n")
  noc_file.write("            RTS2,CTS2: out  std_logic\n")
  noc_file.write("    );\n")
  noc_file.write("end component;\n")
  noc_file.write("\n")

if add_FI:
  noc_file.write("component fault_injector is \n")
  noc_file.write("  generic(DATA_WIDTH : integer := 32);\n")
  noc_file.write("  port(\n")
  noc_file.write("    data_in: in std_logic_vector (DATA_WIDTH-1 downto 0);\n")
  noc_file.write("    address: in std_logic_vector(integer(ceil(log2(real(DATA_WIDTH))))-1 downto 0);\n")
  noc_file.write("    sta_0: in std_logic;\n")
  noc_file.write("    sta_1: in std_logic;\n")
  noc_file.write("    data_out: out std_logic_vector (DATA_WIDTH-1 downto 0)\n")
  noc_file.write("    );\n")
  noc_file.write("end component;\n")


noc_file.write("-- generating bulk signals. not all of them are used in the design...\n")
if add_NI:
  for i in range(0, network_dime*network_dime):
      noc_file.write("\tsignal RX_L_R_"+str(i)+", TX_L_R_"+str(i)+" : std_logic_vector (DATA_WIDTH-1 downto 0);\n")
      noc_file.write("\tsignal RTS_L_R_"+str(i)+", DRTS_L_R_"+str(i)+", CTS_L_R_"+str(i)+", DCTS_L_R_"+str(i)+": std_logic;\n")

for i in range(0, network_dime*network_dime):
    noc_file.write("\tsignal DCTS_N_"+str(i)+", DCTS_E_"+str(i)+", DCTS_w_"+str(i)+", DCTS_S_"+str(i) +": std_logic;\n")
noc_file.write("\n")
for i in range(0, network_dime*network_dime):
    noc_file.write("\tsignal DRTS_N_"+str(i)+", DRTS_E_"+str(i)+", DRTS_W_"+str(i)+", DRTS_S_"+str(i) + ": std_logic;\n")
noc_file.write("\n")
for i in range(0, network_dime*network_dime):
    noc_file.write("\tsignal RX_N_"+str(i)+", RX_E_"+str(i)+", RX_W_"+str(i)+", RX_S_"+str(i) +
      " : std_logic_vector (DATA_WIDTH-1 downto 0);\n")
noc_file.write("\n")
for i in range(0, network_dime*network_dime):
    noc_file.write("\tsignal CTS_N_"+str(i)+", CTS_E_"+str(i)+", CTS_w_"+str(i)+", CTS_S_"+str(i) + ": std_logic;\n")
noc_file.write("\n")
for i in range(0, network_dime*network_dime):
    noc_file.write("\tsignal RTS_N_"+str(i)+", RTS_E_"+str(i)+", RTS_W_"+str(i)+", RTS_S_"+str(i) + ": std_logic;\n")
noc_file.write("\n")
for i in range(0, network_dime*network_dime):
    noc_file.write("\tsignal TX_N_"+str(i)+", TX_E_"+str(i)+", TX_W_"+str(i)+", TX_S_"+str(i)+
                   " : std_logic_vector (DATA_WIDTH-1 downto 0);\n")
noc_file.write("\n")
if add_parity:
  for i in range(0, network_dime*network_dime):
    noc_file.write("\tsignal fault_out_N_"+str(i)+", fault_out_E_"+str(i)+", fault_out_W_"+str(i) +
                   ", fault_out_S_"+str(i)+", fault_out_L_"+str(i)+": std_logic;\n")

noc_file.write("begin\n\n")

noc_file.write("\n\n")
noc_file.write("--        organizaiton of the network:\n")
noc_file.write("--     x --------------->\n")
for j in range(0, network_dime):
    if j == 0:  
      noc_file.write("--  y  ")
    else:
      noc_file.write("--  |  ")
    for i in range(0, network_dime):
      noc_file.write("       ----")
    noc_file.write("\n")
    noc_file.write("--  |       ")
    for i in range(0, network_dime):
      if i != network_dime-1:
        if (i+network_dime*j)>=10:
          noc_file.write(" | "+str(i+network_dime*j)+" | ---")
        else:
          noc_file.write(" | "+str(i+network_dime*j)+"  | ---")
      else:
        if (i+network_dime*j)>=10:
          noc_file.write(" | "+str(i+network_dime*j)+" |")
        else:
          noc_file.write(" | "+str(i+network_dime*j)+"  |")

    noc_file.write("\n")
    if j == network_dime-1:
      noc_file.write("--  v  ")
    else:
      noc_file.write("--  |  ")
    for i in range(0, network_dime):
      if add_NI:
        noc_file.write("      /----")
      else:
        noc_file.write("       ----")
    if add_NI:
      if j == network_dime-1:
        noc_file.write("\n--   ")
        for i in range(0, network_dime):
          noc_file.write("      NI   ")
      else:
        noc_file.write("\n--  |")
        for i in range(0, network_dime):
          noc_file.write("      NI  |")
    else:
      if j == network_dime-1:
        noc_file.write("\n--   ")
        for i in range(0, network_dime):
          noc_file.write("           ")
      else:
        noc_file.write("\n--  |")
        for i in range(0, network_dime):
          noc_file.write("          |")

    noc_file.write("\n")
noc_file.write("\n")
noc_file.write("-- instantiating the routers\n")
for i in range(0, network_dime*network_dime):
    if add_parity:
      noc_file.write("R_"+str(i)+": router_parity generic map (DATA_WIDTH  => DATA_WIDTH, ")
    else:
      noc_file.write("R_"+str(i)+": router generic map (DATA_WIDTH  => DATA_WIDTH, ")

    noc_file.write("current_address=>"+str(i)+", Rxy_rst => "+str(rxy_rst_calculator(i))+", " + 
                   "Cx_rst => "+str(cx_rst_calculator(i))+", NoC_size=>"+str(network_dime)+")\n")
    noc_file.write("PORT MAP (reset, clk, \n")
    if add_NI:
      noc_file.write("\tDCTS_N_"+str(i)+", DCTS_E_"+str(i)+", DCTS_W_"+str(i)+", DCTS_S_"+str(i)+", DCTS_L_R_"+str(i)+",\n")
      noc_file.write("\tDRTS_N_"+str(i)+", DRTS_E_"+str(i)+", DRTS_W_"+str(i)+", DRTS_S_"+str(i)+", DRTS_L_R_"+str(i)+",\n")
      noc_file.write("\tRX_N_"+str(i)+", RX_E_"+str(i)+", RX_W_"+str(i)+", RX_S_"+str(i)+", RX_L_R_"+str(i)+",\n")
      noc_file.write("\tRTS_N_"+str(i)+", RTS_E_"+str(i)+", RTS_W_"+str(i)+", RTS_S_"+str(i)+", RTS_L_R_"+str(i)+",\n")
      noc_file.write("\tCTS_N_"+str(i)+", CTS_E_"+str(i)+", CTS_w_"+str(i)+", CTS_S_"+str(i)+", CTS_L_R_"+str(i)+",\n")
      noc_file.write("\tTX_N_"+str(i)+", TX_E_"+str(i)+", TX_W_"+str(i)+", TX_S_"+str(i)+", TX_L_R_"+str(i))
      
    else:
      noc_file.write("\tDCTS_N_"+str(i)+", DCTS_E_"+str(i)+", DCTS_W_"+str(i)+", DCTS_S_"+str(i)+", DCTS_L_"+str(i)+",\n")
      noc_file.write("\tDRTS_N_"+str(i)+", DRTS_E_"+str(i)+", DRTS_W_"+str(i)+", DRTS_S_"+str(i)+", DRTS_L_"+str(i)+",\n")
      noc_file.write("\tRX_N_"+str(i)+", RX_E_"+str(i)+", RX_W_"+str(i)+", RX_S_"+str(i)+", RX_L_"+str(i)+",\n")
      noc_file.write("\tRTS_N_"+str(i)+", RTS_E_"+str(i)+", RTS_W_"+str(i)+", RTS_S_"+str(i)+", RTS_L_"+str(i)+",\n")
      noc_file.write("\tCTS_N_"+str(i)+", CTS_E_"+str(i)+", CTS_w_"+str(i)+", CTS_S_"+str(i)+", CTS_L_"+str(i)+",\n")
      noc_file.write("\tTX_N_"+str(i)+", TX_E_"+str(i)+", TX_W_"+str(i)+", TX_S_"+str(i)+", TX_L_"+str(i))

    if add_parity:
      noc_file.write(",\n")
      noc_file.write("\tfault_out_N_"+str(i)+", fault_out_E_"+str(i)+", fault_out_W_"+str(i)+", fault_out_S_"+str(i)+", fault_out_L_"+str(i)+");\n\n")
    else:
      noc_file.write("); \n\n")

noc_file.write("\n")

if add_NI:
  noc_file.write("-- instantiating the NI\n")
  for i in range(0, network_dime*network_dime):
    noc_file.write("NI_"+str(i)+":  NI generic map (DATA_WIDTH  => DATA_WIDTH)\n")
    noc_file.write("port map(reset=> reset, clk=>clk,\n")
    noc_file.write("         RX1=> TX_L_R_"+str(i)+",  \n")
    noc_file.write("         TX1=> TX_L_"+str(i)+",  \n") 
    noc_file.write("         DRTS1=> RTS_L_R_"+str(i)+" ,   \n")
    noc_file.write("         DCTS1=> DCTS_L_"+str(i)+",  \n")
    noc_file.write("         RTS1=> RTS_L_"+str(i)+",  \n")
    noc_file.write("         CTS1=>  DCTS_L_R_"+str(i)+",  \n")
    noc_file.write("        ----------------------\n")
    noc_file.write("         RX2=> RX_L_"+str(i)+",  \n")
    noc_file.write("         TX2=> RX_L_R_"+str(i)+"  ,\n")   
    noc_file.write("         DRTS2=> DRTS_L_"+str(i)+",\n")
    noc_file.write("         DCTS2=> CTS_L_R_"+str(i)+" ,\n")  
    noc_file.write("         RTS2=>  DRTS_L_R_"+str(i)+",\n")
    noc_file.write("         CTS2=>  CTS_L_"+str(i)+" \n")
    noc_file.write("  );\n")
noc_file.write("---------------------------------------------------------------\n")

noc_file.write("-- binding the routers together\n")
noc_file.write("-- vertical ins/outs\n")
for i in range(0, network_dime*network_dime):
  node_x = i % network_dime
  node_y = i / network_dime
  if node_y != network_dime-1:
      noc_file.write("-- connecting router: "+str(i)+ " to router: "+str(i+network_dime)+" and vice versa\n")
      noc_file.write("RX_N_"+str(i+network_dime)+"<= TX_S_"+str(i)+";\n")
      noc_file.write("RX_S_"+str(i)+"<= TX_N_"+str(i+network_dime)+";\n")

      noc_file.write("DRTS_N_"+str(i+network_dime)+" <= RTS_S_"+str(i)+";\n")
      noc_file.write("DCTS_S_"+str(i)+" <= CTS_N_"+str(i+network_dime)+";\n")

      noc_file.write("DRTS_S_"+str(i)+" <= RTS_N_"+str(i+network_dime)+";\n")
      noc_file.write("DCTS_N_"+str(i+network_dime)+" <= CTS_S_"+str(i)+";\n")
      noc_file.write("-------------------\n") 
noc_file.write("\n")      
noc_file.write("-- horizontal ins/outs\n")
for i in range(0, network_dime*network_dime):
  node_x = i % network_dime
  node_y = i / network_dime
  if node_x != network_dime -1 :
      noc_file.write("-- connecting router: "+str(i)+ " to router: "+str(i+1)+" and vice versa\n")
      noc_file.write("RX_E_"+str(i)+" <= TX_W_"+str(i+1)+";\n")
      noc_file.write("RX_W_"+str(i+1)+" <= TX_E_"+str(i)+";\n")

      noc_file.write("DRTS_E_"+str(i)+" <= RTS_W_"+str(i+1)+";\n")
      noc_file.write("DCTS_W_"+str(i+1)+" <= CTS_E_"+str(i)+";\n")

      noc_file.write("DRTS_W_"+str(i+1)+" <= RTS_E_"+str(i)+";\n")
      noc_file.write("DCTS_E_"+str(i)+" <= CTS_W_"+str(i+1)+";\n")
      noc_file.write("-------------------\n") 
noc_file.write("end;\n")

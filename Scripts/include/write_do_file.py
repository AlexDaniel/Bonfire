
import file_lists
from Scripts.include.package import *

def write_do_file(program_argv, net_file_name, net_tb_file_name, wave_do_file_name, logging):
    """
    Generates a simulate.do file for running Modelsim.
        program_argv:       program arguments
        net_file_name:      file name for the generated network
        net_tb_file_name:   file name for the generated network
        wave_do_file_name:  file name for the generated wave.do file
        logging:            logging file
    """

    logging.info("Generating simulation.do")
    if program_argv['credit_based_FC']:
        flow_control_type = CREDIT_BASED_SUFFIX
    else:
        flow_control_type = HANDSHAKING_SUFFIX

    do_file = open(SIMUL_DIR + "/" + SIMUL_DO_SCRIPT, 'w')

    do_file.write("#########################################\n")
    do_file.write("# Copyright (C) 2016 Project Bonfire    #\n")
    do_file.write("#                                       #\n")
    do_file.write("# This file is automatically generated! #\n")
    do_file.write("#             DO NOT EDIT!              #\n")
    do_file.write("#########################################\n\n")

    do_file.write("vlib work\n\n")

    do_file.write("# Include files and compile them\n")


    ##### Simulation files #####

    # Credit based flow control
    if program_argv['credit_based_FC']:
        if program_argv['add_checkers']:
            # With checkers
            # Currently being tested (but still a TODO)
            for file in file_lists.CB_Allocator_with_checkers_files:
                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type + CHECKERS_DIR \
                    + "/Allocator_with_checkers/"+file+"\"\n")
      
            for file in file_lists.CB_FIFO_one_hot_CB_PD_FC_with_checkers_files:    
                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type + CHECKERS_DIR \
                    + "/FIFO_one_hot_credit_based_packet_drop_classifier_support_with_checkers/"+file+"\"\n")

            for file in file_lists.CB_LBDR_PD_with_checkers_files:
                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type + CHECKERS_DIR \
                    + "/LBDR_packet_drop_with_checkers/"+file+"\"\n")
 
            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/xbar.vhd\"\n")

            # print_msg(MSG_ERROR, "Checkers are not yet implemented for credit based flow control")
            # do_file.close()
            # sys.exit(1)

        else:
            # Without checkers
            
            if (program_argv['packet_drop'] and program_argv['add_FC']):
                List_of_files = file_lists.credit_based_files_PD_FC
            elif program_argv['packet_drop'] and not program_argv['add_FC']:
                List_of_files = file_lists.credit_based_files_PD
            elif program_argv['packet_saving']:
                List_of_files = file_lists.credit_based_files_PS
            elif program_argv['add_LV']:
                List_of_files = file_lists.credit_based_files_LV
            else:
                List_of_files = file_lists.credit_based_files

            for file in List_of_files:
                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                    + "/RTL/"+file+"\"\n")

            if program_argv['add_LV']:
                for file in file_lists.LV_common_files:
                        do_file.write("vcom \"" + FAULT_MANAGEMENT_RTL_DIR + "/Fault_management_network/"+file+"\"\n")

                if program_argv['lv_port'] == 4:
                    
                    for file in file_lists.LV_files_4:
                        do_file.write("vcom \"" + FAULT_MANAGEMENT_RTL_DIR + "/Fault_management_network/"+ file + "\"\n")

                elif program_argv['lv_port'] == 2:
                    for file in file_lists.LV_files_2:
                        do_file.write("vcom \"" + FAULT_MANAGEMENT_RTL_DIR + "/Fault_management_network/LW_2_port/"\
                        + file + "\"\n")

                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                    + "/RTL/FIFO_one_hot_credit_based_packet_drop_classifier_support.vhd\"\n")


        # Add a network interface
        if program_argv['add_NI'] != -1:
            for file in file_lists.PE_files:
                do_file.write("vcom \"" + PROJECT_ROOT + "/RTL/Processor_NI/"+file+"\"\n")

        # Add parity checking
        if program_argv['add_parity']:
            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/ParityChecker_packet_detector.vhd\"\n")

        # all the routers
        if program_argv['add_parity'] and not program_argv['add_checkers']:
            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/Router_32_bit_credit_based_parity.vhd\"\n")

        elif program_argv['add_LV'] and program_argv['packet_drop'] and program_argv['add_FC'] and not program_argv['add_checkers']:
            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/Router_32_bit_credit_based_packet_drop_LV_compatible.vhd\"\n")

        elif program_argv['add_LV'] and not program_argv['packet_drop'] and program_argv['add_FC'] and not program_argv['add_checkers']:
            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/Router_32_bit_credit_based_packet_drop_LV_compatible.vhd\"\n")

        elif not program_argv['add_LV'] and program_argv['packet_drop'] and program_argv['add_FC'] and not program_argv['add_checkers']:
            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/Router_32_bit_credit_based_packet_drop_classifier.vhd\"\n")

        elif not program_argv['add_LV'] and program_argv['add_checkers'] and program_argv['packet_drop'] and program_argv['add_FC']:
            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/Router_32_bit_credit_based_packet_drop_classifier_with_full_set_of_checkers.vhd\"\n")

        else:
            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/Router_32_bit_credit_based.vhd\"\n")

        # End of credit based flow control

    # Handshaking based flow control
    else:
        # With checkers
        if program_argv['add_checkers']:
            for file in file_lists.HS_Arbiter_one_hot_with_checkers:
                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type + CHECKERS_DIR \
                    + "/Arbiter_one_hot_with_checkers/"+file+"\"\n")

            for file in file_lists.HS_Arbiter_one_hot_with_checkers:
                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type + CHECKERS_DIR \
                    + "/FIFO_one_hot_with_checkers/"+file+"\"\n")

            for file in file_lists.HS_LBDR_with_checkers:
                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type + CHECKERS_DIR \
                    + "/LBDR_with_checkers/"+file+"\"\n")

            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/xbar.vhd\"\n")

        else:
            # No checkers
            for file in file_lists.handshaking_files:
                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                    + "/RTL/"+file+"\"\n")


        # Add a network interface
        if program_argv['add_NI'] != -1:
            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/NI.vhd\"\n")
            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/NI_channel.vhd\"\n")

        # Add parity checking
        if program_argv['add_parity']:
            do_file.write("vcom \"" + FAULT_MANAGEMENT_RTL_DIR \
                + "/Error_Detection_Correction/ParityChecker.vhd\"\n")

            do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                + "/RTL/Router_32_bit_handshaking_parity.vhd\"\n")
        else:
            if program_argv['add_checkers']:
                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                    + "/RTL/Router_32_bit_handshaking_with_full_set_of_checkers.vhd\"\n")
            else:
                do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
                    + "/RTL/Router_32_bit_handshaking.vhd\"\n")

        # End of handshaking based flow control

    # Add fault injectors
    if program_argv['add_FI']:
        do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
            + "/RTL/Fault_injector.vhd\"\n")

    # Include file for the testbench
    do_file.write("vcom \"" + TEST_DIR + "/" + flow_control_type \
        + "/TB_Package_32_bit_" + flow_control_type + ".vhd\"\n")

    if program_argv['trace'] and flow_control_type == "credit_based":
        do_file.write("vcom \"" + ROUTER_RTL_DIR + "/" + flow_control_type \
        + "/RTL/flit_tracker.vhd\"\n")

    # Generated network files
    do_file.write("vcom \"" +  net_file_name + "\"\n")
    do_file.write("vcom \"" +  net_tb_file_name + "\"\n\n")

    #### Simulation control ####

    do_file.write("# Start the simulation\n")
    do_file.write("vsim work.tb_network_" \
        + str(program_argv['network_dime']) + "x" + str(program_argv['network_dime']) + "\n\n")

    do_file.write("# Draw waves\n")
    do_file.write("do " + wave_do_file_name + "\n")

    do_file.write("# Run the simulation\n")
    if program_argv['sim'] == -1 and program_argv['end'] == -1:
        do_file.write("run 15000 ns\n")

    elif program_argv['sim'] != -1 and program_argv['end'] == -1:

        do_file.write("run " + str(int(ceil(program_argv['sim'] * 1.5))) + " ns\n")

    else:
        do_file.write("run " + str(program_argv['end']) + " ns\n")

    if program_argv['lat']:
        do_file.write("\n# Exit Modelsim after simulation\n")
        do_file.write("exit\n")
    do_file.close()
    logging.info("finished writing do file...")

    return None
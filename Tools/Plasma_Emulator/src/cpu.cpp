/*--------------------------------------------------------------------
 * TITLE: Text Based User Interface
 * AUTHOR: Karl Janson
 * DATE CREATED: 14.12.16
 * FILENAME: text_ui.cpp
 * PROJECT: Bonfire NoC CPU Emulator
 * COPYRIGHT: Software placed into the public domain by the author.
 *    Software 'as is' without warranty.  Author liable for nothing.
 * DESCRIPTION:
 *    Text user interface
 *--------------------------------------------------------------------*/

#include <iostream>
#include "message.h"
#include "common.h"
#include "cpu.h"
#include "memory.h"
#include "memory_ctrl.h"

using namespace std;

Cpu::Cpu()
{
    exit_signal = false;
}

void Cpu::execute()
{
}

void Cpu::run()
{

    Memory ram(1024, MEM_TYPE_RAM);

    Memory reg_bank(32, MEM_TYPE_REG_BANK);

    //Message<Type_cmd> message;

    while (!exit_signal)
    {

        /*if (command_lock == true)
        {
            command_mutex.lock();
            message = command_queue.front();
            command_queue.pop();
            command_mutex.unlock();

            cout << message.param << endl;

            command_lock = false;

            switch (message.type)
            {
                case Type_cmd::cmd_exit:
                    exit_signal = true;
                    break;
                case Type_cmd::cmd_asm:
                    cout << "ASM cmd: " << message.param << endl;
                    break;
                default:
                    cout << "def" << endl;
                    break;
            }
        }*/

    }
    cout << "cpu out" << endl;
}

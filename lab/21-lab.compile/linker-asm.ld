SECTIONS
{
    . = 0x10000;
    .text : { *(.text) }
    .data : { *(.data) }
}

ENTRY (_start)

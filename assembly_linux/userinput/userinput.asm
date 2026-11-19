; --------------------------------------------------------------------
;
; userinput.asm
;
; Author:        Allan Smart
; Date Created:  19/11/2026
; Date Modified: 19/11/2026
;
; Description:
; The program does the following:
;           - Prints "Allan's Program"
;           - Asks the user to enter their name
;           - Then prints Welcome and the user's name
;
; Makefile:
; Code is compiled by a makefile.
;
; This is all part of learning Assembly languuage in Linux x86-64
;
; --------------------------------------------------------------------

section .data

    ; 1. Opening message
    opening_message         db "Allan's Program", 10
    opening_message_len     equ $ - opening_message

    ; 2. Prompting user to enter name
    enter_name              db "Please enter your name: "
    enter_name_len          equ $ - enter_name

    ; 5. Display message to screen what the user entered
    member_entered          db "Welcome: "
    member_entered_len      equ $ - member_entered

section .bss

    ;4 Buffer for name input
    name_buffer             resb 156

section .text

    global _start


_start:

    ; 1. Display opening message to the screen
    mov eax, 1
    mov edi, 1
    mov rsi, opening_message
    mov edx, opening_message_len
    syscall

    ; 2. Ask user to enter their name
    mov eax, 1
    mov edi, 1
    mov rsi, enter_name
    mov edx, enter_name_len
    syscall

    ; 3. Take input for user name
    mov eax, 0
    mov edi, 0
    mov rsi, name_buffer
    mov edx, 156
    syscall
    mov r8, rax

    ; 4 Displaying to screen what the user enterd
    mov eax, 1
    mov edi, 1
    mov rsi, member_entered
    mov edx, member_entered_len
    syscall

    ; Displaying user's name
    mov eax, 1
    mov edi, 1
    mov rsi, name_buffer
    mov rdx, r8
    syscall

    ; 5. Exit program cleanly
    mov eax, 60
    mov edi, 0
    syscall


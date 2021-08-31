# Short WriteUp - SAW

This challenge was a cool windows based challenge, I personally learnt a lot of thing from this like SEH/Try Catch Handling, certain cool anti-debugging tricks
and concepts of process hollowing and a cool anti analysis trick called Opaque Predicates. There was a lot of new stuff, sadly I wasnt able to make it in time for the CTF
But I did manage to solve it after the CTF.

So there were two stages,

1. All the anti debugging stuff and the process hollowing
2. The process gets created and the anti analysis trick with the flag check function

---

The Try Catch Handling was really cool to learn about, so apparantly when an exception occurs the SEH routine will transfer the control
over to the handling routine. This is given in the SEH strucutre which has the address to the handler function.

So in total there were 3 Exceptions to be handled, 2 `int3` and 1 `int 2d` which can be handled in most debuggers like IDA, Windbg by placing breakpoints at the 
right place and continuing.

Then there were two other specific anti debugging trick implemented which is specific only for windows, #windows-magic XD. Both of them used the PEB structure
to check if a debugger is currently attached to the process, it specifically checks two flags,

- BeingDebug : Which will be set to 1 if there is a debugger present 
- NtGlobalFlag : Which will be set to 0x70 if there is a debugger present

---

Once this is passed a counter is responsible to check if any of the debugger checks were triggered, if not it stays to 0.

There is a dynamic function resolving as well, which is done over here,
```asm
.text:0005D562 mov     eax, [ebp+allocatedRegion]
.text:0005D568 mov     [ebp+hProcess], eax
.text:0005D56B mov     eax, [ebp+arg_4]
.text:0005D56E sub     eax, 790A0632h
.text:0005D573 mov     [ebp+unkVar], eax
.text:0005D576 mov     eax, [ebp+arg_4]
.text:0005D579 sub     eax, 13F680AEh
.text:0005D57E mov     [ebp+var_44], eax
.text:0005D581 mov     eax, [ebp+arg_4]
.text:0005D584 sub     eax, 1BB7CA0Bh
.text:0005D589 mov     [ebp+var_50], eax
.text:0005D58C mov     eax, [ebp+arg_4]
.text:0005D58F sub     eax, 351575B4h
.text:0005D594 mov     [ebp+var_5C], eax
.text:0005D597 mov     eax, [ebp+arg_4]
.text:0005D59A add     eax, 441432BDh
.text:0005D59F mov     [ebp+var_68], eax
.text:0005D5A2 mov     eax, [ebp+arg_4]
.text:0005D5A5 add     eax, 6494BD71h
.text:0005D5AA mov     [ebp+var_74], eax
.text:0005D5AD mov     eax, [ebp+arg_4]
.text:0005D5B0 sub     eax, 598373E6h
.text:0005D5B5 mov     [ebp+var_80], eax
.text:0005D5B8 mov     eax, [ebp+arg_4]
.text:0005D5BB sub     eax, 0E68EE71h
.text:0005D5C0 mov     [ebp+var_8C], eax
.text:0005D5C6 mov     eax, [ebp+arg_4]
.text:0005D5C9 sub     eax, 6AB3817Dh
.text:0005D5CE mov     [ebp+var_98], eax
.text:0005D5D4 mov     eax, [ebp+arg_4]
.text:0005D5D7 sub     eax, 77EF5EA9h
.text:0005D5DC mov     [ebp+var_A4], eax
.text:0005D5E2 mov     eax, [ebp+unkVar]
.text:0005D5E5 push    eax             ; int
.text:0005D5E6 push    offset aKernel32Dll_0 ; "kernel32.dll"
.text:0005D5EB call    getFuncUsingHash
```

---

The function `getFuncUsingHash` is responsible for getting the right function by calculating if the hash is present in the loaded dll, 
```c
int GetFuncHash(char *funcName){
    int hash = 0;
    int tmp1 = 0, tmp2 = 0;
    for(int i=0;i < strlen(funcName); i++){
        tmp1 = hash << 6;
        tmp1 = tmp1 + funcName[i];
        
        tmp2 = hash << 0x10;
        
        tmp1 = tmp1 + tmp2;
        tmp1 = tmp1 - hash;
        
        hash = tmp1;
    }
    return hash;
}
```

Here are the right functions that was needed,
```
kernel32.dll
Func: CreateProcessA  Hash: 0x86f5f9ce
Func: GetThreadContext  Hash: 0xf197118f
Func: ReadProcessMemory  Hash: 0xa67c8c1a
Func: SetThreadContext  Hash: 0x954c7e83

ntdll.dll
Func: NtClose  Hash: 0xec097f52
Func: NtUnmapViewOfSection  Hash: 0xcaea8a4c
Func: NtWaitForSingleObject  Hash: 0xe44835f5
```

---

Since we get the right function, the second process is spawned and constructed at next, we can breakpoint at `NtWaitForSingleObject` and then attach a debugger to the 
new process.

Debugging the newly created process will allow us to reach the flag check function, where the anti analysis trick was implemented. 
You can check out about opaque predicates, in many malware reports.

To bypass it, I just extracted all the bytes for that function, and used `capstone` to disassemble the opcodes and parsed the bytes to get the right bits into
its place.

The script is attached here: (https://github.com/AmunRha/WriteUps/blob/main/FWORDCTF21/SAW/solve.py)[solve.py]


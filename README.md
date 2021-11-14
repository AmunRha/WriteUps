# CTF Write ups

This repo contains the CTF scripts and probably some short write ups for challenges that I have solved during or after a CTF.

Check out [https://amunrha.github.io](https://amunrha.github.io) for full write ups for certain challenges.

---

## CTF List

<details>
  <summary>FWORD CTF 2021</summary>
  <ul>
    <li>
    <a href="https://github.com/AmunRha/WriteUps/blob/main/FWORDCTF21/Omen/solve_z3.py">Omen</a><br>
      Windows based challenge. The challenge includes process injection, and shellcode. Stepping through instructions should land us to the flag checker
      eventually, and then its just simple equations which can be solved using z3.<br>
      Tags: [#z3, #windows]
    </li>
  </ul>
  
  <ul>
    <li>
    <a href="https://github.com/AmunRha/WriteUps/tree/main/FWORDCTF21/SAW">SAW</a><br>
      Windows based challenge. The challenge included concepts of process hollowing, multiple anti-debugging checks, run time function resolving and implementaion 
      of opaque predicates to do anti analysis. Final bitwise check can be extracted and parsed using capstone.<br>
      Note: Solved after CTF<br>
      Tags: [#anti-debugging, #opaque-predicates, #windows]
    </li>   
  </ul>
</details>

<details>
  <summary>ALLES! CTF 2021</summary>
  <ul>
    <li>
    <a href="https://github.com/AmunRha/WriteUps/tree/main/ALLESCTF21/Monstrosity">Monstrosity</a><br>
      DotNet challenge. The challenge was pretty straight forward and yet tricky, the challenge implemented a JIT hooking technique to change pieces of code during             runtime, debugging was my way of solving this challenge, but statically analysing the challenge should also work. The core of the challenge was to recreate the           maze and supply the right inputs (which changes during runtime) to the binary, which makes the flag.<br>
      Tags: [#DotNet, #JIT_Hook, #maze]
    </li>
  </ul>
</details>

<details>
  <summary>DOME CTF 2021</summary>
  <ul>
    <li>
    <a href="https://github.com/AmunRha/WriteUps/tree/main/ALLESCTF21/Monstrosity">Assemble It!</a><br>
      This challenge was based on python disassembly, the solution would be to manually decompile and understand the program. Then writing a decrypt function would get the flag.<br>
      Tags: [#python, #bytecode]
    </li>
  </ul>
  
  <ul>
    <li>
    <a href="https://github.com/AmunRha/WriteUps/tree/main/DOMECTF21/Dome_Code">Dome Code</a><br>
      The challenge file given was a picture, and apparantly the clue given gave the idea of solving it using the hex codes of colors.<br>
      Tags: [#misc]
    </li>
  </ul>
  
  <ul>
    <li>
    <a href="https://github.com/AmunRha/WriteUps/tree/main/DOMECTF21/Bing">Bing</a><br>
      This challenge was mostly based on substituting with the right things.<br>
      Tags: [#misc]
    </li>
  </ul>
</details>



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
    <a href="">SAW</a><br>
      Windows based challenge. The challenge included concepts of process hollowing, multiple anti-debugging checks, run time function resolving and implementaion 
      of opaque predicates to do anti analysis. Final bitwise check can be extracted and parsed using capstone.<br>
      Note: Solved after CTF<br>
      Tags: [#anti-debugging, #opaque-predicates, #windows]
    </li>   
  </ul>
</details>



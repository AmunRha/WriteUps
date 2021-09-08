# Short WriteUp - Monstrosity

This challenge implemented JIT Hook to change certain functions during runtime, and several other functions which were responsible for verifying/traversing the maze

The main binary loads and runs functions from `Maze.dll`,
```c#
	internal unsafe static int main(string[] args)
	{
		uint num = 0;
		void* value = <Module>.CUtility.GetByteResourceContent((sbyte*)(&<Module>.??_C@_06JECEJHIJ@loader@), &num);
		byte[] array = new byte[num];
		Marshal.Copy((IntPtr)value, array, 0, num);
		Assembly assembly = Assembly.Load(array);
		<Module>.VirtualAlloc(null, num, 12288, 64);
		<Module>.CreateThread(null, 0UL, <Module>.__unep@?BackgroundInitialize@@$$FYAKPEAX@Z, null, 0, null);
		Thread.Sleep(1000);
		object[] args2 = new object[]
		{
			10,
			10
		};
		object obj = Activator.CreateInstance(assembly.GetModules()[0].GetType("Maze.Maze"), args2);
		object[] parameters = new object[]
		{
			obj
		};
		assembly.GetModules()[0].GetType("Maze.MazeWalker").GetMethod("startWalking").Invoke(null, parameters);
		return 0;
	}
```

It loads and runs `Maze.Maze` and `Maze.Mazewalker`, the former is responsible for constructing the maze boundaries from using a function `GetRandomSeed()`
```c#
		public static int GetRandomSeed()
		{
			return (int)DateTime.Now.Subtract(new DateTime(1970, 1, 1)).TotalSeconds;
		}
```
which is one of the functions which are changed during runtime to
```c#
		public static int GetRandomSeed()
		{
			return 1337;
		}
```

---

Then there are several other functions which are responsible for verifying and traversing the maze using our inputs, for eg,
```c#
private static void visitField_0_0(string oldInput)
{
	MazeWalker.checkLastTransition();
	ConsoleKeyInfo consoleKeyInfo = Console.ReadKey();
	bool flag = consoleKeyInfo.KeyChar == 'w';
	if (flag)
	{
		MazeWalker.outOfBounds(oldInput + consoleKeyInfo.KeyChar.ToString());
	}
	else
	{
		bool flag2 = consoleKeyInfo.KeyChar == 'a';
		if (flag2)
		{
			MazeWalker.outOfBounds(oldInput + consoleKeyInfo.KeyChar.ToString());
		}
		else
		{
			bool flag3 = consoleKeyInfo.KeyChar == 's';
			if (flag3)
			{
				MazeWalker.visitField_0_1(oldInput + consoleKeyInfo.KeyChar.ToString());
			}
			else
			{
				bool flag4 = consoleKeyInfo.KeyChar == 'd';
				if (flag4)
				{
					MazeWalker.visitField_1_0(oldInput + consoleKeyInfo.KeyChar.ToString());
				}
				else
				{
					MazeWalker.isValid = false;
					MazeWalker.visitField_1_0(oldInput + consoleKeyInfo.KeyChar.ToString());
				}
			}
		}
	}
}

```
The characters checked against in the decompilation is `wasd` but during runtime functions similar to the above one are changed, specifically the character checked
against are changed for every function during the JIT Hook.

My approach to solving this was to completely debug the binary to construct the maze, find the solution and traverse it. I built a excel sheet script to construct the maze
and my team members produced a solution for the maze parallely. 

Debugging the whole way through we finally receieve the flag, 

flag: `ALLES!{vfpzjtwmcdlvygjzabcsmlkjefgwmndxwrstucmwzhrucylowsfi}`

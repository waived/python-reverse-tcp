PYTHON SHELL:

Description:
      Via a Reverse-TCP-connection, the 'server.py' controller can manage
      multiple incoming-connections from devices infected with 'client.py'

      Initially built with the intent of being used against Linux/Unix
      environments, this script can easily be modified and used on 
      the Windows NT platforms as well.

Note: There are no features/functions built into this shell. It only
      functions as a raw terminal environment, either using SH, BASH,
      or Command-Prompt statements. If said statements yield verbose
      output to the user, the client.py backdoor will report the 
      output back to the attacker.

      This shell CANNOT manage sessions with devices in a concurrent
      manner, nor switch between sessions. This is a basic shell design
      used for basic penetration testing / red teaming activities.

      If used on a Windows NT platform, using AutoPyToExe (fouond at
      https://pypi.org/project/auto-py-to-exe/) is a plausible option
      for converting the client.py to a packaged non-dependent Windows
      executable file.

Good luck, and use responsibly!

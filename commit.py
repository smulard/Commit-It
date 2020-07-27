
import datetime
import subprocess as cmd

current_time = datetime.datetime.now()


# Commit and push up latest changes
cp = cmd.run("git add .", check=True, shell=True)
print(cp)

cp = cmd.run(f"git commit -m 'adding {current_time}'", check=True, shell=True)
print(cp)

cp = cmd.run("git push -u origin develop -f", check=True, shell=True)
print(cp)

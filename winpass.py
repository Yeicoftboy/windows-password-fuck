import subprocess

def change_windows_password(username, password):
  """Change the password for the specified Windows user account.

  Args:
    username: The username of the Windows user account.
    password: The new password for the Windows user account.
  """

  # Mount the Windows partition.
  sudo_mount_command = "sudo mount /dev/sda1 /mnt"
  subprocess.check_call(sudo_mount_command.split())

  # Change to the mounted Windows partition.
  cd_command = "cd /mnt"
  subprocess.check_call(cd_command.split())

  # Find the SAM file.
  ls_command = "ls -l /mnt/Windows/System32/config/"
  subprocess.check_call(ls_command.split())

  # Edit the SAM file with the chntpw utility.
  chntpw_command = "sudo chntpw -i /mnt/Windows/System32/config/SAM"
  subprocess.check_call(chntpw_command.split())

  # Select the user account that you want to change the password for.
  chntpw_select_user_command = "chntpw -u {} SAM".format(username)
  subprocess.check_call(chntpw_select_user_command.split())

  # Enter the new password for the user account.
  chntpw_set_password_command = "1"
  subprocess.check_call(chntpw_set_password_command.split())

  # Save the changes and exit the chntpw utility.
  chntpw_save_changes_command = "q"
  subprocess.check_call(chntpw_save_changes_command.split())

  # Unmount the Windows partition.
  sudo_umount_command = "sudo umount /mnt"
  subprocess.check_call(sudo_umount_command.split())

if __name__ == "__main__":
  # Get the username and password from the user.
  username = input("Enter the Windows username: ")
  password = input("Enter the new Windows password: ")

  # Change the Windows password.
  change_windows_password(username, password)

  # Print a message to the user.
  print("The Windows password has been changed.")

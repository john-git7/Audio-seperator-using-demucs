import subprocess
import os

input_audio = "input.mp3"
output_dir = "separated_audio"
os.makedirs(output_dir, exist_ok=True)
command = f"demucs -o {output_dir} {input_audio}"
subprocess.run(command, shell=True)
print(f"Separation complete! Check the '{output_dir}' folder for results.")


#commaand for the running demucs - demucs -n htdemucs -o "D:\test 2\output" ""
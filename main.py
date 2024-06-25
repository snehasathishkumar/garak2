import subprocess

def run_garak_command(model_type:str , model_name:str, generations:int):
    command = [
        'python', '-m', 'garak',
        '--model_type', model_type,
        '--model_name', model_name,
        '--probes', 'lmrc.Profanity',
        '--generations', generations
    ]
    print(type("sucess"))

    try:
        subprocess.check_call(command)
        print("Garak command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the Garak command: {e}")
    return 0

if __name__ == "__main__":
    print("main")

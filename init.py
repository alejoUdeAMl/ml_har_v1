github_repo = 'alejoUdeAMl/ml_har_v1'
zip_file_url = 'https://github.com/alejoUdeAMl/ml_har_v1/archive/main.zip'

def init(force_download=False):
    from IPython.display import display, HTML
    js = """
<meta name="google-signin-client_id"
      content="461673936472-kdjosv61up3ac1ajeuq6qqu72upilmls.apps.googleusercontent.com"/>
<script src="https://apis.google.com/js/client:platform.js?onload=google_button_start"></script>
    """

    display(HTML(js))

    if force_download or not os.path.exists("local"):
        print("replicating local resources")
        dirname = github_repo.split("/")[-1]+"-main/"
        if os.path.exists(dirname):
            shutil.rmtree(dirname)
        r = requests.get(zip_file_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
        if os.path.exists("local"):
            shutil.rmtree("local")
        if os.path.exists(dirname+"/content/local"):
            shutil.move(dirname+"/content/local", "local")
        elif os.path.exists(dirname+"/local"):
            shutil.move(dirname+"/local", "local")
        shutil.rmtree(dirname)

def install_sourcedefender():
    print('enabling encryption...')
    output = subprocess.run(['pip', 'install', 'sourcedefender==7.0.0'], stderr=subprocess.PIPE)

    if output.returncode != 0:
        STDOUT_RED_COLOR = '\033[91m'
        STDOUT_RESET_COLOR = '\033[0m'
        print('Sourcedefender installation failed, returning')
        print(STDOUT_RED_COLOR + output.stderr.decode('ASCII') + STDOUT_RESET_COLOR)
    else:
        print('encryption enabled')


import requests, zipfile, io, os, shutil, subprocess

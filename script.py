import mechanize

url = mechanize.Browser() 
url.open("https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/viewform") #requesting the gle form base url


for i in range(1,101):
    url.form = list(url.forms())[0]
    url.set_all_readonly(False)
    url["entry.1156409"] = "Kartikeya" ##name
    url["entry.210055283"] = "190420"  ##roll number

    #fill the radio
    control = url.form.find_control(name="entry.192452008")
    control.disabled = False
    control.value = "Yes"

    # fill the link to git repo
    url["entry.446099277"]="https://github.com/kartikcode/Python-Form-Automater.git"
    
    url.submit()
    url.back()

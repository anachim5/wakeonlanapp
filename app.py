from flask import Flask, render_template, request, redirect, url_for
import yaml
import subprocess

app = Flask(__name__)

def load_config():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config

@app.route('/')
def index():
    config = load_config()
    devices = config.get('devices', [])
    result = request.args.get('result', '')
    return render_template('index.html', devices=devices, result=result)

@app.route('/wake/<mac>', methods=['POST'])
def wake(mac):
    # Run the ansible playbook to wake up the device
    subprocess.run(['ansible-playbook', 'wake_on_lan.yml', '--extra-vars', f'mac_address={mac}'])

    # Wait for 3 minutes and then run the ansible playbook to ping the device
    subprocess.run(['ansible-playbook', 'ping_after_wait.yml', '--extra-vars', f'mac_address={mac}'])

    result = f"Sent Wake-on-LAN packet to {mac}. Check back in a few minutes for status."
    return redirect(url_for('index', result=result))

# Function to load config from YAML file
def load_config():
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config

# Function to save config to YAML file
def save_config(config):
    with open('config.yml', 'w') as file:
        yaml.safe_dump(config, file, default_flow_style=False)

# Route to display devices and allow CRUD operations
@app.route('/devices', methods=['GET', 'POST'])
def devices():
    config = load_config()
    devices = config.get('devices', [])

    if request.method == 'POST':
        action = request.form['action']

        if action == 'add':
            name = request.form['name']
            mac_address = request.form['mac_address']
            devices.append({'name': name, 'mac_address': mac_address})
            save_config(config)
            return redirect(url_for('devices'))

        elif action == 'edit':
            index = int(request.form['index'])
            name = request.form['name']
            mac_address = request.form['mac_address']
            devices[index]['name'] = name
            devices[index]['mac_address'] = mac_address
            save_config(config)
            return redirect(url_for('devices'))

        elif action == 'delete':
            index = int(request.form['index'])
            del devices[index]
            save_config(config)
            return redirect(url_for('devices'))

    return render_template('devices.html', devices=devices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

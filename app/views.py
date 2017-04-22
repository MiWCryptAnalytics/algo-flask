from flask import render_template, flash, redirect
from app import app
from .forms import *


@app.route('/')
@app.route('/index')
def index():
    return ("Algo VPN Cloud Factory")


@app.route('/algo', methods=['GET', 'POST'])
def algo():
    form = AlgoForm()
    return render_template('algo.html',
                           title='Algo VPN Factory',
                           form=form)

@app.route('/roles', methods=['GET', 'POST'])
def additional_roles():
    form = AlgoAdditionalrolesForm()
    return render_template('algo.html',
                           title='Algo VPN Factory',
                           form=form)

@app.route('/do', methods=['GET', 'POST'])
def digital_ocean():
    form = AlgoDigitaloceanForm()
    return render_template('algo.html',
                           title='Algo VPN Factory',
                           form=form)

@app.route('/azure', methods=['GET', 'POST'])
def azure():
    form = AlgoAzureForm()
    return render_template('algo.html',
                           title='Algo VPN Factory',
                           form=form)

@app.route('/aws', methods=['GET', 'POST'])
def aws():
    form = AlgoEc2Form()
    return render_template('algo.html',
                           title='Algo VPN Factory',
                           form=form)

@app.route('/gce', methods=['GET', 'POST'])
def gce():
    form = AlgoGceForm()
    return render_template('algo.html',
                           title='Algo VPN Factory',
                           form=form)

@app.route('/noncloud', methods=['GET', 'POST'])
def non_cloud():
    form = AlgoNoncloudForm()
    return render_template('algo.html',
                           title='Algo VPN Factory',
                           form=form)

@app.route('/user', methods=['GET', 'POST'])
def user():
    form = AlgoUsermanagementForm()
    return render_template('algo.html',
                           title='Algo VPN Factory',
                           form=form)